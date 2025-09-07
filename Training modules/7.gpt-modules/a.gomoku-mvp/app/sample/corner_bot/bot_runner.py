import sys, json

def main():
    data = json.loads(sys.stdin.read())
    board = data["board"]
    size = len(board)
    # ưu tiên 4 góc -> biên -> trung tâm -> ô trống đầu tiên
    candidates = [(0,0),(size-1,0),(0,size-1),(size-1,size-1)]
    for (x,y) in candidates:
        if board[y][x] == 0:
            print(f"{x},{y}")
            return
    # biên
    for x in range(size):
        if board[0][x]==0: print(f"{x},0"); return
        if board[size-1][x]==0: print(f"{x},{size-1}"); return
    for y in range(size):
        if board[y][0]==0: print(f"0,{y}"); return
        if board[y][size-1]==0: print(f"{size-1},{y}"); return
    # trung tâm
    c = size//2
    if board[c][c]==0:
        print(f"{c},{c}")
        return
    # fallback: ô trống đầu tiên
    for y in range(size):
        for x in range(size):
            if board[y][x]==0:
                print(f"{x},{y}")
                return

if __name__ == "__main__":
    main()
