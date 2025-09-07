# Lịch Trình Đào Tạo Elasticsearch (Tập Trung Vào Operation) Trong 5 Ngày

## Ngày 1: Giới Thiệu và Quản Lý Cơ Bản

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Giới thiệu Elasticsearch** | - Tổng quan về Elasticsearch: Search và analytics engine, vai trò trong DevOps.<br>- Kiến trúc: cluster, node, index, shard, replica.<br>- Cài đặt Elasticsearch server. | 2 giờ | [Elasticsearch Overview](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) | 1. Cài đặt Elasticsearch trên Ubuntu/CentOS hoặc Docker và kiểm tra phiên bản bằng `curl -X GET "localhost:9200"`.<br>2. Khởi động Elasticsearch và kiểm tra trạng thái cluster bằng `curl -X GET "localhost:9200/_cluster/health"`.<br>3. Tạo index `logs` bằng `curl -X PUT "localhost:9200/logs"`. |
| **Quản lý Server** | - Khởi động, dừng, và kiểm tra trạng thái server (`systemctl`, `docker`).<br>- Cấu hình `elasticsearch.yml` (cluster.name, node.name, network.host).<br>- Tự động khởi động với `systemd` hoặc Docker. | 2 giờ | [Elasticsearch Configuration](https://www.elastic.co/guide/en/elasticsearch/reference/current/settings.html) | 1. Khởi động Elasticsearch bằng `systemctl start elasticsearch` hoặc `docker run`.<br>2. Sửa `elasticsearch.yml` để thay đổi `cluster.name` và `node.name`.<br>3. Kích hoạt tự khởi động bằng `systemctl enable elasticsearch` hoặc Docker Compose. |
| **Quản lý Index** | - Tạo, xóa, và quản lý index.<br>- Cấu hình mapping cho index.<br>- Tìm kiếm cơ bản bằng REST API. | 2 giờ | [Elasticsearch Indices](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices.html) | 1. Tạo index `users` với mapping cho các trường `name`, `email`.<br>2. Index một document vào `users` bằng `curl -X POST`.<br>3. Thực hiện tìm kiếm cơ bản bằng `curl -X GET "localhost:9200/users/_search"`. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Elasticsearch là gì?  
   a) Cơ sở dữ liệu quan hệ  
   b) Search và analytics engine  
   c) Object storage  
   d) Monitoring tool  
   **Đáp án**: b
2. Lệnh nào kiểm tra trạng thái cluster Elasticsearch?  
   a) curl -X GET "localhost:9200/_cluster/health"  
   b) curl -X GET "localhost:9200/_status"  
   c) curl -X POST "localhost:9200/_cluster"  
   d) curl -X GET "localhost:9200/_health"  
   **Đáp án**: a
3. File cấu hình chính của Elasticsearch là gì?  
   a) elasticsearch.yml  
   b) config.yaml  
   c) settings.conf  
   d) elastic.conf  
   **Đáp án**: a
4. Lệnh nào tạo index trong Elasticsearch?  
   a) curl -X PUT "localhost:9200/my_index"  
   b) curl -X POST "localhost:9200/my_index"  
   c) curl -X GET "localhost:9200/my_index"  
   d) curl -X DELETE "localhost:9200/my_index"  
   **Đáp án**: a
5. Shard trong Elasticsearch dùng để làm gì?  
   a) Phân chia dữ liệu trên các node  
   b) Tạo mapping  
   c) Tìm kiếm dữ liệu  
   d) Sao lưu dữ liệu  
   **Đáp án**: a
6. Lệnh nào index một document?  
   a) curl -X POST "localhost:9200/my_index/_doc"  
   b) curl -X PUT "localhost:9200/my_index"  
   c) curl -X GET "localhost:9200/my_index/_doc"  
   d) curl -X DELETE "localhost:9200/my_index/_doc"  
   **Đáp án**: a
7. `cluster.name` trong `elasticsearch.yml` dùng để làm gì?  
   a) Định danh cluster  
   b) Cấu hình port  
   c) Cấu hình logging  
   d) Cấu hình backup  
   **Đáp án**: a
8. Replica trong Elasticsearch giúp gì?  
   a) Tăng tính sẵn sàng cao  
   b) Tăng tốc tìm kiếm  
   c) Tạo index  
   d) Sao lưu dữ liệu  
   **Đáp án**: a
9. Lệnh nào kiểm tra phiên bản Elasticsearch?  
   a) curl -X GET "localhost:9200"  
   b) elasticsearch --version  
   c) Cả hai  
   d) curl -X GET "localhost:9200/_version"  
   **Đáp án**: c
10. Mapping trong Elasticsearch dùng để làm gì?  
    a) Định nghĩa cấu trúc dữ liệu  
    b) Tạo index  
    c) Tìm kiếm dữ liệu  
    d) Sao lưu dữ liệu  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao Elasticsearch được sử dụng phổ biến trong DevOps?
2. Mô tả các thành phần chính trong kiến trúc Elasticsearch (cluster, node, shard, replica).
3. Làm thế nào để cấu hình Elasticsearch tự khởi động?
4. Giải thích vai trò của mapping trong quản lý index.
5. Các best practice khi cấu hình `elasticsearch.yml` là gì?

## Ngày 2: Sao Lưu, Khôi Phục và Giám Sát

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Sao Lưu và Khôi Phục** | - Snapshot và restore trong Elasticsearch.<br>- Cấu hình snapshot repository.<br>- Quy trình khôi phục index từ snapshot. | 2.5 giờ | [Elasticsearch Snapshot and Restore](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html) | 1. Tạo snapshot repository trên file system local bằng `curl -X PUT`.<br>2. Thực hiện snapshot cho index `logs` bằng `curl -X PUT "localhost:9200/_snapshot/my_repo/snapshot_1"`.<br>3. Khôi phục index `logs` từ snapshot vào index mới `logs_restore`. |
| **Giám Sát Elasticsearch** | - Sử dụng API `_cluster/health`, `_cat/nodes`.<br>- Tích hợp Metricbeat để giám sát metrics.<br>- Cấu hình alert cho cluster health. | 2.5 giờ | [Elasticsearch Monitoring](https://www.elastic.co/guide/en/elasticsearch/reference/current/monitoring.html) | 1. Kiểm tra trạng thái cluster bằng `curl -X GET "localhost:9200/_cluster/health"`.<br>2. Cài đặt Metricbeat và cấu hình để thu thập metrics Elasticsearch.<br>3. Tạo alert trong Kibana cho trạng thái cluster chuyển sang yellow/red. |
| **Quản Lý Log** | - Cấu hình logging trong `elasticsearch.yml`.<br>- Phân tích log để debug.<br>- Best practices cho logging. | 1 giờ | [Elasticsearch Logging](https://www.elastic.co/guide/en/elasticsearch/reference/current/logging.html) | 1. Cấu hình `log.level` trong `elasticsearch.yml` để ghi log chi tiết.<br>2. Kiểm tra log file Elasticsearch để phân tích lỗi.<br>3. Cấu hình log rotation bằng `logrotate` cho log Elasticsearch. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Lệnh nào tạo snapshot repository trong Elasticsearch?  
   a) curl -X PUT "localhost:9200/_snapshot/my_repo"  
   b) curl -X POST "localhost:9200/_snapshot"  
   c) curl -X GET "localhost:9200/_snapshot"  
   d) curl -X DELETE "localhost:9200/_snapshot"  
   **Đáp án**: a
2. Snapshot trong Elasticsearch dùng để làm gì?  
   a) Sao lưu index  
   b) Tạo index  
   c) Tìm kiếm dữ liệu  
   d) Giám sát cluster  
   **Đáp án**: a
3. Lệnh nào kiểm tra trạng thái node?  
   a) curl -X GET "localhost:9200/_cat/nodes"  
   b) curl -X GET "localhost:9200/_nodes"  
   c) Cả hai  
   d) curl -X GET "localhost:9200/_cluster"  
   **Đáp án**: c
4. Metricbeat dùng để làm gì trong Elasticsearch?  
   a) Thu thập metrics cluster  
   b) Tạo snapshot  
   c) Tìm kiếm dữ liệu  
   d) Cấu hình logging  
   **Đáp án**: a
5. Lệnh nào khôi phục index từ snapshot?  
   a) curl -X POST "localhost:9200/_snapshot/my_repo/snapshot_1/_restore"  
   b) curl -X PUT "localhost:9200/_snapshot/my_repo"  
   c) curl -X GET "localhost:9200/_snapshot"  
   d) curl -X DELETE "localhost:9200/_snapshot"  
   **Đáp án**: a
6. Log file Elasticsearch thường nằm ở đâu?  
   a) /var/log/elasticsearch  
   b) Data directory  
   c) Cả hai  
   d) /etc/elasticsearch  
   **Đáp án**: c
7. Tham số nào cấu hình mức độ log?  
   a) log.level  
   b) log.destination  
   c) log.rotation  
   d) log.min_duration  
   **Đáp án**: a
8. Log rotation trong Elasticsearch được cấu hình bằng gì?  
   a) logrotate  
   b) elasticsearch.yml  
   c) cron  
   d) Metricbeat  
   **Đáp án**: a
9. Lệnh nào kiểm tra trạng thái cluster health?  
   a) curl -X GET "localhost:9200/_cluster/health"  
   b) curl -X GET "localhost:9200/_health"  
   c) curl -X GET "localhost:9200/_status"  
   d) curl -X POST "localhost:9200/_cluster"  
   **Đáp án**: a
10. Best practice khi sao lưu Elasticsearch là gì?  
    a) Sử dụng snapshot repository  
    b) Tắt logging  
    c) Không dùng Metricbeat  
    d) Xóa index  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao sao lưu và khôi phục quan trọng trong vận hành Elasticsearch?
2. Mô tả quy trình tạo snapshot và khôi phục index.
3. Làm thế nào để giám sát trạng thái cluster bằng Metricbeat?
4. Giải thích cách cấu hình log rotation cho Elasticsearch.
5. Các best practice khi giám sát Elasticsearch là gì?

## Ngày 3: Tìm Kiếm và Tối Ưu Hiệu Suất

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Tìm Kiếm Cơ Bản** | - Tìm kiếm bằng REST API (match, term queries).<br>- Sử dụng Query DSL.<br>- Kết quả tìm kiếm và relevance scoring. | 2 giờ | [Elasticsearch Search](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html) | 1. Thực hiện match query để tìm kiếm document trong index `logs`.<br>2. Sử dụng term query để tìm kiếm chính xác một giá trị.<br>3. Kết hợp match và term query bằng bool query. |
| **Tối Ưu Tìm Kiếm** | - Sử dụng filter để tăng hiệu suất.<br>- Caching query results.<br>- Tối ưu hóa relevance scoring. | 2 giờ | [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) | 1. Tạo filter query để giảm thời gian tìm kiếm trong `logs`.<br>2. Kích hoạt caching cho query thường xuyên bằng `request_cache`.<br>3. Tối ưu hóa relevance scoring bằng cách điều chỉnh `boost` trong query. |
| **Cấu Hình Hiệu Suất** | - Điều chỉnh JVM heap size.<br>- Cấu hình thread pools.<br>- Quản lý shard và replica. | 2 giờ | [Elasticsearch Performance](https://www.elastic.co/guide/en/elasticsearch/reference/current/tune-for-search-speed.html) | 1. Thay đổi JVM heap size trong `jvm.options`.<br>2. Cấu hình thread pool cho tìm kiếm trong `elasticsearch.yml`.<br>3. Điều chỉnh số lượng replica cho index `logs` và kiểm tra hiệu suất. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Match query trong Elasticsearch dùng để làm gì?  
   a) Tìm kiếm full-text  
   b) Tìm kiếm chính xác  
   c) Tạo index  
   d) Sao lưu dữ liệu  
   **Đáp án**: a
2. Term query khác match query như thế nào?  
   a) Term tìm kiếm chính xác, match tìm kiếm full-text  
   b) Term nhanh hơn match  
   c) Match dùng filter, term không  
   d) Không có khác biệt  
   **Đáp án**: a
3. Lệnh nào thực hiện tìm kiếm trong Elasticsearch?  
   a) curl -X GET "localhost:9200/my_index/_search"  
   b) curl -X POST "localhost:9200/my_index/_doc"  
   c) curl -X PUT "localhost:9200/my_index"  
   d) curl -X DELETE "localhost:9200/my_index"  
   **Đáp án**: a
4. Filter query cải thiện hiệu suất như thế nào?  
   a) Giảm dữ liệu cần xử lý  
   b) Tăng relevance scoring  
   c) Tạo index  
   d) Sao lưu dữ liệu  
   **Đáp án**: a
5. Tham số nào kích hoạt caching query?  
   a) request_cache  
   b) query_cache  
   c) search_cache  
   d) cache_enabled  
   **Đáp án**: a
6. JVM heap size được cấu hình ở đâu?  
   a) jvm.options  
   b) elasticsearch.yml  
   c) log4j2.properties  
   d) snapshot.yml  
   **Đáp án**: a
7. Relevance scoring trong Elasticsearch dựa trên gì?  
   a) TF-IDF và BM25  
   b) IP address  
   c) Shard count  
   d) Replica count  
   **Đáp án**: a
8. Lệnh nào điều chỉnh số replica?  
   a) curl -X PUT "localhost:9200/my_index/_settings"  
   b) curl -X POST "localhost:9200/my_index/_replica"  
   c) curl -X GET "localhost:9200/my_index/_settings"  
   d) curl -X DELETE "localhost:9200/my_index/_replica"  
   **Đáp án**: a
9. Thread pool trong Elasticsearch dùng để làm gì?  
   a) Quản lý concurrency  
   b) Tạo index  
   c) Sao lưu dữ liệu  
   d) Giám sát cluster  
   **Đáp án**: a
10. Best practice khi tối ưu tìm kiếm là gì?  
    a) Sử dụng filter query  
    b) Tắt caching  
    c) Không dùng replica  
    d) Xóa index  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao filter query hiệu quả hơn match query trong một số trường hợp?
2. Mô tả cách sử dụng Query DSL để kết hợp nhiều điều kiện tìm kiếm.
3. Làm thế nào để tối ưu hóa relevance scoring trong Elasticsearch?
4. Giải thích vai trò của JVM heap size trong hiệu suất Elasticsearch.
5. Các best practice khi cấu hình shard và replica là gì?

## Ngày 4: Bảo Mật và Bảo Trì

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Bảo Mật Elasticsearch** | - Kích hoạt authentication và RBAC.<br>- Cấu hình TLS cho kết nối an toàn.<br>- Quản lý user và role. | 2.5 giờ | [Elasticsearch Security](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-settings.html) | 1. Kích hoạt basic authentication và tạo user `admin` bằng Kibana.<br>2. Cấu hình TLS cho cluster bằng certificate tự ký.<br>3. Tạo role `read_only` và gán cho user để giới hạn truy cập index `logs`. |
| **Bảo Trì Cluster** | - Quản lý shard allocation.<br>- Reindexing và shrink index.<br>- Nâng cấp Elasticsearch. | 2.5 giờ | [Elasticsearch Cluster Maintenance](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-reindex.html) | 1. Kiểm tra shard allocation bằng `curl -X GET "localhost:9200/_cat/shards"`.<br>2. Thực hiện reindex từ index `logs` sang `logs_new`.<br>3. Mô phỏng nâng cấp Elasticsearch bằng Docker (hoặc đọc tài liệu). |
| **Quản Lý Lỗi** | - Xử lý lỗi phổ biến (OOM, shard failures).<br>- Phân tích log để debug.<br>- Best practices cho xử lý lỗi. | 1 giờ | [Elasticsearch Error Handling](https://www.elastic.co/guide/en/elasticsearch/reference/current/troubleshooting.html) | 1. Tạo tình huống OOM bằng cách giảm heap size và kiểm tra log.<br>2. Kiểm tra lỗi shard failure bằng `curl -X GET "localhost:9200/_cluster/health"`.<br>3. Cấu hình `log.level` để ghi lại lỗi chi tiết. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Lệnh nào kích hoạt authentication trong Elasticsearch?  
   a) xpack.security.enabled = true  
   b) security.enabled = true  
   c) auth.enabled = true  
   d) tls.enabled = true  
   **Đáp án**: a
2. TLS trong Elasticsearch dùng để làm gì?  
   a) Mã hóa kết nối  
   b) Tạo index  
   c) Sao lưu dữ liệu  
   d) Giám sát cluster  
   **Đáp án**: a
3. Lệnh nào tạo user trong Elasticsearch?  
   a) curl -X POST "localhost:9200/_security/user/admin"  
   b) curl -X PUT "localhost:9200/_user/admin"  
   c) curl -X GET "localhost:9200/_security/user"  
   d) curl -X DELETE "localhost:9200/_security/user"  
   **Đáp án**: a
4. Lệnh nào kiểm tra shard allocation?  
   a) curl -X GET "localhost:9200/_cat/shards"  
   b) curl -X GET "localhost:9200/_shards"  
   c) curl -X GET "localhost:9200/_cluster/shards"  
   d) curl -X POST "localhost:9200/_cat/shards"  
   **Đáp án**: a
5. Reindex trong Elasticsearch dùng để làm gì?  
   a) Sao chép dữ liệu sang index mới  
   b) Tạo snapshot  
   c) Tìm kiếm dữ liệu  
   d) Giám sát cluster  
   **Đáp án**: a
6. Lỗi OOM trong Elasticsearch là gì?  
   a) Out of Memory  
   b) Out of Shards  
   c) Out of Replicas  
   d) Out of Connections  
   **Đáp án**: a
7. Lệnh nào nâng cấp Elasticsearch?  
   a) docker pull docker.elastic.co/elasticsearch/elasticsearch  
   b) curl -X POST "localhost:9200/_upgrade"  
   c) systemctl upgrade elasticsearch  
   d) Cả a và b  
   **Đáp án**: a
8. Log nào giúp debug lỗi Elasticsearch?  
   a) Cluster log  
   b) Application log  
   c) Cả hai  
   d) Không có log  
   **Đáp án**: c
9. Tham số nào ghi lại lỗi chi tiết?  
   a) log.level  
   b) log.destination  
   c) log.rotation  
   d) log.min_duration  
   **Đáp án**: a
10. Best practice khi bảo trì cluster là gì?  
    a) Kiểm tra shard allocation  
    b) Tắt logging  
    c) Không dùng replica  
    d) Xóa index  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao cần authentication và TLS trong Elasticsearch?
2. Mô tả cách cấu hình RBAC để giới hạn truy cập index.
3. Làm thế nào để xử lý lỗi OOM trong Elasticsearch?
4. Giải thích vai trò của reindex trong bảo trì cluster.
5. Các best practice khi quản lý lỗi trong Elasticsearch là gì?

## Ngày 5: Final Lab và Đánh Giá

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Final Lab** | Triển khai hệ thống Elasticsearch cho ứng dụng log phân tích, với quản lý index, tìm kiếm, giám sát, bảo mật, và sao lưu. | 4 giờ | [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) | **Mô tả**: Thiết lập cluster Elasticsearch với 3 node để lưu trữ và phân tích log ứng dụng, tích hợp Kibana để visualize, cấu hình giám sát, bảo mật, và sao lưu.<br>**Yêu cầu**:<br>- **Môi trường**: Máy local Ubuntu/CentOS với Elasticsearch, Kibana, Metricbeat hoặc container Docker.<br>- **Đề mục**:<br>  1. **Thiết lập cluster**: Cài đặt cluster 3 node với Elasticsearch và Kibana.<br>  2. **Quản lý index**: Tạo index `app_logs` với mapping cho log (timestamp, message, level).<br>  3. **Tìm kiếm**: Thiết lập match query và filter query để tìm kiếm log theo level (ERROR, INFO).<br>  4. **Sao lưu**: Tạo snapshot repository và snapshot index `app_logs`.<br>  5. **Giám sát**: Cấu hình Metricbeat để thu thập metrics cluster và tạo alert trong Kibana.<br>  6. **Bảo mật**: Kích hoạt authentication, RBAC, và TLS cho cluster.<br>  7. **Tài liệu**: Cung cấp README.md với sơ đồ kiến trúc, cấu hình, và quy trình vận hành.<br>**Guideline**:<br>- Sử dụng `curl` hoặc Kibana để quản lý index và tìm kiếm.<br>- Đảm bảo cluster có tính sẵn sàng cao với replica.<br>- Kiểm tra quyền user để chỉ truy cập index cần thiết.<br>- Tài liệu hóa rõ ràng, bao gồm sơ đồ cluster và hướng dẫn tái tạo.<br>- Kiểm tra hiệu suất tìm kiếm bằng Kibana.<br>- Đảm bảo snapshot có thể khôi phục thành công. |
| **MCQ** | Bài kiểm tra trắc nghiệm về các tác vụ vận hành Elasticsearch. | 2 giờ | [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) | Tạo và trả lời 20 câu hỏi trắc nghiệm về kiến trúc, quản lý index, sao lưu, giám sát, tìm kiếm, và bảo mật. Sample MCQs:<br>1. Elasticsearch là gì? (a) Search và analytics engine **(Đáp án: a)**<br>2. Lệnh nào tạo index? (a) curl -X PUT "localhost:9200/my_index" **(Đáp án: a)**<br>3. Snapshot dùng để làm gì? (a) Sao lưu index **(Đáp án: a)**<br>4. Metricbeat dùng để làm gì? (a) Thu thập metrics cluster **(Đáp án: a)**<br>5. TLS dùng để làm gì? (a) Mã hóa kết nối **(Đáp án: a)** |

**Tổng thời gian**: 6 giờ

## Ghi Chú
- **Tổng thời gian**: 30 giờ (6 giờ/ngày).
- **Môi trường thực hành**: Máy local với Elasticsearch, Kibana, Metricbeat hoặc container Docker, hoặc [Elastic Cloud Trial](https://www.elastic.co/cloud/elasticsearch-service).
- **Tài liệu chính**: [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).
- **Final Lab**: Dự án thực tế triển khai hệ thống log phân tích, tập trung vào vận hành.
- **Đánh giá**: MCQ và câu hỏi vấn đáp củng