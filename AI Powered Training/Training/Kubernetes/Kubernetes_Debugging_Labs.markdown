# Bài Tập Thực Hành Debugging Pod trong Kubernetes

**Mục tiêu**: Cung cấp các bài tập thực hành để người học rèn luyện kỹ năng phát hiện và khắc phục lỗi trong Kubernetes, tập trung vào các vấn đề phổ biến như lỗi image, cấu hình sai, thiếu tài nguyên, và lỗi kết nối mạng.

**Yêu cầu**:
- Cụm Kubernetes (Minikube được khuyến nghị).
- Cài đặt `kubectl`.
- Hiểu cơ bản về Pod, Deployment, Service, và các lệnh `kubectl` (`get`, `describe`, `logs`, `exec`).

---

## Bài Lab 1: Debug Pod Lỗi ImagePullBackOff
- **Mô tả**: Tạo một Pod với image không tồn tại, xác định nguyên nhân lỗi `ImagePullBackOff` và khắc phục.
- **Định hướng**: Làm quen với việc phân tích trạng thái Pod và sửa lỗi liên quan đến image container.
- **Các bước**:
  1. Tạo file `image-error-pod.yaml`:
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       name: image-error-pod
     spec:
       containers:
       - name: nginx
         image: nginx:nonexistent
     ```
  2. Áp dụng: `kubectl apply -f image-error-pod.yaml`.
  3. Kiểm tra trạng thái: `kubectl get pod image-error-pod`.
  4. Phân tích lỗi: `kubectl describe pod image-error-pod` (tìm dòng liên quan đến `ImagePullBackOff`).
  5. Xem log (nếu có): `kubectl logs image-error-pod` (có thể không có log do lỗi image).
  6. Khắc phục: Sửa image thành `nginx:latest` trong `image-error-pod.yaml` và áp dụng lại: `kubectl apply -f image-error-pod.yaml`.
  7. Kiểm tra lại: `kubectl get pod image-error-pod`.
- **Kết quả mong đợi**: Pod chuyển từ trạng thái `ImagePullBackOff` sang `Running` sau khi sửa image.

---

## Bài Lab 2: Debug Pod CrashLoopBackOff do Lệnh Sai
- **Mô tả**: Tạo một Pod với lệnh container sai, xác định nguyên nhân lỗi `CrashLoopBackOff` và khắc phục.
- **Định hướng**: Hiểu cách sử dụng log và sự kiện để xác định lỗi ứng dụng trong container.
- **Các bước**:
  1. Tạo file `crash-pod.yaml`:
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       name: crash-pod
     spec:
       containers:
       - name: busybox
         image: busybox
         command: ["invalid-command"]
     ```
  2. Áp dụng: `kubectl apply -f crash-pod.yaml`.
  3. Kiểm tra trạng thái: `kubectl get pod crash-pod` (xem trạng thái `CrashLoopBackOff`).
  4. Phân tích lỗi: `kubectl describe pod crash-pod` (tìm thông tin về lỗi lệnh).
  5. Xem log: `kubectl logs crash-pod` (xem thông báo lỗi liên quan đến lệnh không tồn tại).
  6. Khắc phục: Sửa command thành `["sh", "-c", "echo Running && sleep 3600"]` trong `crash-pod.yaml` và áp dụng lại.
  7. Kiểm tra lại: `kubectl get pod crash-pod`.
- **Kết quả mong đợi**: Pod chuyển từ trạng thái `CrashLoopBackOff` sang `Running` sau khi sửa lệnh.

---

## Bài Lab 3: Debug Pod Pending do Thiếu Tài Nguyên
- **Mô tả**: Tạo một Pod yêu cầu tài nguyên vượt quá khả năng của cụm, xác định nguyên nhân lỗi `Pending` và khắc phục.
- **Định hướng**: Hiểu cách kiểm tra sự kiện để phát hiện lỗi tài nguyên và điều chỉnh yêu cầu.
- **Các bước**:
  1. Tạo file `resource-error-pod.yaml`:
     ```yaml
     apiVersion: v1
     kind: Pod
     metadata:
       name: resource-error-pod
     spec:
       containers:
       - name: nginx
         image: nginx
         resources:
           requests:
             memory: "10Gi"
             cpu: "8"
     ```
  2. Áp dụng: `kubectl apply -f resource-error-pod.yaml`.
  3. Kiểm tra trạng thái: `kubectl get pod resource-error-pod` (xem trạng thái `Pending`).
  4. Phân tích lỗi: `kubectl describe pod resource-error-pod` (tìm thông báo về thiếu tài nguyên).
  5. Kiểm tra tài nguyên cụm: `kubectl describe nodes` (xem CPU và memory khả dụng).
  6. Khắc phục: Sửa yêu cầu tài nguyên thành `memory: "128Mi", cpu: "500m"` trong `resource-error-pod.yaml` và áp dụng lại.
  7. Kiểm tra lại: `kubectl get pod resource-error-pod`.
- **Kết quả mong đợi**: Pod chuyển từ trạng thái `Pending` sang `Running` sau khi giảm yêu cầu tài nguyên.

---

## Bài Lab 4: Debug Lỗi Kết Nối Service
- **Mô tả**: Tạo một Deployment và Service với selector sai, dẫn đến Pod không thể truy cập qua Service. Xác định và khắc phục lỗi.
- **Định hướng**: Hiểu cách kiểm tra cấu hình Service và đảm bảo selector khớp với nhãn Pod.
- **Các bước**:
  1. Tạo file `nginx-deployment.yaml`:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: nginx-deployment
     spec:
       replicas: 2
       selector:
         matchLabels:
           app: nginx
       template:
         metadata:
           labels:
             app: nginx
         spec:
           containers:
           - name: nginx
             image: nginx
             ports:
             - containerPort: 80
     ```
  2. Tạo file `nginx-service.yaml` với selector sai:
     ```yaml
     apiVersion: v1
     kind: Service
     metadata:
       name: nginx-service
     spec:
       selector:
         app: wrong-label
       ports:
       - port: 80
         targetPort: 80
       type: ClusterIP
     ```
  3. Áp dụng: `kubectl apply -f nginx-deployment.yaml -f nginx-service.yaml`.
  4. Kiểm tra Service: `kubectl get svc nginx-service` và `kubectl describe svc nginx-service` (xem mục Endpoints trống).
  5. Thử truy cập: `kubectl port-forward svc/nginx-service 8080:80` (sẽ không kết nối được).
  6. Kiểm tra nhãn Pod: `kubectl get pods -l app=nginx --show-labels`.
  7. Khắc phục: Sửa selector trong `nginx-service.yaml` thành `app: nginx` và áp dụng lại.
  8. Kiểm tra lại: `kubectl port-forward svc/nginx-service 8080:80`, mở `http://localhost:8080`.
- **Kết quả mong đợi**: Service hoạt động, truy cập được Pods qua `port-forward` sau khi sửa selector.

---

## Bài Lab 5: Debug Job Thất Bại do Lỗi Cấu Hình
- **Mô tả**: Tạo một Job với cấu hình sai (lệnh không hợp lệ), xác định nguyên nhân thất bại và khắc phục.
- **Định hướng**: Hiểu cách debug Job thông qua log và trạng thái hoàn thành.
- **Các bước**:
  1. Tạo file `failed-job.yaml`:
     ```yaml
     apiVersion: batch/v1
     kind: Job
     metadata:
       name: failed-job
     spec:
       template:
         spec:
           containers:
           - name: task
             image: busybox
             command: ["nonexistent-command"]
           restartPolicy: Never
     ```
  2. Áp dụng: `kubectl apply -f failed-job.yaml`.
  3. Kiểm tra trạng thái: `kubectl get job failed-job` và `kubectl get pod -l job-name=failed-job`.
  4. Phân tích lỗi: `kubectl describe job failed-job` và `kubectl describe pod <pod-name>` (tìm lỗi liên quan đến lệnh).
  5. Xem log: `kubectl logs <pod-name>` (xem thông báo lỗi lệnh).
  6. Khắc phục: Sửa command thành `["echo", "Job completed"]` trong `failed-job.yaml` và áp dụng lại (xóa Job cũ trước: `kubectl delete job failed-job`).
  7. Kiểm tra lại: `kubectl get job failed-job`, `kubectl logs <pod-name>`.
- **Kết quả mong đợi**: Job hoàn thành thành công, log hiển thị thông điệp "Job completed".

---

## Câu Hỏi Trắc Nghiệm (MCQ)
1. Trạng thái `ImagePullBackOff` chỉ ra lỗi gì?
   - A. Lệnh container sai
   - B. Image không tồn tại
   - C. Thiếu tài nguyên
   - D. Service không kết nối
   - **Đáp án**: B
2. Lệnh nào để kiểm tra sự kiện Pod?
   - A. `kubectl logs`
   - B. `kubectl describe pod`
   - C. `kubectl exec`
   - D. `kubectl get pod`
   - **Đáp án**: B
3. `CrashLoopBackOff` xảy ra khi nào?
   - A. Container liên tục bị crash
   - B. Image không tải được
   - C. Pod ở trạng thái Pending
   - D. Service không hoạt động
   - **Đáp án**: A
4. Lệnh nào để truy cập container và kiểm tra môi trường?
   - A. `kubectl logs`
   - B. `kubectl exec -it <pod> -- sh`
   - C. `kubectl describe pod`
   - D. `kubectl get pod`
   - **Đáp án**: B
5. Nếu Service không có Endpoints, vấn đề có thể là gì?
   - A. Image sai
   - B. Selector không khớp
   - C. Thiếu tài nguyên
   - D. Lệnh container sai
   - **Đáp án**: B
6. Trạng thái `Pending` thường liên quan đến vấn đề gì?
   - A. Lệnh sai
   - B. Thiếu tài nguyên
   - C. Service lỗi
   - D. Image không tồn tại
   - **Đáp án**: B
7. Lệnh nào để xem log của Job?
   - A. `kubectl logs job`
   - B. `kubectl logs <pod-name>`
   - C. `kubectl describe job`
   - D. `kubectl exec job`
   - **Đáp án**: B
8. Lệnh nào để kiểm tra tài nguyên cụm?
   - A. `kubectl get nodes`
   - B. `kubectl describe nodes`
   - C. `kubectl logs nodes`
   - D. `kubectl exec nodes`
   - **Đáp án**: B
9. Tại sao cần kiểm tra log khi debug?
   - A. Xem cấu hình Pod
   - B. Xác định nguyên nhân lỗi
   - C. Cập nhật image
   - D. Tăng tài nguyên
   - **Đáp án**: B
10. Nếu Job không hoàn thành, bước đầu tiên nên làm gì?
    - A. Xóa Job
    - B. Kiểm tra log của Pod
    - C. Tăng tài nguyên
    - D. Sửa Service
    - **Đáp án**: B

---

## Câu Hỏi Vấn Đáp
1. Các bước cơ bản để debug một Pod ở trạng thái `CrashLoopBackOff` là gì?
2. Làm thế nào để xác định một Service không kết nối được với Pod?
3. Tại sao Pod có thể rơi vào trạng thái `Pending` và cách khắc phục?
4. Lệnh `kubectl describe` cung cấp thông tin gì khi debug?
5. Cách xử lý lỗi `ImagePullBackOff` trong Kubernetes?

---

**Ghi chú**:
- Sử dụng Minikube để tạo môi trường thực hành.
- Image sử dụng: `nginx`, `busybox`.
- Đảm bảo xóa tài nguyên sau mỗi bài lab để tránh xung đột: `kubectl delete -f <file>.yaml`.