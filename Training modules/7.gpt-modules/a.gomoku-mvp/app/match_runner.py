import time, json
from typing import Optional, Tuple
from app.gomoku_env import GomokuEnv, BLACK, WHITE
from app.storage import get_bot_path, add_match, update_streak
from app.utils import run_bot

def parse_action(s: str) -> Optional[Tuple[int,int]]:
    try:
        x, y = s.split(",")
        return int(x), int(y)
    except:
        return None

def run_match(bot_a: int, bot_b: int, move_timeout=2.0, max_moves=15*15):
    env = GomokuEnv(size=15, win_len=5)
    env.reset()
    path_a = get_bot_path(bot_a)
    path_b = get_bot_path(bot_b)

    moves = []
    start_ts = time.time()
    while not env.done and len(moves) < max_moves:
        state = {"board": env.board.tolist(), "player": int(env.current_player)}
        bot_dir = path_a if env.current_player == BLACK else path_b
        out, err = run_bot(bot_dir, state, timeout_sec=move_timeout)
        if out is None:
            # lỗi -> đối thủ thắng
            winner = bot_b if env.current_player == BLACK else bot_a
            loser  = bot_a if env.current_player == BLACK else bot_b
            add_match({
                "bot_a": bot_a, "bot_b": bot_b, "winner": winner,
                "reason": "bot_failed", "err": err, "duration_s": round(time.time()-start_ts, 3)
            })
            update_streak(winner, loser)
            return winner, {"reason":"bot_failed", "err": err}

        action = parse_action(out)
        if action is None:
            winner = bot_b if env.current_player == BLACK else bot_a
            loser  = bot_a if env.current_player == BLACK else bot_b
            add_match({
                "bot_a": bot_a, "bot_b": bot_b, "winner": winner,
                "reason": "bad_action", "raw": out, "duration_s": round(time.time()-start_ts, 3)
            })
            update_streak(winner, loser)
            return winner, {"reason":"bad_action", "raw": out}

        _, _, done, info = env.step(action)
        moves.append({"p": int(WHITE if env.current_player == BLACK else BLACK), "move": action})
        if done:
            if env.winner is None:
                # Hòa
                add_match({
                    "bot_a": bot_a, "bot_b": bot_b, "winner": None,
                    "reason": "draw", "moves": len(moves), "duration_s": round(time.time()-start_ts, 3)
                })
                update_streak(None, None)
                return None, {"reason":"draw"}
            else:
                winner = bot_a if env.winner == BLACK else bot_b
                loser  = bot_b if env.winner == BLACK else bot_a
                add_match({
                    "bot_a": bot_a, "bot_b": bot_b, "winner": winner,
                    "reason": "win", "moves": len(moves), "duration_s": round(time.time()-start_ts, 3)
                })
                update_streak(winner, loser)
                return winner, {"reason":"win"}

    # quá số nước tối đa
    add_match({
        "bot_a": bot_a, "bot_b": bot_b, "winner": None,
        "reason": "max_moves", "moves": len(moves), "duration_s": round(time.time()-start_ts, 3)
    })
    update_streak(None, None)
    return None, {"reason":"max_moves"}
