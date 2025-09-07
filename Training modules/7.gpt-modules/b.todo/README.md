Project: Web App 3 tầng trên Kubernetes (todo)
│
├── 1. Kubernetes cơ bản (Triển khai ứng dụng)
│   ├── 1.1 Deployment + Service
│   │     - Backend API (Express)
│   │     - Frontend (Nginx serve static)
│   │     - Kiểm tra rolling update, scale
│   ├── 1.2 Ingress + TLS
│   │     - Ingress Controller (nginx)
│   │     - Host-based routing (frontend.local, api.local)
│   │     - Self-signed certificate (Secret type tls)
│   ├── 1.3 Config & Secret
│   │     - DB password trong Secret
│   │     - App config trong ConfigMap
│   ├── 1.4 StatefulSet + PVC
│   │     - MariaDB StatefulSet
│   │     - PersistentVolume + StorageClass
│   │     - Test DB persistence (xóa Pod, data còn giữ)
│
├── 2. Observability (Giám sát & Logging)
│   ├── 2.1 Monitoring
│   │     - Cài Prometheus, Grafana (Helm chart)
│   │     - Scrape metrics từ backend + DB
│   │     - Tạo dashboard custom (CPU, memory, request)
│   │     - Alert rule (CPU > 80%)
│   ├── 2.2 Logging
│   │     - Filebeat DaemonSet
│   │     - Logstash filter (parse JSON log từ backend)
│   │     - Elasticsearch index
│   │     - Kibana visualize log
│   ├── 2.3 Tracing (Bonus)
│         - OpenTelemetry SDK cho backend
│         - Jaeger/Tempo để trace request
│
├── 3. CI/CD
│   ├── 3.1 Dockerization
│   │     - Dockerfile multi-stage cho backend
│   │     - Dockerfile cho frontend
│   ├── 3.2 CI Pipeline
│   │     - GitHub Actions/GitLab CI
│   │     - Step: test → build → push image
│   ├── 3.3 CD Pipeline
│   │     - ArgoCD hoặc Tekton
│   │     - Auto-sync manifest khi có thay đổi
│
├── 4. IaC / Cloud (Nâng cao)
│   ├── 4.1 Terraform cơ bản
│   │     - Tạo namespace, secret, configmap bằng Terraform
│   │     - Tạo cluster trên Kind/Minikube
│   ├── 4.2 Cloud thử nghiệm
│         - Deploy app trên EKS/GKE/AKS
│         - Sử dụng LoadBalancer service
