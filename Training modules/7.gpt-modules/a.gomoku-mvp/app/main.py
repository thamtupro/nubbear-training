from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import os, zipfile, tempfile, shutil, threading, time, random

from app.storage import init_storage, register_bot, list_bots, enqueue, dequeue_batch, queue_len, get_matches, get_streak
from app.match_runner import run_match

app = FastAPI(title="Gomoku MVP API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

MAX_CONCURRENCY = 2  # theo yêu cầu: 2-3 trận đồng thời là đủ
_running = 0
_lock = threading.Lock()

def matchmaker_loop():
    global _running
    while True:
        try:
            # giới hạn số trận đồng thời
            with _lock:
                if _running >= MAX_CONCURRENCY:
                    time.sleep(0.5)
                    continue

            # lấy batch nhỏ để ghép cặp theo streak ±2
            batch = dequeue_batch(10)
            if not batch:
                time.sleep(0.3)
                continue

            # phân loại theo streak
            def streak_of(bid): return get_streak(bid)
            waiting = list(batch)
            used = set()
            pairs = []

            # ưu tiên ghép chênh lệch streak <= 2
            for i, a in enumerate(waiting):
                if a in used: continue
                sa = streak_of(a)
                cand = None
                for j in range(i+1, len(waiting)):
                    b = waiting[j]
                    if b in used: continue
                    if abs(sa - streak_of(b)) <= 2:
                        cand = b
                        break
                if cand is not None:
                    pairs.append((a, cand))
                    used.add(a); used.add(cand)

            # ghép ngẫu nhiên phần còn lại
            leftovers = [x for x in waiting if x not in used]
            random.shuffle(leftovers)
            while len(leftovers) >= 2:
                a = leftovers.pop()
                b = leftovers.pop()
                pairs.append((a, b))

            # chạy các trận (non-blocking bằng thread)
            for a, b in pairs:
                with _lock:
                    _running += 1
                threading.Thread(target=_run_one, args=(a, b), daemon=True).start()

        except Exception as e:
            print("matchmaker error:", e)
            time.sleep(1)

def _run_one(a: int, b: int):
    global _running
    try:
        run_match(a, b)
    except Exception as e:
        print("match error:", e)
    finally:
        with _lock:
            _running -= 1

@app.on_event("startup")
def on_startup():
    init_storage()
    threading.Thread(target=matchmaker_loop, daemon=True).start()

@app.post("/upload_zip")
async def upload_zip(name: str, file: UploadFile = File(...)):
    # file zip phải chứa bot_runner.py
    if not file.filename.endswith(".zip"):
        raise HTTPException(400, "Please upload a .zip containing bot_runner.py")
    with tempfile.TemporaryDirectory() as td:
        zip_path = os.path.join(td, "bot.zip")
        with open(zip_path, "wb") as f:
            f.write(await file.read())
        with zipfile.ZipFile(zip_path, "r") as z:
            if "bot_runner.py" not in z.namelist():
                raise HTTPException(400, "zip must include bot_runner.py at root")
            z.extractall(td)
        bot_id = register_bot(name=name, src_dir=td)
    return {"bot_id": bot_id}

@app.post("/register_sample/{sample_name}")
def register_sample(sample_name: str):
    sample_dir = os.path.join(os.path.dirname(__file__), "samples", sample_name)
    if not os.path.isdir(sample_dir):
        raise HTTPException(404, "Sample not found")
    bot_id = register_bot(name=f"{sample_name}", src_dir=sample_dir)
    return {"bot_id": bot_id}

@app.post("/join_queue/{bot_id}")
def join(bot_id: int):
    enqueue(bot_id)
    return {"status": "enqueued", "queue_len": queue_len()}

@app.get("/bots")
def bots():
    return list_bots()

@app.get("/matches")
def matches(limit: int = 20):
    return {"matches": get_matches(limit=limit)}

@app.get("/queue")
def qlen():
    return {"queue_len": queue_len()}
