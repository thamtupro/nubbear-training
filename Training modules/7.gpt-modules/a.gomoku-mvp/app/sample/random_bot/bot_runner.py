import sys, json, random

def pick(board):
    size = len(board)
    empty = [(x,y) for y in range(size) for x in range(size) if board[y][x] == 0]
    return random.choice(empty) if empty else (0,0)

def main():
    data = json.loads(sys.stdin.read())
    board = data["board"]
    x,y = pick(board)
    print(f"{x},{y}")

if __name__ == "__main__":
    main()
