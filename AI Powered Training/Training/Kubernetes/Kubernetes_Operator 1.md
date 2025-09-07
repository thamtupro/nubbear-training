# Lịch trình đào tạo Kubernetes Operator (5 ngày)

Lịch trình này được thiết kế để giúp bạn đi sâu vào Kubernetes Operator, từ khái niệm cơ bản đến xây dựng và triển khai Operator trong môi trường thực tế. Mỗi ngày bao gồm các bài học lý thuyết, thực hành, câu hỏi trắc nghiệm (MCQ), và câu hỏi vấn đáp để củng cố kiến thức. Cuối khóa, bạn sẽ thực hiện một bài lab cuối để áp dụng kiến thức vào một dự án thực tế.

- **Thời lượng**: 5 ngày, mỗi ngày 8 giờ (tổng 40 giờ).
- **Mục tiêu**: Hiểu và xây dựng Kubernetes Operator để tự động hóa quản lý ứng dụng phức tạp, tập trung vào vận hành, quản trị, và giám sát.
- **Yêu cầu**: Kiến thức cơ bản về Kubernetes (Pods, Deployments, Services, ConfigMaps, Secrets, Volumes, Jobs, CronJobs) và kỹ năng sử dụng `kubectl`.
- **Kết quả mong đợi**: Xây dựng được một Operator tùy chỉnh, triển khai ứng dụng phức tạp, và áp dụng best practices trong quản lý Operator.

## Ngày 1: Giới thiệu về Kubernetes Operator

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Tổng quan về Operator** | Operator là gì, vai trò trong quản lý ứng dụng, so sánh với Deployment và StatefulSet. | 2 giờ | - [Kubernetes Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)<br>- [What is a Kubernetes Operator?](https://www.groundcover.com/blog/kubernetes-operator) | **Lab 1.1**: Cài đặt môi trường Operator SDK.<br>1. Cài đặt Operator SDK: `brew install operator-sdk` (hoặc tương tự trên Linux/Windows).<br>2. Kiểm tra phiên bản: `operator-sdk version`.<br>3. Khởi tạo cụm Minikube: `minikube start`. |
| **Custom Resource Definitions (CRDs)** | CRDs là gì, cách định nghĩa và sử dụng để mở rộng Kubernetes API. | 2 giờ | - [Kubernetes CRDs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)<br>- [CRD Example](https://iximiuz.com/en/posts/kubernetes-operator-pattern/) | **Lab 1.2**: Tạo CRD đơn giản.<br>1. Tạo CRD cho một tài nguyên `App` với `operator-sdk init --domain example.com --repo github.com/example/app-operator`.<br>2. Định nghĩa CRD: `operator-sdk create api --group app --version v1 --kind App --resource --controller`.<br>3. Áp dụng CRD: `kubectl apply -f config/crd/bases/app.example.com_apps.yaml`. |
| **Custom Controllers** | Vai trò của Controller trong Operator, cách hoạt động của control loop. | 2 giờ | - [Kubernetes Controllers](https://kubernetes.io/docs/concepts/architecture/controller/)<br>- [Operator SDK Controller](https://sdk.operatorframework.io/docs/building-operators/golang/) | **Lab 1.3**: Tạo Controller cơ bản.<br>1. Tạo Controller cho CRD `App` sử dụng Operator SDK.<br>2. Cập nhật logic trong `controllers/app_controller.go` để in thông báo khi CR được tạo.<br>3. Build và chạy Operator: `make install run`. |
| **Thực hành tổng hợp** | Kết hợp CRD và Controller để quản lý một ứng dụng đơn giản. | 2 giờ | - [Operator SDK Quickstart](https://sdk.operatorframework.io/docs/building-operators/golang/quickstart/) | **Lab 1.4**: Triển khai Operator đơn giản.<br>1. Tạo file `app-sample.yaml` để định nghĩa một instance của `App`.<br>2. Áp dụng: `kubectl apply -f config/samples/app_v1_app.yaml`.<br>3. Kiểm tra trạng thái: `kubectl get apps` và `kubectl describe app app-sample`. |

**Câu hỏi trắc nghiệm (MCQ)**:
1. Kubernetes Operator là gì?
   - A. Công cụ quản lý container
   - B. Mở rộng Kubernetes API để quản lý ứng dụng
   - C. Công cụ giám sát log
   - D. Công cụ CI/CD
   - **Đáp án**: B
2. CRD được sử dụng để làm gì?
   - A. Tạo Pod
   - B. Định nghĩa tài nguyên tùy chỉnh
   - C. Quản lý Service
   - D. Debug Pod
   - **Đáp án**: B
3. Controller trong Operator có vai trò gì?
   - A. Tạo Service
   - B. Đảm bảo trạng thái thực tế khớp với trạng thái mong muốn
   - C. Lưu trữ dữ liệu
   - D. Giám sát metric
   - **Đáp án**: B
4. Công cụ nào thường được dùng để xây dựng Operator?
   - A. Helm
   - B. Operator SDK
   - C. Prometheus
   - D. Fluentd
   - **Đáp án**: B
5. Lệnh nào để kiểm tra CRD trong cụm?
   - A. `kubectl get crd`
   - B. `kubectl get pod`
   - C. `kubectl describe svc`
   - D. `kubectl logs crd`
   - **Đáp án**: A
6. Operator thường được sử dụng cho ứng dụng nào?
   - A. Ứng dụng stateless đơn giản
   - B. Ứng dụng có trạng thái phức tạp
   - C. Ứng dụng không cần quản lý
   - D. Ứng dụng web tĩnh
   - **Đáp án**: B
7. Control loop trong Operator hoạt động như thế nào?
   - A. Tạo Pod liên tục
   - B. So sánh trạng thái thực tế và mong muốn
   - C. Xóa tài nguyên
   - D. Giám sát log
   - **Đáp án**: B
8. Lệnh nào để chạy Operator trong môi trường phát triển?
   - A. `make install run`
   - B. `kubectl apply`
   - C. `kubectl run`
   - D. `helm install`
   - **Đáp án**: A
9. CRD được định nghĩa trong file nào?
   - A. YAML
   - B. JSON
   - C. Python
   - D. Go
   - **Đáp án**: A
10. Operator SDK hỗ trợ ngôn ngữ nào để viết Operator?
    - A. Golang, Ansible, Helm
    - B. Python, Java, Ruby
    - C. C++, PHP, Perl
    - D. Bash, PowerShell, SQL
    - **Đáp án**: A

**Câu hỏi vấn đáp**:
1. Kubernetes Operator khác gì so với Deployment hoặc StatefulSet?
2. Tại sao cần sử dụng CRD trong Operator?
3. Control loop trong Operator hoạt động như thế nào?
4. Làm thế nào để kiểm tra một CRD đã được áp dụng đúng trong cụm?
5. Khi nào nên sử dụng Operator thay vì các công cụ khác như Helm?

**Ghi chú**: Cài đặt Operator SDK, Go, và Minikube trước buổi học. Sử dụng image `nginx` cho các ví dụ đơn giản.

## Ngày 2: Xây dựng Operator với Operator SDK

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Operator SDK Overview** | Tổng quan về Operator SDK, các thành phần (Golang, Ansible, Helm). | 2 giờ | - [Operator SDK Overview](https://sdk.operatorframework.io/docs/overview/)<br>- [Golang Operator Tutorial](https://sdk.operatorframework.io/docs/building-operators/golang/) | **Lab 2.1**: Khởi tạo dự án Operator.<br>1. Tạo dự án: `operator-sdk init --domain example.com --repo github.com/example/my-operator`.<br>2. Tạo API: `operator-sdk create api --group app --version v1 --kind MyApp`.<br>3. Kiểm tra cấu trúc dự án: `tree .`. |
| **Viết Controller Logic** | Viết logic Controller để quản lý tài nguyên tùy chỉnh (CRUD operations). | 2 giờ | - [Controller Implementation](https://sdk.operatorframework.io/docs/building-operators/golang/reconciliation-loop/) | **Lab 2.2**: Viết Controller để quản lý Deployment.<br>1. Cập nhật `controllers/myapp_controller.go` để tạo một Deployment khi CR `MyApp` được tạo.<br>2. Build: `make generate && make manifests`.<br>3. Triển khai: `make install run`. |
| **Testing Operator** | Kiểm tra Operator bằng unit test và integration test. | 2 giờ | - [Operator SDK Testing](https://sdk.operatorframework.io/docs/building-operators/golang/testing/) | **Lab 2.3**: Viết unit test cho Controller.<br>1. Tạo file test trong `controllers/myapp_controller_test.go`.<br>2. Viết test để kiểm tra tạo Deployment.<br>3. Chạy test: `make test`. |
| **Thực hành tổng hợp** | Triển khai Operator để quản lý một ứng dụng web đơn giản. | 2 giờ | - [Operator SDK Quickstart](https://sdk.operatorframework.io/docs/building-operators/golang/quickstart/) | **Lab 2.4**: Triển khai Operator quản lý `nginx`.<br>1. Tạo CR `MyApp` để triển khai `nginx` với 3 bản sao.<br>2. Áp dụng: `kubectl apply -f config/samples/app_v1_myapp.yaml`.<br>3. Kiểm tra: `kubectl get deployments` và `kubectl get myapps`. |

**Câu hỏi trắc nghiệm (MCQ)**:
1. Operator SDK hỗ trợ loại Operator nào?
   - A. Golang, Ansible, Helm
   - B. Python, Java, Ruby
   - C. C++, PHP, Perl
   - D. Bash, PowerShell, SQL
   - **Đáp án**: A
2. Lệnh nào để khởi tạo dự án Operator?
   - A. `operator-sdk init`
   - B. `kubectl create operator`
   - C. `make operator`
   - D. `helm init`
   - **Đáp án**: A
3. Controller trong Operator SDK được viết bằng gì?
   - A. YAML
   - B. Go
   - C. JSON
   - D. Python
   - **Đáp án**: B
4. Lệnh nào để tạo API mới cho Operator?
   - A. `operator-sdk create api`
   - B. `kubectl create api`
   - C. `make api`
   - D. `helm create api`
   - **Đáp án**: A
5. Unit test trong Operator SDK được chạy bằng lệnh nào?
   - A. `make test`
   - B. `kubectl test`
   - C. `operator-sdk test`
   - D. `helm test`
   - **Đáp án**: A
6. Mục đích của `make generate` trong Operator SDK là gì?
   - A. Tạo CRD
   - B. Tạo mã boilerplate
   - C. Triển khai Operator
   - D. Xóa tài nguyên
   - **Đáp án**: B
7. File nào chứa logic Controller?
   - A. `main.go`
   - B. `myapp_controller.go`
   - C. `crd.yaml`
   - D. `sample.yaml`
   - **Đáp án**: B
8. Lệnh nào để triển khai Operator trong môi trường phát triển?
   - A. `make install run`
   - B. `kubectl apply`
   - C. `helm install`
   - D. `operator-sdk deploy`
   - **Đáp án**: A
9. CR `MyApp` được định nghĩa trong file nào?
   - A. `config/samples/app_v1_myapp.yaml`
   - B. `controllers/myapp_controller.go`
   - C. `config/crd/bases/app.example.com_apps.yaml`
   - D. `main.go`
   - **Đáp án**: A
10. Mục đích của integration test trong Operator là gì?
    - A. Kiểm tra logic Controller trong cụm thực tế
    - B. Tạo CRD
    - C. Triển khai Pod
    - D. Giám sát log
    - **Đáp án**: A

**Câu hỏi vấn đáp**:
1. Operator SDK khác gì so với Kubebuilder?
2. Làm thế nào để viết logic Controller để quản lý một Deployment?
3. Tại sao cần viết unit test cho Operator?
4. Các bước để triển khai một Operator sử dụng Operator SDK là gì?
5. Làm thế nào để kiểm tra một Operator có hoạt động đúng không?

**Ghi chú**: Đảm bảo cài đặt Go, Operator SDK, và Minikube. Sử dụng image `nginx` cho các bài lab.

## Ngày 3: Quản lý ứng dụng phức tạp với Operator

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Quản lý Stateful Applications** | Sử dụng Operator để quản lý ứng dụng có trạng thái (như cơ sở dữ liệu). | 2 giờ | - [StatefulSet with Operators](https://www.cncf.io/blog/2022/06/15/kubernetes-operators-what-are-they-some-examples/)<br>- [MySQL Operator](https://github.com/mysql/mysql-operator) | **Lab 3.1**: Triển khai MySQL Operator.<br>1. Cài đặt MySQL Operator: `kubectl apply -f https://raw.githubusercontent.com/mysql/mysql-operator/main/deploy/deploy-crds.yaml`.<br>2. Tạo instance MySQL: `kubectl apply -f config/samples/mysql_v1alpha1_cluster.yaml`.<br>3. Kiểm tra: `kubectl get mysqlclusters`. |
| **Scaling và Upgrades** | Tự động hóa mở rộng quy mô và nâng cấp ứng dụng với Operator. | 2 giờ | - [Operator Scaling](https://konghq.com/blog/learning-center/what-is-a-kubernetes-operator) | **Lab 3.2**: Tùy chỉnh Operator để scale Deployment.<br>1. Cập nhật Controller để scale Deployment dựa trên trường `spec.replicas` trong CR.<br>2. Áp dụng CR với `replicas: 5`.<br>3. Kiểm tra: `kubectl get deployments`. |
| **Backup và Restore** | Tích hợp backup/restore vào Operator. | 2 giờ | - [Operator Backup](https://komodor.com/learn/kubernetes-operator/) | **Lab 3.3**: Thêm logic backup cho Operator.<br>1. Cập nhật Controller để tạo Job backup khi CR có trường `spec.backup=true`.<br>2. Tạo Job chạy `mysqldump` cho MySQL.<br>3. Kiểm tra: `kubectl get jobs`. |
| **Thực hành tổng hợp** | Tích hợp scaling và backup vào Operator. | 2 giờ | - [Operator Best Practices](https://spacelift.io/blog/kubernetes-operator) | **Lab 3.4**: Tạo Operator quản lý toàn diện.<br>1. Tạo CR với các trường `replicas` và `backup`.<br>2. Áp dụng: `kubectl apply -f config/samples/app_v1_myapp.yaml`.<br>3. Kiểm tra scaling và backup: `kubectl get deployments,jobs`. |

**Câu hỏi trắc nghiệm (MCQ)**:
1. Operator thường được dùng để quản lý ứng dụng nào?
   - A. Stateless
   - B. Stateful
   - C. Tĩnh
   - D. Không cần quản lý
   - **Đáp án**: B
2. MySQL Operator quản lý tài nguyên nào?
   - A. Deployment
   - B. MySQLCluster
   - C. Service
   - D. ConfigMap
   - **Đáp án**: B
3. Làm thế nào để scale ứng dụng với Operator?
   - A. Sử dụng Service
   - B. Cập nhật trường trong CR
   - C. Tạo Pod mới
   - D. Sử dụng ConfigMap
   - **Đáp án**: B
4. Backup trong Operator thường được thực hiện bằng gì?
   - A. Deployment
   - B. Job
   - C. CronJob
   - D. Service
   - **Đáp án**: B
5. Lệnh nào để kiểm tra instance MySQL do Operator tạo?
   - A. `kubectl get mysqlclusters`
   - B. `kubectl get pods`
   - C. `kubectl get svc`
   - D. `kubectl get deployments`
   - **Đáp án**: A
6. Trường nào trong CR thường dùng để scale?
   - A. `spec.replicas`
   - B. `spec.backup`
   - C. `spec.image`
   - D. `spec.port`
   - **Đáp án**: A
7. Làm thế nào để thêm logic backup vào Operator?
   - A. Tạo Service
   - B. Cập nhật Controller
   - C. Tạo ConfigMap
   - D. Tạo Secret
   - **Đáp án**: B
8. Lệnh nào để kiểm tra Job backup?
   - A. `kubectl get jobs`
   - B. `kubectl get pods`
   - C. `kubectl get svc`
   - D. `kubectl get deployments`
   - **Đáp án**: A
9. Operator có thể tự động hóa gì?
   - A. Tạo Pod
   - B. Backup và restore
   - C. Debug Pod
   - D. Tạo Service
   - **Đáp án**: B
10. Tại sao Operator phù hợp với ứng dụng stateful?
    - A. Vì chúng đơn giản
    - B. Vì chúng cần quản lý trạng thái
    - C. Vì chúng không cần lưu trữ
    - D. Vì chúng không cần Controller
    - **Đáp án**: B

**Câu hỏi vấn đáp**:
1. Tại sao Operator phù hợp hơn cho ứng dụng stateful so với Deployment?
2. Làm thế nào để tích hợp scaling vào Operator?
3. Các bước để thêm logic backup vào Operator là gì?
4. Làm thế nào để kiểm tra một Operator quản lý ứng dụng stateful có hoạt động đúng không?
5. Sự khác biệt giữa Operator và Helm trong quản lý ứng dụng là gì?

**Ghi chú**: Sử dụng image `mysql` và `nginx` cho các bài lab.

## Ngày 4: Giám sát và Debugging Operator

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Giám sát Operator** | Tích hợp Prometheus để giám sát Operator và ứng dụng. | 2 giờ | - [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) | **Lab 4.1**: Triển khai Prometheus Operator.<br>1. Cài đặt Prometheus Operator: `kubectl apply -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/main/bundle.yaml`.<br>2. Tạo ServiceMonitor cho Operator: `kubectl apply -f config/monitoring/servicemonitor.yaml`.<br>3. Kiểm tra metric: `kubectl port-forward svc/prometheus 9090:9090`. |
| **Debugging Operator** | Kiểm tra log, sự kiện, và xử lý lỗi trong Operator. | 2 giờ | - [Operator Debugging](https://sdk.operatorframework.io/docs/building-operators/golang/troubleshooting/) | **Lab 4.2**: Debug Operator lỗi.<br>1. Tạo CR với cấu hình sai (ví dụ: `spec.replicas=-1`).<br>2. Kiểm tra log: `kubectl logs <operator-pod>`.<br>3. Khắc phục: Sửa CR và áp dụng lại. |
| **Best Practices** | Thiết kế Operator hiệu quả, tối ưu hóa hiệu suất và bảo mật. | 2 giờ | - [Operator Best Practices](https://spacelift.io/blog/kubernetes-operator) | **Lab 4.3**: Áp dụng best practices.<br>1. Thêm validation cho CR (ví dụ: giới hạn `replicas` từ 1-10).<br>2. Cập nhật Controller để xử lý lỗi gracefully.<br>3. Kiểm tra: `kubectl apply -f config/samples/app_v1_myapp.yaml`. |
| **Thực hành tổng hợp** | Tích hợp giám sát và debugging vào Operator. | 2 giờ | - [Operator Monitoring](https://konghq.com/blog/learning-center/what-is-a-kubernetes-operator) | **Lab 4.4**: Giám sát và debug Operator.<br>1. Tạo CR với lỗi cố ý (ví dụ: image sai).<br>2. Kiểm tra metric và log qua Prometheus.<br>3. Khắc phục và kiểm tra lại. |

**Câu hỏi trắc nghiệm (MCQ)**:
1. Prometheus Operator được dùng để làm gì?
   - A. Tạo Pod
   - B. Giám sát metric
   - C. Tạo Service
   - D. Debug Pod
   - **Đáp án**: B
2. Lệnh nào để kiểm tra log của Operator?
   - A. `kubectl get operator`
   - B. `kubectl logs <operator-pod>`
   - C. `kubectl describe operator`
   - D. `kubectl exec operator`
   - **Đáp án**: B
3. ServiceMonitor trong Prometheus Operator có vai trò gì?
   - A. Tạo CRD
   - B. Thu thập metric từ Service
   - C. Tạo Deployment
   - D. Debug Operator
   - **Đáp án**: B
4. Làm thế nào để debug Operator khi CR sai?
   - A. Kiểm tra log và sự kiện
   - B. Tạo Service mới
   - C. Xóa CRD
   - D. Tăng tài nguyên
   - **Đáp án**: A
5. Best practice nào quan trọng khi thiết kế Operator?
   - A. Hardcode cấu hình
   - B. Thêm validation cho CR
   - C. Tạo nhiều Pod
   - D. Sử dụng ConfigMap
   - **Đáp án**: B
6. Lệnh nào để truy cập Prometheus UI?
   - A. `kubectl port-forward svc/prometheus`
   - B. `kubectl get prometheus`
   - C. `kubectl describe prometheus`
   - D. `kubectl exec prometheus`
   - **Đáp án**: A
7. Lỗi CR sai thường gây ra trạng thái gì?
   - A. Running
   - B. Failed
   - C. Pending
   - D. CrashLoopBackOff
   - **Đáp án**: B
8. Làm thế nào để tối ưu hóa hiệu suất Operator?
   - A. Tăng tài nguyên Pod
   - B. Xử lý lỗi gracefully
   - C. Tạo nhiều CRD
   - D. Sử dụng Service
   - **Đáp án**: B
9. Validation trong CR được thêm vào đâu?
   - A. Controller
   - B. CRD
   - C. Service
   - D. ConfigMap
   - **Đáp án**: B
10. Lệnh nào để kiểm tra sự kiện của Operator?
    - A. `kubectl get events`
    - B. `kubectl logs events`
    - C. `kubectl describe events`
    - D. `kubectl exec events`
    - **Đáp án**: A

**Câu hỏi vấn đáp**:
1. Làm thế nào để tích hợp Prometheus vào Operator?
2. Các bước debug một Operator khi CR không hoạt động đúng?
3. Tại sao cần thêm validation cho CR trong Operator?
4. Best practices nào quan trọng khi thiết kế Operator?
5. Làm thế nào để kiểm tra metric của Operator qua Prometheus?

**Ghi chú**: Cài đặt Prometheus Operator và đảm bảo Operator SDK hoạt động.

## Ngày 5: Triển khai Operator trong môi trường thực tế

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|----------------