# Lịch trình đào tạo Kubernetes 5 ngày

Lịch trình đào tạo Kubernetes trong 5 ngày, mỗi ngày 8 giờ (tổng 40 giờ), được thiết kế cho người học có kiến thức cơ bản về Linux và Docker. Lịch trình tập trung vào triển khai ứng dụng 3 thành phần (Frontend, Backend, Database) trên Kubernetes, sử dụng Deployment, ReplicaSet, Service, ConfigMap, Secret, Volume, Job, CronJob và kỹ năng debugging. Các chủ đề Ingress, Logging & Monitoring, Scheduling, Security, StatefulSet được loại bỏ.

## Ngày 1: Cơ bản Kubernetes
**Mục tiêu**: Hiểu các khái niệm cơ bản và thiết lập cụm Kubernetes.

| **Thời gian** | **Chủ đề/Bài học** | **Tài liệu tham khảo** | **Yêu cầu** | **Thực hành** |
|---------------|--------------------|-----------------------|-------------|---------------|
| 2h | **Giới thiệu Kubernetes**: Tổng quan, vai trò, thành phần (Control Plane, Nodes) | [Kubernetes Overview](https://kubernetes.io/docs/concepts/overview/), [What is Kubernetes](https://www.redhat.com/en/topics/containers/what-is-kubernetes) | Hiểu vai trò và thành phần Kubernetes | - |
| 2h | **Pod**: Pod lifecycle, multi-container Pods, init containers | [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/), [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) | Hiểu Pod lifecycle, cấu trúc Pod | Tạo Pod với `kubectl run nginx --image=nginx` |
| 2h | **API và Truy cập Kubernetes**: Sử dụng kubectl, cấu hình API, lệnh cơ bản (`kubectl get`, `describe`) | [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/), [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) | Cài đặt kubectl, Minikube; sử dụng lệnh kubectl | Cài Minikube ([Minikube Start](https://minikube.sigs.k8s.io/docs/start/)), tạo Pod với 2 container |
| 2h | **Thực hành**: Quản lý Pod cơ bản | [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/) | Tạo, xóa, kiểm tra Pod | 1. Tạo Pod chạy `nginx`.<br>2. Tạo Pod với main container (`httpd`) và sidecar (`busybox`).<br>3. Kiểm tra trạng thái với `kubectl describe pod`. |

**Ghi chú**: Cài đặt Minikube và kubectl trước buổi học.

## Ngày 2: Quản lý Workload (Deployment, ReplicaSet, Job, CronJob)
**Mục tiêu**: Hiểu các workload quản lý Pod và so sánh chúng.

| **Thời gian** | **Chủ đề/Bài học** | **Tài liệu tham khảo** | **Yêu cầu** | **Thực hành** |
|---------------|--------------------|-----------------------|-------------|---------------|
| 2h | **Deployment và ReplicaSet**: Deployment cho ứng dụng stateless, ReplicaSet quản lý bản sao, rolling updates | [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [Kubernetes ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) | Hiểu Deployment, ReplicaSet, scale/update | Tạo Deployment với 3 bản sao `nginx`, thực hiện rolling update |
| 2h | **Job**: Chạy tác vụ một lần, xử lý song song, quản lý lỗi (restartPolicy, completions) | [Kubernetes Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/), [Running Automated Tasks](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/) | Hiểu Job, cấu hình tác vụ | Tạo Job chạy lệnh `echo "Task completed"` |
| 2h | **CronJob**: Lên lịch tác vụ định kỳ, cấu hình lịch trình, quản lý lịch sử | [Kubernetes CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/), [CronJob Tutorial](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/) | Hiểu CronJob, cấu hình lịch trình | Tạo CronJob chạy mỗi 5 phút |
| 2h | **Thực hành**: Triển khai ứng dụng với các workload | [Kubernetes Tutorials - Workloads](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/) | So sánh Deployment, Job, CronJob | 1. Tạo Deployment `httpd` với 3 bản sao.<br>2. Tạo Job chạy lệnh kiểm tra DB.<br>3. Tạo CronJob chạy mỗi 5 phút để in log.<br>4. Scale Deployment lên 5 bản sao, kiểm tra Job completion. |

**Ghi chú**: Sử dụng image `busybox` cho Job/CronJob và `httpd` cho Deployment.

## Ngày 3: Mạng và Cấu hình (Service, ConfigMap, Secret, Volume)
**Mục tiêu**: Hiểu cách cấu hình mạng, lưu trữ và quản lý cấu hình.

| **Thời gian** | **Chủ đề/Bài học** | **Tài liệu tham khảo** | **Yêu cầu** | **Thực hành** |
|---------------|--------------------|-----------------------|-------------|---------------|
| 2h | **Service**: ClusterIP, NodePort, LoadBalancer, Headless Service; DNS trong Kubernetes | [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/), [Service Types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) | Hiểu các loại Service, cấu hình DNS | Tạo Service ClusterIP cho `nginx` |
| 2h | **ConfigMap và Secret**: Quản lý cấu hình, thông tin nhạy cảm | [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/), [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) | Sử dụng ConfigMap/Secret trong Pod | Tạo ConfigMap/Secret cho ứng dụng |
| 2h | **Volume và PersistentVolume**: Các loại Volume, PersistentVolumeClaim (PVC) | [Kubernetes Volumes](https://kubernetes.io/docs/concepts/storage/volumes/), [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) | Hiểu cách lưu trữ kiên trì, tạo PVC | Tạo PVC 1Gi, gắn vào Pod |
| 2h | **Thực hành**: Triển khai ứng dụng với Service, ConfigMap, Secret, Volume | [Kubernetes Tutorials - Services](https://kubernetes.io/docs/tutorials/services/) | Triển khai ứng dụng FE/BE/DB | 1. Tạo Deployment FE (`nginx`) và BE (`http-echo`).<br>2. Tạo Service NodePort cho FE/BE.<br>3. Tạo ConfigMap (DB_HOST), Secret (DB_PASSWORD).<br>4. Tạo Deployment DB (`postgres`) với PVC.<br>5. Kiểm tra kết nối với `kubectl port-forward`. |

**Ghi chú**: Sử dụng image `nginx`, `hashicorp/http-echo`, `postgres:13`.

## Ngày 4: Debugging Pod
**Mục tiêu**: Nắm vững kỹ năng gỡ lỗi Pod và xử lý sự cố.

| **Thời gian** | **Chủ đề/Bài học** | **Tài liệu tham khảo** | **Yêu cầu** | **Thực hành** |
|---------------|--------------------|-----------------------|-------------|---------------|
| 2h | **Debugging cơ bản**: Kiểm tra trạng thái Pod (`kubectl describe`, `kubectl get`), phân tích sự kiện | [Debugging Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/), [Troubleshooting Applications](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/) | Hiểu cách kiểm tra trạng thái Pod | Kiểm tra Pod lỗi với `kubectl describe` |
| 2h | **Debugging nâng cao**: Truy cập container (`kubectl exec`), kiểm tra log (`kubectl logs`), debug crashloop | [Debugging CrashLoopBackOff](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/) | Sử dụng `kubectl exec`, `logs` | Truy cập container, xem log |
| 2h | **Xử lý sự cố phổ biến**: Pod không khởi động, lỗi image, thiếu tài nguyên | [Troubleshooting Kubernetes](https://kubernetes.io/docs/tasks/debug-application-cluster/troubleshooting/) | Xử lý lỗi Pod cơ bản | Tạo Pod lỗi (image không tồn tại) và khắc phục |
| 2h | **Thực hành**: Debug ứng dụng | [Kubernetes Debugging Tutorials](https://kubernetes.io/docs/tasks/debug/) | Xử lý lỗi trong ứng dụng | 1. Tạo Pod với image sai (`nginx:invalid`), debug lỗi.<br>2. Tạo Pod thiếu tài nguyên, khắc phục.<br>3. Tạo Deployment crashloop, kiểm tra log với `kubectl logs`.<br>4. Sử dụng `kubectl exec` để kiểm tra container. |

**Ghi chú**: Tạo các Pod lỗi để thực hành gỡ lỗi.

## Ngày 5: Chuẩn bị Lab Cuối
**Mục tiêu**: Thực hành triển khai ứng dụng 3 thành phần và chuẩn bị lab cuối.

| **Thời gian** | **Chủ đề/Bài học** | **Tài liệu tham khảo** | **Yêu cầu** | **Thực hành** |
|---------------|--------------------|-----------------------|-------------|---------------|
| 4h | **Triển khai ứng dụng mẫu**: Thực hành triển khai FE, BE, DB với Deployment, Service, Volume, ConfigMap, Secret, Job | [Kubernetes Tutorials - Deploy App](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/) | Triển khai ứng dụng hoàn chỉnh | Triển khai FE (`nginx`), BE (`http-echo`), DB (`postgres`) với Service, PVC, ConfigMap, Secret, Job |
| 4h | **Chuẩn bị lab cuối**: Hướng dẫn triển khai ứng dụng 3 thành phần, workflow triển khai | [Kubernetes Tutorials - Stateful App](https://kubernetes.io/docs/tutorials/stateful-application/) | Chuẩn bị cho lab cuối | 1. Triển khai ứng dụng mẫu tương tự lab cuối.<br>2. Dùng Job để chèn dữ liệu giả vào DB.<br>3. Kiểm tra kết nối FE/BE/DB với `kubectl port-forward`. |

## Bài Lab Cuối Khóa
**Mô tả**: Triển khai ứng dụng 3 thành phần (Frontend, Backend, Database) trên Kubernetes, sử dụng Deployment, Service, ConfigMap, Secret, Volume và Job. Truy cập qua Service NodePort.

**Đầu vào**:
- Source code:
  - **Frontend**: Ứng dụng web (`nginx`).
  - **Backend**: API trả thông báo (`hashicorp/http-echo`).
  - **Database**: PostgreSQL với dữ liệu giả (`postgres:13`).
- Dữ liệu giả: Bảng `users` (cột `id` SERIAL, `name` VARCHAR).

**Đầu ra**:
- Ứng dụng triển khai hoàn chỉnh:
  - Deployment: FE (3 bản sao), BE (2 bản sao), DB (1 bản sao).
  - Service NodePort: Truy cập FE và BE.
  - PersistentVolumeClaim: Lưu trữ cho DB.
  - ConfigMap: Cấu hình DB (DB_HOST, DB_PORT).
  - Secret: Mật khẩu DB.
  - Job: Khởi tạo dữ liệu giả trong DB.
- Truy cập FE/BE qua NodePort, DB chứa dữ liệu giả.

**Yêu cầu**:
- Cụm Minikube.
- Cài đặt kubectl.
- Truy cập qua `kubectl port-forward` hoặc NodePort.

**Tài liệu tham khảo**:
- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Kubernetes Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
- [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Kubernetes Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)

**Workflow triển khai**:
1. **Chuẩn bị môi trường**:
   - Khởi động: `minikube start`.
   - Kiểm tra: `kubectl get nodes`.

2. **Tạo PersistentVolumeClaim**:
   - File `db-pvc.yaml`:
     ```yaml
     apiVersion: v1
     kind: PersistentVolumeClaim
     metadata:
       name: postgres-pvc
     spec:
       accessModes:
       - ReadWriteOnce
       resources:
         requests:
           storage: 1Gi
     ```
   - Áp dụng: `kubectl apply -f db-pvc.yaml`.

3. **Tạo ConfigMap**:
   - File `app-config.yaml`:
     ```yaml
     apiVersion: v1
     kind: ConfigMap
     metadata:
       name: app-config
     data:
       DB_HOST: postgres-service
       DB_PORT: "5432"
     ```
   - Áp dụng: `kubectl apply -f app-config.yaml`.

4. **Tạo Secret**:
   - File `db-secret.yaml`:
     ```yaml
     apiVersion: v1
     kind: Secret
     metadata:
       name: postgres-secret
     type: Opaque
     data:
       postgres-password: cGFzc3dvcmQ=  # base64 của "password"
     ```
   - Áp dụng: `kubectl apply -f db-secret.yaml`.

5. **Triển khai Database**:
   - File `postgres-deployment.yaml`:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: postgres
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: postgres
       template:
         metadata:
           labels:
             app: postgres
         spec:
           containers:
           - name: postgres
             image: postgres:13
             env:
             - name: POSTGRES_PASSWORD
               valueFrom:
                 secretKeyRef:
                   name: postgres-secret
                   key: postgres-password
             - name: POSTGRES_DB
               value: myapp
             ports:
             - containerPort: 5432
             volumeMounts:
             - name: data
               mountPath: /var/lib/postgresql/data
           volumes:
           - name: data
             persistentVolumeClaim:
               claimName: postgres-pvc
     ```
   - File `postgres-service.yaml`:
     ```yaml
     apiVersion: v1
     kind: Service
     metadata:
       name: postgres-service
     spec:
       selector:
         app: postgres
       ports:
       - port: 5432
         targetPort: 5432
       type: ClusterIP
     ```
   - Áp dụng: `kubectl apply -f postgres-deployment.yaml -f postgres-service.yaml`.

6. **Tạo Job khởi tạo dữ liệu**:
   - File `db-init-job.yaml`:
     ```yaml
     apiVersion: batch/v1
     kind: Job
     metadata:
       name: db-init
     spec:
       template:
         spec:
           containers:
           - name: db-init
             image: postgres:13
             command: ["psql", "-h", "postgres-service", "-U", "postgres", "-d", "myapp", "-c", "CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(50)); INSERT INTO users (name) VALUES ('User1'), ('User2');"]
             env:
             - name: PGPASSWORD
               valueFrom:
                 secretKeyRef:
                   name: postgres-secret
                   key: postgres-password
           restartPolicy: OnFailure
     ```
   - Áp dụng: `kubectl apply -f db-init-job.yaml`.

7. **Triển khai Backend**:
   - File `backend-deployment.yaml`:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: backend
     spec:
       replicas: 2
       selector:
         matchLabels:
           app: backend
       template:
         metadata:
           labels:
             app: backend
         spec:
           containers:
           - name: backend
             image: hashicorp/http-echo
             args: ["-text=Connected to DB"]
             env:
             - name: DB_HOST
               valueFrom:
                 configMapKeyRef:
                   name: app-config
                   key: DB_HOST
             - name: DB_PORT
               valueFrom:
                 configMapKeyRef:
                   name: app-config
                   key: DB_PORT
             - name: DB_PASSWORD
               valueFrom:
                 secretKeyRef:
                   name: postgres-secret
                   key: postgres-password
             ports:
             - containerPort: 5678
     ```
   - File `backend-service.yaml`:
     ```yaml
     apiVersion: v1
     kind: Service
     metadata:
       name: backend-service
     spec:
       selector:
         app: backend
       ports:
       - port: 80
         targetPort: 5678
         nodePort: 30001
       type: NodePort
     ```
   - Áp dụng: `kubectl apply -f backend-deployment.yaml -f backend-service.yaml`.

8. **Triển khai Frontend**:
   - File `frontend-deployment.yaml`:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: frontend
     spec:
       replicas: 3
       selector:
         matchLabels:
           app: frontend
       template:
         metadata:
           labels:
             app: frontend
         spec:
           containers:
           - name: frontend
             image: nginx
             ports:
             - containerPort: 80
     ```
   - File `frontend-service.yaml`:
     ```yaml
     apiVersion: v1
     kind: Service
     metadata:
       name: frontend-service
     spec:
       selector:
         app: frontend
       ports:
       - port: 80
         targetPort: 80
         nodePort: 30002
       type: NodePort
     ```
   - Áp dụng: `kubectl apply -f frontend-deployment.yaml -f frontend-service.yaml`.

9. **Kiểm tra ứng dụng**:
   - Kiểm tra trạng thái: `kubectl get pods,svc,pvc,jobs`.
   - Truy cập Frontend: `kubectl port-forward svc/frontend-service 8080:80`, mở `http://localhost:8080`.
   - Truy cập Backend: `kubectl port-forward svc/backend-service 8081:80`, mở `http://localhost:8081`.
   - Kiểm tra DB: `kubectl exec -it $(kubectl get pod -l app=postgres -o jsonpath="{.items[0].metadata.name}") -- psql -U postgres -d myapp -c "SELECT * FROM users;"`.

## Kiểm tra sau khóa học
### Kiểm tra lý thuyết
- **5 câu hỏi tự luận**:
  1. Sự khác biệt giữa Pod và Deployment là gì?
  2. Service NodePort hoạt động như thế nào so với ClusterIP?
  3. Tại sao cần sử dụng PersistentVolumeClaim cho DB?
  4. Job và CronJob được sử dụng khi nào, khác nhau ra sao?
  5. Làm thế nào để debug một Pod ở trạng thái CrashLoopBackOff?
- **25 câu hỏi trắc nghiệm**: Bao quát Pod, Deployment, ReplicaSet, Service, ConfigMap, Secret, Volume, Job, CronJob.

### Bài Lab Cuối
**Mô tả**: Như mô tả ở trên.

**Câu hỏi bổ sung**:
1. Sự khác biệt giữa Deployment và Job trong quản lý Pod?
2. Làm thế nào để cấu hình Service NodePort để truy cập Frontend và Backend?
3. Tại sao cần sử dụng PersistentVolumeClaim cho Database?
4. Cách sử dụng Job để khởi tạo dữ liệu giả trong DB?
5. Làm thế nào để kiểm tra trạng thái hoàn thành của một Job?
