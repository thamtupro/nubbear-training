# Repo Structure
```
gomoku-mvp/
├─ app/
│  ├─ main.py               # FastAPI + background matchmaker
│  ├─ gomoku_env.py         # Luật Gomoku
│  ├─ match_runner.py       # Chạy 1 trận (gọi 2 bot qua subprocess)
│  ├─ storage.py            # Lưu bot, queue, streak (JSON file)
│  ├─ utils.py              # Hàm tiện ích
│  └─ samples/
│     ├─ random_bot/bot_runner.py   # bot random hợp lệ
│     └─ corner_bot/bot_runner.py   # bot chơi ưu tiên góc/biên
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
└─ README.md                # hướng dẫn chạy + test
```
---
# Gomoku MVP

## Chạy
```bash
docker compose up --build -d

```
## Đăng ký 2 bot mẫu
```
curl -X POST localhost:8000/register_sample/random_bot
# => {"bot_id": 17...}
curl -X POST localhost:8000/register_sample/corner_bot
# => {"bot_id": 17...}
curl localhost:8000/bots
```
## Xếp hàng (queue) & Tự động ghép trận

```
# ví dụ enqueue mỗi bot 2 lần (giả lập nhiều người chơi dùng cùng bot)

curl -X POST localhost:8000/join_queue/<<BOT_ID_RANDOM>>
curl -X POST localhost:8000/join_queue/<<BOT_ID_CORNER>>
curl -X POST localhost:8000/join_queue/<<BOT_ID_RANDOM>>
curl -X POST localhost:8000/join_queue/<<BOT_ID_CORNER>>
curl localhost:8000/queue
```

## Xem danh sách trận (đợi vài giây sau khi chạy bot)
```
curl localhost:8000/matches?limit=10
```

## Expected outcome
- /queue giảm dần khi matchmaker lấy bot ra ghép.
- /matches trả về các bản ghi dạng:
```
{
  "matches": [
    {"bot_a":171234567,"bot_b":171234890,"winner":171234890,"reason":"win","moves":23,"duration_s":0.123},
    {"bot_a":171234567,"bot_b":171234890,"winner":null,"reason":"draw","moves":225,"duration_s":1.421}
  ]
}

```
- `corner_bot` có xu hướng ít thua hơn `random_bot` (khởi đầu ở góc/biên ổn định).

# Cách chạy nhanh

1) clone code (hoặc copy các file trên vào cấu trúc thư mục như đã liệt kê).  

2) `docker compose up --build -d`  

3) Đăng ký bot mẫu:
```bash
curl -X POST localhost:8000/register_sample/random_bot
curl -X POST localhost:8000/register_sample/corner_bot
```

4) Lấy bot_id từ /bots, rồi enqueue vài lần:
```bash
curl -X POST localhost:8000/join_queue/<BOT_ID_RANDOM>
curl -X POST localhost:8000/join_queue/<BOT_ID_CORNER>
```

5) Xem kết quả:
```bash
curl localhost:8000/matches?limit=10
```