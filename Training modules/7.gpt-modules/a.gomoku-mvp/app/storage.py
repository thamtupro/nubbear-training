import json, os, threading, time, shutil
from typing import Dict, Any, Optional, List, Tuple

DATA_DIR = "/data"
BOTS_DIR = os.path.join(DATA_DIR, "bots")
STATE_FILE = os.path.join(DATA_DIR, "state.json")

_lock = threading.Lock()
_state_cache: Dict[str, Any] = {
    "bots": {},          # bot_id -> {"name":..., "path":...}
    "streaks": {},       # bot_id -> int
    "queue": [],         # list of bot_id in FIFO
    "matches": []        # append-only log
}

def init_storage():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(BOTS_DIR, exist_ok=True)
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
            _state_cache.update(data)
    persist()

def persist():
    with _lock:
        tmp = STATE_FILE + ".tmp"
        with open(tmp, "w") as f:
            json.dump(_state_cache, f)
        os.replace(tmp, STATE_FILE)

def next_id() -> int:
    # simple incremental id
    return int(time.time() * 1000) % 10**9

def register_bot(name: str, src_dir: str) -> int:
    bot_id = next_id()
    dst = os.path.join(BOTS_DIR, f"bot_{bot_id}")
    shutil.copytree(src_dir, dst)
    with _lock:
        _state_cache["bots"][str(bot_id)] = {"name": name, "path": dst}
        if str(bot_id) not in _state_cache["streaks"]:
            _state_cache["streaks"][str(bot_id)] = 0
    persist()
    return bot_id

def list_bots():
    with _lock:
        return {k: v for k, v in _state_cache["bots"].items()}

def enqueue(bot_id: int):
    with _lock:
        _state_cache["queue"].append(bot_id)
    persist()

def dequeue_batch(n: int) -> List[int]:
    with _lock:
        take = _state_cache["queue"][:n]
        _state_cache["queue"] = _state_cache["queue"][n:]
    persist()
    return take

def queue_len() -> int:
    with _lock:
        return len(_state_cache["queue"])

def get_streak(bot_id: int) -> int:
    with _lock:
        return int(_state_cache["streaks"].get(str(bot_id), 0))

def update_streak(winner_id: Optional[int], loser_id: Optional[int]):
    with _lock:
        if winner_id is not None:
            _state_cache["streaks"][str(winner_id)] = _state_cache["streaks"].get(str(winner_id), 0) + 1
        if loser_id is not None:
            _state_cache["streaks"][str(loser_id)] = 0
    persist()

def add_match(rec: Dict[str, Any]):
    with _lock:
        _state_cache["matches"].append(rec)
    persist()

def get_bot_path(bot_id: int) -> str:
    with _lock:
        return _state_cache["bots"][str(bot_id)]["path"]

def get_matches(limit=20):
    with _lock:
        return _state_cache["matches"][-limit:]
