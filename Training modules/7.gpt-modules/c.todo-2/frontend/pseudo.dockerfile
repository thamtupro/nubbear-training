# -------- Stage 1: Build React --------
FROM node:18-alpine AS build

WORKDIR /app

# Copy package.json để cache dependency
COPY package*.json ./
RUN npm install

# Copy source và build
COPY . .
RUN npm run build

# -------- Stage 2: Serve with Nginx --------
FROM nginx:alpine

# Copy file build từ stage 1 sang nginx
COPY --from=build /app/build /usr/share/nginx/html

# Copy default nginx config (nếu muốn API proxy)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
