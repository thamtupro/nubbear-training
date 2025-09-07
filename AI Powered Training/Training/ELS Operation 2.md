## Ngày 1: Giới Thiệu về Elasticsearch trên Docker

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Giới thiệu Elasticsearch trên Docker** | Tổng quan về Elasticsearch, vai trò trong tìm kiếm và phân tích dữ liệu, lợi ích khi chạy trên Docker. So sánh với triển khai truyền thống. | 1.5 giờ | - [What is Elasticsearch?](https://www.elastic.co/what-is/elasticsearch)<br>- [Running Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html) | **Lab 1.1**: Cài đặt và chạy Elasticsearch trên Docker.<br>1. Kéo image Elasticsearch: `docker pull docker.elastic.co/elasticsearch/elasticsearch:8.8.2`.<br>2. Chạy container: `docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.8.2`.<br>3. Kiểm tra trạng thái qua `curl http://localhost:9200` và xác minh giao diện hoạt động. |
| **Cấu hình cơ bản trên Docker** | Cấu hình Elasticsearch trong Docker, sử dụng Docker Compose cho cụm nhiều node, tối ưu hóa Dockerfile cho môi trường sản xuất. | 1.5 giờ | - [Elasticsearch Dockerfile Optimization](https://opster.com/guides/elasticsearch/operations/elasticsearch-dockerfile/)<br>- [Docker Compose for Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose) | **Lab 1.2**: Sử dụng Docker Compose cho cụm Elasticsearch.<br>1. Tạo file `docker-compose.yml` với cấu hình multi-node từ tài liệu tham khảo.<br>2. Chạy cụm: `docker-compose up -d`.<br>3. Kiểm tra trạng thái cụm qua `curl http://localhost:9200/_cat/nodes`.<br>4. Tối ưu hóa Dockerfile: thêm cấu hình heap size trong `ES_JAVA_OPTS`. |
| **Quản lý và giám sát cơ bản** | Giám sát tài nguyên (CPU, bộ nhớ) của container Elasticsearch, sử dụng Metricbeat để thu thập metrics, tạo dashboard trên Kibana. | 2 giờ | - [Monitoring Docker with Elasticsearch, Kibana, and Metricbeat](https://www.velotio.com/engineering-blog/monitoring-docker-container-with-elasticsearch-kibana-metricbeat)<br>- [Elasticsearch Monitoring Metrics](https://www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics/) | **Lab 1.3**: Thiết lập giám sát với Metricbeat.<br>1. Cài đặt Metricbeat: `docker pull docker.elastic.co/beats/metricbeat:8.8.2`.<br>2. Cấu hình Metricbeat để thu thập metrics Docker: chỉnh sửa file config và chạy container.<br>3. Kiểm tra metrics trong Elasticsearch qua `curl http://localhost:9200/_cat/indices?v`.<br>4. Tạo dashboard cơ bản trên Kibana tại `http://localhost:5601`. |
| **Sao lưu và khôi phục** | Sử dụng snapshot để sao lưu dữ liệu, cấu hình repository trên Docker, thực hành khôi phục dữ liệu. | 1 giờ | - [Elasticsearch Snapshot and Restore](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html) | **Lab 1.4**: Sao lưu và khôi phục dữ liệu.<br>1. Cấu hình snapshot repository: tạo volume Docker và chạy lệnh `PUT _snapshot/my_backup`.<br>2. Thực hiện snapshot: `POST _snapshot/my_backup/snapshot_1`.<br>3. Kiểm tra trạng thái snapshot qua `GET _snapshot/my_backup/snapshot_1`.<br>4. Khôi phục dữ liệu: `POST _snapshot/my_backup/snapshot_1/_restore`. |

**Tổng thời gian**: 6 giờ  
**Ghi chú**: Các bài tập sử dụng Elasticsearch ở chế độ dev trên Docker. Người học cần cài đặt Docker và có quyền truy cập CLI/UI.

---

## Ngày 2: Quản lý và Mở rộng Elasticsearch trên Docker

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Mở rộng cụm Elasticsearch trên Docker** | Hiểu cách mở rộng cụm, cấu hình discovery.type, quản lý node roles (master, data, client). | 1.5 giờ | - [Elasticsearch Cluster Scaling](https://www.elastic.co/guide/en/elasticsearch/reference/current/scalability.html)<br>- [Node Roles](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html) | **Lab 2.1**: Mở rộng cụm với Docker Compose.<br>1. Cập nhật `docker-compose.yml` để thêm node data và node master.<br>2. Chạy lại cụm: `docker-compose up -d`.<br>3. Kiểm tra phân bổ node qua `curl http://localhost:9200/_cat/nodes`.<br>4. Thay đổi discovery.type và kiểm tra lại. |
| **Tối ưu hóa hiệu suất trên Docker** | Tối ưu hóa JVM heap, quản lý tài nguyên container (CPU, memory limits), sử dụng cgroups. | 1.5 giờ | - [JVM Tuning](https://www.elastic.co/guide/en/elasticsearch/reference/current/tune-for-indexing-speed.html)<br>- [Docker Resource Management](https://docs.docker.com/config/containers/resource_constraints/) | **Lab 2.2**: Tối ưu hóa tài nguyên container.<br>1. Cấu hình heap size trong Docker: thêm `-e ES_JAVA_OPTS="-Xms512m -Xmx512m"`.<br>2. Đặt giới hạn CPU và memory: `docker run --memory="2g" --cpu="1"`.<br>3. Kiểm tra hiệu suất qua Metricbeat và dashboard Kibana. |
| **Giám sát nâng cao với Elastic Stack** | Sử dụng Elastic Agent, cấu hình logs forwarding, tạo alert trên Kibana cho các metrics quan trọng. | 2 giờ | - [Elastic Agent for Monitoring](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)<br>- [Kibana Alerts](https://www.elastic.co/guide/en/kibana/current/alerting-getting-started.html) | **Lab 2.3**: Thiết lập alert trên Kibana.<br>1. Cài đặt Elastic Agent: `docker pull docker.elastic.co/beats/elastic-agent:8.8.2`.<br>2. Cấu hình để thu thập logs và metrics, gửi đến Elasticsearch.<br>3. Tạo alert cho JVM heap >85% trên Kibana.<br>4. Kiểm tra alert qua email hoặc Slack (cấu hình nếu cần). |
| **Quản lý log và debugging** | Thu thập log từ container, sử dụng Filebeat, phân tích log trên Kibana, xử lý lỗi phổ biến. | 1 giờ | - [Filebeat for Docker Logs](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-docker.html) | **Lab 2.4**: Thu thập và phân tích log.<br>1. Cài đặt Filebeat: `docker pull docker.elastic.co/beats/filebeat:8.8.2`.<br>2. Cấu hình Filebeat để thu thập log từ container Elasticsearch.<br>3. Phân tích log trên Kibana, tìm lỗi như "No memory stats data available". |

**Tổng thời gian**: 6 giờ  
**Ghi chú**: Đảm bảo Docker Compose và Elastic Stack đã được cài đặt từ ngày 1. Người học cần quyền truy cập CLI/UI và internet.

---

## Ngày 3: Elasticsearch trên Kubernetes - Cơ bản

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Giới thiệu Elasticsearch trên Kubernetes** | Tổng quan về ECK (Elastic Cloud on Kubernetes), lợi ích của orchestration, so sánh với Docker. | 1.5 giờ | - [Elastic Cloud on Kubernetes](https://www.elastic.co/elastic-cloud-kubernetes)<br>- [ECK Documentation](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s) | **Lab 3.1**: Cài đặt ECK trên Kubernetes.<br>1. Cài đặt Helm: `helm install elastic-operator oci://docker.io/elastic/eck-operator`.<br>2. Kiểm tra trạng thái operator qua `kubectl get pods -n elastic-system`.<br>3. Xác minh ECK hoạt động qua UI hoặc CLI. |
| **Triển khai cụm Elasticsearch với ECK** | Sử dụng YAML để định nghĩa cụm, cấu hình node roles, storage class. | 1.5 giờ | - [Deploy Elasticsearch with ECK](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s/deploy-elasticsearch)<br>- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/) | **Lab 3.2**: Triển khai cụm Elasticsearch.<br>1. Tạo file `elasticsearch.yaml` với 3 node (1 master, 2 data).<br>2. Áp dụng: `kubectl apply -f elasticsearch.yaml`.<br>3. Kiểm tra trạng thái cụm qua `kubectl get elasticsearch`.<br>4. Truy cập qua `curl http://<service-name>:9200`. |
| **Giám sát trên Kubernetes với ECK** | Cấu hình stack monitoring, sử dụng Kibana để visualize metrics, thiết lập logs forwarding. | 2 giờ | - [Monitoring with ECK](https://www.elastic.co/docs/deploy-manage/monitor)<br>- [Kibana Dashboards](https://www.elastic.co/guide/en/kibana/current/dashboard.html) | **Lab 3.3**: Thiết lập giám sát với ECK.<br>1. Cấu hình monitoring trong YAML: thêm `monitoring` section.<br>2. Triển khai Kibana qua ECK: `kubectl apply -f kibana.yaml`.<br>3. Truy cập Kibana tại `http://<kibana-service>:5601`, tạo dashboard cho cluster health.<br>4. Kiểm tra logs forwarding qua Elastic Agent. |
| **Quản lý tài nguyên và scaling** | Sử dụng Horizontal Pod Autoscaler, cấu hình resource limits, mở rộng cụm thủ công. | 1 giờ | - [Autoscaling with ECK](https://www.elastic.co/docs/deploy-manage/autoscaling)<br>- [Kubernetes Resource Limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) | **Lab 3.4**: Scaling cụm Elasticsearch.<br>1. Cấu hình HPA: `kubectl autoscale deployment elasticsearch-master --min=1 --max=3 --cpu-percent=80`.<br>2. Kiểm tra scaling qua `kubectl get hpa`.<br>3. Mở rộng thủ công: cập nhật node count trong YAML và áp dụng lại. |

**Tổng thời gian**: 6 giờ  
**Ghi chú**: Yêu cầu Kubernetes cluster (Minikube, GKE, v.v.) và Helm đã được cài đặt. Người học cần quyền admin trên cluster.

---

## Ngày 4: Quản lý nâng cao và Sao lưu trên Kubernetes

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Bảo mật và truy cập trên Kubernetes** | Cấu hình TLS, quản lý RBAC, tích hợp với Kubernetes authentication. | 1.5 giờ | - [Security with ECK](https://www.elastic.co/docs/deploy-manage/security)<br>- [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) | **Lab 4.1**: Cấu hình bảo mật với ECK.<br>1. Tạo certificate cho TLS: sử dụng cert-manager hoặc tự tạo.<br>2. Cấu hình TLS trong YAML: thêm `tls` section.<br>3. Áp dụng và kiểm tra kết nối an toàn qua `curl --cacert ca.crt https://<service>:9200`.<br>4. Thiết lập RBAC cho user truy cập cụm. |
| **Sao lưu và khôi phục trên Kubernetes** | Sử dụng snapshot repository, cấu hình backup tự động, khôi phục dữ liệu từ snapshot. | 1.5 giờ | - [Backup with ECK](https://www.elastic.co/docs/deploy-manage/tools)<br>- [Snapshot and Restore](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html) | **Lab 4.2**: Sao lưu và khôi phục với ECK.<br>1. Cấu hình snapshot repository: tạo NFS volume và thêm vào YAML.<br>2. Thực hiện snapshot tự động: `kubectl apply -f snapshot-policy.yaml`.<br>3. Kiểm tra snapshot qua `kubectl get snapshots`.<br>4. Khôi phục dữ liệu: `kubectl apply -f restore.yaml`. |
| **Giám sát nâng cao với Prometheus** | Tích hợp Prometheus với Elasticsearch trên Kubernetes, tạo dashboard trên Grafana. | 2 giờ | - [Prometheus Integration](https://prometheus.io/docs/prometheus/latest/installation/)<br>- [Grafana Dashboards](https://grafana.com/grafana/dashboards/) | **Lab 4.3**: Tích hợp Prometheus và Grafana.<br>1. Cài đặt Prometheus operator: `helm install prometheus-operator prometheus-community/kube-prometheus-stack`.<br>2. Cấu hình scrape metrics từ Elasticsearch pod.<br>3. Triển khai Grafana: `helm install grafana grafana/grafana`.<br>4. Tạo dashboard cho metrics như heap usage, query rate. |
| **Xử lý sự cố và logging nâng cao** | Phân tích log từ pod, sử dụng EFK stack (Elasticsearch, Fluentd, Kibana), xử lý lỗi phổ biến. | 1 giờ | - [EFK Stack on Kubernetes](https://logz.io/learn/complete-guide-kubernetes-logging-efk-stack/) | **Lab 4.4**: Thiết lập EFK stack.<br>1. Cài đặt Fluentd: `helm install fluentd fluent/fluentd`.<br>2. Cấu hình Fluentd để thu thập log từ pod Elasticsearch.<br>3. Phân tích log trên Kibana, tìm lỗi như shard allocation failed.<br>4. Tạo alert cho lỗi quan trọng. |

**Tổng thời gian**: 6 giờ  
**Ghi chú**: Đảm bảo ECK và Kubernetes cluster đã được thiết lập từ ngày 3. Người học cần quyền admin và internet.

---

## Ngày 5: Tổng hợp và Đánh giá

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Tổng hợp kiến thức** | Ôn tập các khái niệm chính: triển khai, giám sát, mở rộng, sao lưu trên Docker và Kubernetes. | 1.5 giờ | - [Elasticsearch Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)<br>- [ECK Documentation](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s) | **Lab 5.1**: Ôn tập triển khai Docker.<br>1. Chạy lại cụm multi-node với Docker Compose.<br>2. Kiểm tra giám sát qua Metricbeat.<br>3. Sao lưu và khôi phục một index. |
| **Tối ưu hóa và best practices** | Áp dụng best practices cho sản xuất: cấu hình heap, resource limits, security, monitoring. | 1.5 giờ | - [Best Practices for Elasticsearch](https://www.elastic.co/blog/best-practices-elasticsearch-production)<br>- [Production Checklist](https://www.elastic.co/guide/en/elasticsearch/reference/current/production.html) | **Lab 5.2**: Tối ưu hóa cụm Kubernetes.<br>1. Cấu hình heap size và resource limits trong ECK YAML.<br>2. Kiểm tra hiệu suất qua Prometheus/Grafana.<br>3. Áp dụng TLS và RBAC. |
| **Chuẩn bị cho final lab** | Hướng dẫn cách tiếp cận bài final lab, các công cụ cần thiết, và cách debug. | 1 giờ | - [Troubleshooting Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/troubleshooting.html) | **Lab 5.3**: Debug một vấn đề giả lập.<br>1. Tạo lỗi shard allocation failed trên Kubernetes.<br>2. Sử dụng Kibana và log để tìm nguyên nhân.<br>3. Sửa lỗi và kiểm tra lại. |
| **Final Lab Preparation** | Chuẩn bị cho bài lab cuối, bao gồm các kịch bản thực tế. | 1 giờ | - [Final Lab Guidelines](#final-lab-guidelines) | **Lab 5.4**: Thực hành kịch bản.<br>1. Triển khai cụm trên Kubernetes với ECK.<br>2. Giám sát và mở rộng khi load tăng.<br>3. Sao lưu và khôi phục khi có sự cố. |

**Tổng thời gian**: 5 giờ  
**Ghi chú**: Đảm bảo tất cả công cụ từ các ngày trước đã sẵn sàng. Người học cần chuẩn bị cho bài final lab.

---

### Final Lab: Quản lý và Giám sát Elasticsearch trên Docker và Kubernetes

**Mô tả:**  
Bạn được giao nhiệm vụ triển khai và quản lý một cụm Elasticsearch cho một ứng dụng sản xuất, chạy trên cả Docker và Kubernetes. Yêu cầu bao gồm:  
- Triển khai cụm 3 node trên Docker và Kubernetes.  
- Thiết lập giám sát với Metricbeat trên Docker và ECK trên Kubernetes.  
- Mở rộng cụm khi load tăng (simulated load).  
- Sao lưu dữ liệu và khôi phục khi có sự cố giả lập.  

**Input:**  
- Docker Compose file cho cụm 3 node.  
- Kubernetes YAML cho ECK với 3 node (1 master, 2 data).  
- Simulated load script (cung cấp qua file `.sh`).  
- Snapshot repository đã cấu hình.  

**Output:**  
- Cụm Elasticsearch hoạt động trên cả Docker và Kubernetes, có thể truy cập qua API.  
- Dashboard trên Kibana cho metrics quan trọng (heap usage, query rate).  
- Log chứng minh đã mở rộng thành công khi load tăng.  
- Báo cáo khôi phục dữ liệu sau sự cố (log hoặc screenshot).  

**Outline:**  
1. Triển khai cụm Elasticsearch trên Docker và Kubernetes.  
2. Cấu hình giám sát với Metricbeat và ECK.  
3. Tạo load giả lập và mở rộng cụm.  
4. Thực hiện sao lưu và khôi phục dữ liệu.  
5. Kiểm tra và báo cáo kết quả.  

**Guidelines:**  
- Sử dụng tài liệu tham khảo từ các ngày trước để triển khai.  
- Đảm bảo security (TLS, RBAC) khi cần.  
- Debug lỗi qua log trên Kibana và CLI.  
- Ghi lại các bước và kết quả để báo cáo.  

---

### MCQ và Câu hỏi vấn đáp sau mỗi ngày

**Ngày 1 MCQ (10 câu):**  
1. Elasticsearch là gì? A) Công cụ quản lý cơ sở dữ liệu quan hệ B) Công cụ tìm kiếm và phân tích dữ liệu C) Công cụ giám sát mạng D) Công cụ quản lý container  
2. Lợi ích chính của việc chạy Elasticsearch trên Docker là gì? A) Tăng tốc độ xử lý query B) Dễ dàng triển khai và cô lập C) Giảm dung lượng bộ nhớ D) Tự động sao lưu dữ liệu  
3. Lệnh nào dùng để kiểm tra trạng thái Elasticsearch trên Docker? A) `docker ps` B) `curl http://localhost:9200` C) `docker logs` D) `kubectl get pods`  
4. Docker Compose được sử dụng để làm gì trong Elasticsearch? A) Chạy single node B) Quản lý cụm multi-node C) Tối ưu hóa Dockerfile D) Giám sát metrics  
5. Metricbeat thu thập dữ liệu gì từ container Elasticsearch? A) Log hệ thống B) Metrics tài nguyên (CPU, memory) C) Dữ liệu index D) Dữ liệu backup  
6. Lệnh nào kích hoạt KV secrets engine trên Elasticsearch? A) `vault secrets enable kv` B) `elasticsearch secrets enable kv` C) `docker secrets enable kv` D) `kubectl secrets enable kv`  
7. Để sao lưu dữ liệu, Elasticsearch sử dụng tính năng nào? A) Backup API B) Snapshot C) Export Data D) Log Forwarding  
8. Dashboard trên Kibana dùng để làm gì? A) Quản lý node roles B) Visualize metrics và logs C) Tạo snapshot D) Cấu hình TLS  
9. Lệnh nào dùng để mở rộng cụm trên Docker Compose? A) `docker-compose scale` B) `kubectl scale` C) `docker scale` D) `elasticsearch scale`  
10. File nào chứa cấu hình cho Elasticsearch trên Docker? A) `elasticsearch.yml` B) `docker-compose.yml` C) `config.json` D) `kibana.yml`  

**Ngày 1 Câu hỏi vấn đáp (5 câu):**  
1. Hãy giải thích vai trò của Metricbeat trong việc giám sát Elasticsearch trên Docker.  
2. Làm thế nào để tối ưu hóa tài nguyên container Elasticsearch trên Docker?  
3. Tại sao cần sử dụng Docker Compose cho cụm multi-node thay vì chạy từng container riêng lẻ?  
4. Hãy mô tả quy trình sao lưu dữ liệu trên Elasticsearch và tầm quan trọng của nó.  
5. Nếu gặp lỗi "No memory stats data available" trên Kibana, bạn sẽ làm gì để xử lý?  

**Ngày 2 MCQ (10 câu):**  
1. Horizontal Pod Autoscaler (HPA) được sử dụng để làm gì trên Kubernetes? A) Quản lý log B) Mở rộng pod dựa trên CPU/memory C) Sao lưu dữ liệu D) Cấu hình TLS  
2. Lệnh nào dùng để kiểm tra trạng thái HPA trên Kubernetes? A) `kubectl get hpa` B) `kubectl get pods` C) `kubectl get services` D) `kubectl get nodes`  
3. Elastic Agent thu thập dữ liệu gì từ Elasticsearch? A) Metrics và logs B) Chỉ metrics C) Chỉ logs D) Dữ liệu index  
4. Filebeat được sử dụng để làm gì? A) Thu thập metrics container B) Thu thập log container C) Tối ưu hóa heap D) Quản lý node roles  
5. Lệnh nào dùng để seal lại Vault? A) `vault operator seal` B) `vault operator unseal` C) `docker seal` D) `kubectl seal`  
6. Để tạo alert trên Kibana, bạn cần vào section nào? A) Dashboard B) Alerts C) Discover D) Visualize  
7. Resource limits trên Docker được cấu hình như thế nào? A) Trong `docker run --memory` B) Trong `docker-compose.yml` C) Trong `elasticsearch.yml` D) Cả A và B  
8. Lệnh nào dùng để kiểm tra log container trên Docker? A) `docker logs` B) `kubectl logs` C) `curl logs` D) `elasticsearch logs`  
9. Prometheus tích hợp với Elasticsearch như thế nào? A) Qua API B) Qua scrape metrics C) Qua log forwarding D) Qua dashboard  
10. Lệnh nào dùng để áp dụng YAML trên Kubernetes? A) `kubectl apply -f` B) `docker apply -f` C) `helm apply -f` D) `vault apply -f`  

**Ngày 2 Câu hỏi vấn đáp (5 câu):**  
1. Hãy giải thích cách sử dụng Elastic Agent để giám sát nâng cao trên Docker.  
2. Làm thế nào để xử lý lỗi shard allocation failed trên Elasticsearch?  
3. Tại sao cần cấu hình resource limits cho container Elasticsearch?  
4. Hãy mô tả quy trình mở rộng cụm Elasticsearch trên Docker Compose.  
5. Nếu dashboard trên Kibana không hiển thị metrics, bạn sẽ làm gì để debug?  

**Ngày 3 MCQ (10 câu):**  
1. ECK là gì? A) Công cụ giám sát Kubernetes B) Operator cho Elasticsearch trên Kubernetes C) Công cụ sao lưu dữ liệu D) Công cụ quản lý log  
2. Lệnh nào dùng để cài đặt ECK trên Kubernetes? A) `helm install elastic-operator` B) `kubectl install eck` C) `docker install eck` D) `vault install eck`  
3. Storage Class trên Kubernetes dùng để làm gì? A) Quản lý node roles B) Cung cấp storage cho pod C) Giám sát metrics D) Tạo dashboard  
4. Lệnh nào dùng để kiểm tra trạng thái cụm Elasticsearch trên Kubernetes? A) `kubectl get elasticsearch` B) `kubectl get pods` C) `kubectl get services` D) `kubectl get nodes`  
5. Kibana trên Kubernetes được triển khai như thế nào với ECK? A) Qua YAML file B) Qua Docker Compose C) Qua Helm chart D) Qua CLI  
6. Horizontal Pod Autoscaler (HPA) dựa vào metric nào để scale? A) CPU và memory B) Log size C) Network bandwidth D) Disk usage  
7. Lệnh nào dùng để tạo snapshot repository trên Kubernetes? A) `kubectl create snapshot` B) `elasticsearch create snapshot` C) `PUT _snapshot` D) `helm create snapshot`  
8. TLS trên Kubernetes được cấu hình như thế nào cho Elasticsearch? A) Trong YAML file B) Trong Docker Compose C) Trong `elasticsearch.yml` D) Trong CLI  
9. Lệnh nào dùng để mở rộng thủ công cụm trên Kubernetes? A) `kubectl scale` B) `docker scale` C) `helm scale` D) `vault scale`  
10. Monitoring với ECK được cấu hình ở đâu? A) Trong section `monitoring` của YAML B) Trong `docker-compose.yml` C) Trong `elasticsearch.yml` D) Trong CLI  

**Ngày 3 Câu hỏi vấn đáp (5 câu):**  
1. Hãy giải thích vai trò của ECK trong việc quản lý Elasticsearch trên Kubernetes.  
2. Làm thế nào để cấu hình storage class cho pod Elasticsearch trên Kubernetes?  
3. Tại sao cần sử dụng Kibana để visualize metrics trên Kubernetes?  
4. Hãy mô tả quy trình mở rộng cụm Elasticsearch với HPA trên Kubernetes.  
5. Nếu pod Elasticsearch không khởi động được, bạn sẽ làm gì để debug?  

**Ngày 4 MCQ (10 câu):**  
1. TLS trên Kubernetes được sử dụng để làm gì? A) Quản lý log B) Mã hóa kết nối C) Tăng tốc độ query D) Sao lưu dữ liệu  
2. Lệnh nào dùng để kiểm tra certificate TLS trên Kubernetes? A) `kubectl describe certificate` B) `kubectl get certificate` C) `curl --cacert` D) `docker describe certificate`  
3. Snapshot repository trên Kubernetes được lưu trữ ở đâu? A) NFS volume B) Local disk C) Docker volume D) Memory  
4. Lệnh nào dùng để thực hiện snapshot tự động trên Elasticsearch? A) `POST _snapshot` B) `kubectl snapshot` C) `docker snapshot` D) `helm snapshot`  
5. Prometheus scrape metrics từ đâu trên Kubernetes? A) Pod Elasticsearch B) Node Kubernetes C) Service Kubernetes D) ConfigMap  
6. Grafana được sử dụng để làm gì? A) Thu thập log B) Visualize metrics C) Sao lưu dữ liệu D) Quản lý node roles