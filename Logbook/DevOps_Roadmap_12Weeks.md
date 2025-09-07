# DevOps Roadmap 12 Tuần (Chi tiết theo Module)

---

## 📅 Week 1 – Linux/Unix (Foundations)

### Module 1: User & Group Management
- **Requirement:**
  - Hiểu /etc/passwd, /etc/group, UID/GID.
  - Tạo user, group, gán quyền sudo.
  - Quản lý password & SSH key.
- **Outcome:**
  - Tạo user `devuser`, add vào group `devops`.
  - Cho phép `devuser` chạy `sudo systemctl restart nginx`.
  - Login SSH bằng key cho `devuser`.
- **Keyword:** `linux useradd groupadd sudoers tutorial`, `ssh key authentication linux`

### Module 2: Permission & Ownership
- **Requirement:**
  - Hiểu rwx, owner/group/other.
  - Sử dụng chmod, chown, umask.
  - Phân biệt soft link & hard link.
- **Outcome:**
  - Tạo file log, phân quyền chỉ cho `devuser` đọc/ghi.
  - Tạo thư mục `teamshare` để nhiều user cùng truy cập.
- **Keyword:** `linux file permissions chmod chown`, `umask examples`

### Module 3: Systemd & Service Management
- **Requirement:**
  - Hiểu unit file, target, dependency.
  - Dùng systemctl để start/stop/enable service.
  - Tạo 1 custom systemd service đơn giản.
- **Outcome:**
  - Viết 1 systemd unit để chạy script hello.sh khi boot.
  - Enable + kiểm tra log qua journalctl -u hello.service.
- **Keyword:** `systemd basics tutorial`, `systemd unit file example`, `journalctl usage`

### Module 4: Logrotate
- **Requirement:**
  - Hiểu logrotate config, rotate schedule, compression.
  - Cấu hình logrotate cho app custom log.
- **Outcome:**
  - Tạo file log `/var/log/app/app.log`.
  - Viết rule logrotate: daily, giữ 7 bản, nén gzip.
  - Kiểm tra bằng logrotate -f.
- **Keyword:** `logrotate configuration example`, `logrotate tutorial linux`

**✅ Tổng Outcome Tuần 1:** dựng server demo, quản lý user/permission, viết systemd service, config logrotate.

---

## 📅 Week 2 – Networking (Linux/Net Core)

### Module 1: TCP/IP & Tools
- **Requirement:** hiểu TCP/IP, DNS, HTTP; dùng ping, curl, dig, netstat.
- **Outcome:** kiểm tra kết nối web, tra DNS domain, phân tích header HTTP.
- **Keyword:** `linux networking basics`, `curl dig tutorial`

### Module 2: Firewall & iptables
- **Requirement:** viết rule iptables/ufw, NAT, forward basic.
- **Outcome:** chặn port 22 từ IP cụ thể, mở port 8080 cho app.
- **Keyword:** `iptables examples`, `ufw tutorial`

### Module 3: Reverse Proxy (Nginx)
- **Requirement:** config reverse proxy, load balancing, health check.
- **Outcome:** dựng nginx proxy cho 2 backend app, test round-robin.
- **Keyword:** `nginx reverse proxy config`, `nginx load balancing tutorial`

### Module 4: TLS/SSL Basics
- **Requirement:** hiểu TLS, certificate, self-signed.
- **Outcome:** bật TLS self-signed cho nginx reverse proxy.
- **Keyword:** `nginx ssl self signed cert`, `openssl generate cert`

**✅ Tổng Outcome Tuần 2:** dựng nginx reverse proxy có TLS, firewall rule chuẩn.

---

## 📅 Week 3 – Cloud Basics

### Module 1: IAM Basics
- **Requirement:** user, role, policy; principle of least privilege.
- **Outcome:** tạo user dev với quyền chỉ upload object storage.
- **Keyword:** `aws iam basics`, `gcp iam tutorial`

### Module 2: Compute Service
- **Requirement:** tạo VM (AWS EC2, GCP Compute Engine).
- **Outcome:** deploy VM chạy web server.
- **Keyword:** `aws ec2 launch tutorial`, `gcp compute engine basics`

### Module 3: Storage Service
- **Requirement:** object vs block storage, S3/Blob basics.
- **Outcome:** tạo bucket, upload/download file qua CLI.
- **Keyword:** `aws s3 cli tutorial`, `gcp cloud storage cli`

**✅ Tổng Outcome Tuần 3:** deploy 1 VM + 1 bucket cloud, IAM user hạn chế.

---

## 📅 Week 4 – Terraform Fundamentals

### Module 1: Provider & Resource
- **Requirement:** init provider, viết resource VM/storage.
- **Outcome:** script tạo VM + bucket.
- **Keyword:** `terraform provider resource example`

### Module 2: Variables & Output
- **Requirement:** variable, output.
- **Outcome:** script VM config qua variable, output IP.
- **Keyword:** `terraform variables output tutorial`

### Module 3: State Management
- **Requirement:** hiểu state, terraform.tfstate.
- **Outcome:** show state, refresh, import resource nhỏ.
- **Keyword:** `terraform state management tutorial`

**✅ Tổng Outcome Tuần 4:** script Terraform apply/destroy VM + bucket, dùng variable & output.

---

## 📅 Week 5 – CI/CD Basics

### Module 1: Pipeline Concepts
- **Requirement:** build, test, deploy stage.
- **Outcome:** viết pipeline YAML (GitHub/GitLab) chạy unit test.
- **Keyword:** `github actions pipeline tutorial`, `gitlab ci yaml example`

### Module 2: Docker Integration
- **Requirement:** build image trong pipeline.
- **Outcome:** pipeline build image app, push registry.
- **Keyword:** `ci cd docker build pipeline`

**✅ Tổng Outcome Tuần 5:** pipeline build-test, build docker image.

---

## 📅 Week 6 – CI/CD Advanced

### Module 1: Artifact & Cache
- **Requirement:** cache dependency, save artifact.
- **Outcome:** pipeline NodeJS với cache npm + publish artifact.
- **Keyword:** `ci cd caching github actions`, `gitlab artifact tutorial`

### Module 2: Multi-stage Pipeline
- **Requirement:** split build, test, deploy.
- **Outcome:** pipeline deploy staging sau build, test pass.
- **Keyword:** `ci cd multi stage pipeline example`

**✅ Tổng Outcome Tuần 6:** pipeline end-to-end multi-stage, optimize cache.

---

## 📅 Week 7 – GitOps Intro

### Module 1: ArgoCD Basics
- **Requirement:** install ArgoCD, repo sync.
- **Outcome:** deploy app demo từ Git repo qua ArgoCD.
- **Keyword:** `argocd getting started`

### Module 2: GitOps Concepts
- **Requirement:** desired state, rollback.
- **Outcome:** update manifest, ArgoCD auto-sync, rollback thử.
- **Keyword:** `gitops argo basics`

**✅ Tổng Outcome Tuần 7:** GitOps deploy app, rollback bằng Git.

---

## 📅 Week 8 – Security Basics

### Module 1: Secrets Management
- **Requirement:** secret vs config, Sealed Secrets basics.
- **Outcome:** deploy secret k8s an toàn bằng Sealed Secrets.
- **Keyword:** `kubernetes sealed secrets tutorial`

### Module 2: Image Scanning
- **Requirement:** scan vuln, integrate CI.
- **Outcome:** pipeline tích hợp Trivy scan.
- **Keyword:** `trivy ci cd integration`

**✅ Tổng Outcome Tuần 8:** pipeline có security scan, deploy secret bằng Sealed Secrets.

---

## 📅 Week 9 – Kubernetes Storage & Scaling

### Module 1: Storage
- **Requirement:** PV, PVC, StorageClass.
- **Outcome:** deploy DB stateful dùng PVC + StorageClass.
- **Keyword:** `kubernetes pvc storageclass tutorial`

### Module 2: Scaling
- **Requirement:** HPA (CPU, custom metric).
- **Outcome:** app autoscale pod khi load cao.
- **Keyword:** `kubernetes hpa tutorial`

**✅ Tổng Outcome Tuần 9:** app DB stateful với PVC, autoscale pod bằng HPA.

---

## 📅 Week 10 – Ingress & RBAC

### Module 1: Ingress
- **Requirement:** ingress-nginx basics.
- **Outcome:** expose app qua ingress, HTTPS.
- **Keyword:** `kubernetes ingress nginx example`

### Module 2: RBAC
- **Requirement:** Role, RoleBinding, ServiceAccount.
- **Outcome:** user dev chỉ đọc pod, không xoá được.
- **Keyword:** `kubernetes rbac rolebinding tutorial`

**✅ Tổng Outcome Tuần 10:** app có ingress TLS, RBAC phân quyền dev.

---

## 📅 Week 11 – Prometheus Advanced

### Module 1: Metric Types
- **Requirement:** counter, gauge, histogram, summary.
- **Outcome:** instrument app có counter/histogram metric.
- **Keyword:** `prometheus metric types`, `prometheus histogram example`

### Module 2: Alert Rules
- **Requirement:** viết alert rule meaningful.
- **Outcome:** alert khi request latency > 1s, 95th percentile.
- **Keyword:** `prometheus alert rules latency`

**✅ Tổng Outcome Tuần 11:** app có custom metric, Grafana dashboard latency.

---

## 📅 Week 12 – Tracing & Incident Mgmt

### Module 1: Tracing (OpenTelemetry)
- **Requirement:** instrument app, Jaeger.
- **Outcome:** trace request end-to-end qua Jaeger UI.
- **Keyword:** `opentelemetry jaeger tutorial`

### Module 2: Incident Management
- **Requirement:** on-call, runbook, postmortem.
- **Outcome:** simulate incident, follow runbook, viết postmortem.
- **Keyword:** `incident runbook example`, `postmortem template sre`

**✅ Tổng Outcome Tuần 12:** app có tracing OTEL, simulate incident + viết postmortem.

---

# 📌 Tổng quan
- **Tháng 1:** Linux/Net + Cloud/IaC foundation.
- **Tháng 2:** CI/CD + Security cơ bản.
- **Tháng 3:** Kubernetes nâng cao + Observability (Prometheus, Tracing, SRE).
