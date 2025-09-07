from typing import Tuple, Dict, Any, List
import numpy as np

EMPTY, BLACK, WHITE = 0, 1, 2

class GomokuEnv:
    def __init__(self, size: int = 15, win_len: int = 5):
        self.size = size
        self.win_len = win_len
        self.board = np.zeros((size, size), dtype=np.int8)
        self.current_player = BLACK
        self.done = False
        self.winner = None
        self.last_move = None

    def reset(self) -> Dict[str, Any]:
        self.board.fill(EMPTY)
        self.current_player = BLACK
        self.done = False
        self.winner = None
        self.last_move = None
        return self.obs()

    def obs(self) -> Dict[str, Any]:
        return {
            "board": self.board.tolist(),
            "current_player": int(self.current_player),
            "last_move": self.last_move
        }

    def valid_actions(self) -> List[Tuple[int, int]]:
        ys, xs = np.where(self.board == EMPTY)
        return list(zip(xs.tolist(), ys.tolist()))

    def step(self, action: Tuple[int, int]):
        if self.done:
            raise RuntimeError("Game already finished")
        x, y = action
        if not (0 <= x < self.size and 0 <= y < self.size):
            self.done = True
            self.winner = WHITE if self.current_player == BLACK else BLACK
            return self.obs(), -1, True, {"reason": "invalid_out_of_bounds"}
        if self.board[y, x] != EMPTY:
            self.done = True
            self.winner = WHITE if self.current_player == BLACK else BLACK
            return self.obs(), -1, True, {"reason": "invalid_occupied"}

        self.board[y, x] = self.current_player
        self.last_move = (x, y)

        if self._check_win(x, y):
            self.done = True
            self.winner = self.current_player
            return self.obs(), 1, True, {"reason": "win"}

        if not self.valid_actions():
            self.done = True
            self.winner = None
            return self.obs(), 0, True, {"reason": "draw"}

        self.current_player = WHITE if self.current_player == BLACK else BLACK
        return self.obs(), 0, False, {}

    def _check_win(self, x: int, y: int) -> bool:
        p = self.board[y, x]
        for dx, dy in [(1,0),(0,1),(1,1),(1,-1)]:
            cnt = 1
            for sign in (1, -1):
                nx, ny = x + dx*sign, y + dy*sign
                while 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny, nx] == p:
                    cnt += 1
                    nx += dx*sign
                    ny += dy*sign
            if cnt >= self.win_len:
                return True
        return False
