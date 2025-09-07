# Base image: dùng Node 18 (alpine cho nhẹ)
FROM node:18-alpine

# Làm việc trong /app 
WORKDIR /app

# Copy package.json trước để cache dependency
COPY package*.json ./

# Cài dependency
RUN npm install

# Copy toàn bộ source code
COPY . .

# Expose port cho backend
EXPOSE 4000

# Environment variables (sẽ override bằng docker-compose hoặc k8s secret)
# ENV DB_HOST=localhost
# ENV DB_USER=root
# ENV DB_PASS=password
# ENV DB_NAME=todo_db

# Run app
CMD ["node", "src/index.js"]
