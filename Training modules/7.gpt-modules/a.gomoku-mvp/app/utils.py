import subprocess, json, os

def run_bot(bot_dir: str, state: dict, timeout_sec: float = 2.0):
    """
    Chạy bot_runner.py trong thư mục bot. Bot đọc stdin JSON {'board':..., 'player':...}
    Và in ra 'x,y'
    """
    cmd = ["python", "bot_runner.py"]
    proc = subprocess.Popen(cmd, cwd=bot_dir, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        out, err = proc.communicate(json.dumps(state), timeout=timeout_sec)
        if proc.returncode != 0:
            return None, f"rc={proc.returncode} err={err[:200]}"
        return out.strip(), None
    except subprocess.TimeoutExpired:
        proc.kill()
        return None, "timeout"
