# Structure
```
backend/
  ├── src/
  │   ├── index.js
  │   ├── routes.js
  │   ├── models.js
  ├── package.json
frontend/
  ├── src/
  │   ├── App.js
  │   ├── api.js
  ├── package.json
init.sql
```
# Requirement (for image build)
## Frontend (React)
- Base image: node:18-alpine để build → sau đó thường copy sang nginx:alpine để serve static file.
- Copy source code (src/, package.json).
- Cài dependency: react, react-dom, axios, react-scripts.
- Build script: npm run build.
- Serve static file bằng Nginx (port 80).
- Cần config API endpoint (ví dụ REACT_APP_API_URL=http://backend:4000/api) → truyền bằng ENV khi build hoặc runtime.
## Backend (Node.js + Express + Sequelize)
- Base image: node:18-alpine (gọn nhẹ, phổ biến).
- Copy source code (src/, package.json).
- Cần cài dependency: express, sequelize, mysql2, cors, body-parser.
- Environment variables (nên config bằng ENV, sau này dễ dùng K8s Secret):
  - DB_HOST=localhost
  - DB_USER=root
  - DB_PASS=password
  - DB_NAME=todo_db
- Port: 4000.
- Entrypoint: node src/index.js.