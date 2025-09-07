# Lịch Trình Đào Tạo MinIO (Tập Trung Vào Operation) Trong 5 Ngày

## Ngày 1: Giới Thiệu và Quản Lý Cơ Bản

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Giới thiệu MinIO** | - Tổng quan về MinIO: Object storage, vai trò trong DevOps.<br>- Kiến trúc: server, client, bucket, object.<br>- Cài đặt MinIO server và client. | 2 giờ | [MinIO Documentation](https://docs.min.io/) | 1. Cài đặt MinIO server trên Ubuntu/CentOS và kiểm tra bằng `minio server`.<br>2. Kết nối MinIO client (`mc`) và kiểm tra phiên bản.<br>3. Tạo bucket `ecommerce` bằng `mc mb`. |
| **Quản lý Server** | - Khởi động, dừng, và kiểm tra trạng thái.<br>- Cấu hình MinIO (`minio.conf`).<br>- Tự động khởi động với `systemd`. | 2 giờ | [MinIO Server Configuration](https://docs.min.io/docs/minio-server-configuration-guide.html) | 1. Khởi động MinIO server bằng `systemd`.<br>2. Cấu hình `MINIO_ROOT_USER` và `MINIO_ROOT_PASSWORD` trong `minio.conf`.<br>3. Kiểm tra trạng thái server bằng `mc admin info`. |
| **Quản lý Bucket và Object** | - Tạo và quản lý bucket, object.<br>- Gán policy cho bucket.<br>- Kết nối qua MinIO Console hoặc `mc`. | 2 giờ | [MinIO Bucket Management](https://docs.min.io/docs/minio-client-complete-guide.html) | 1. Tạo bucket `products` và upload file bằng `mc cp`.<br>2. Gán read-only policy cho bucket `products`.<br>3. Kết nối đến MinIO Console và kiểm tra bucket. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. MinIO là loại storage nào?  
   a) Block storage  
   b) Object storage  
   c) File storage  
   d) Database  
   **Đáp án**: b
2. Lệnh nào tạo bucket trong MinIO?  
   a) mc mb  
   b) mc create  
   c) mc bucket  
   d) mc add  
   **Đáp án**: a
3. Công cụ nào dùng để quản lý MinIO qua CLI?  
   a) mc  
   b) minio  
   c) s3cmd  
   d) aws  
   **Đáp án**: a
4. File cấu hình chính của MinIO là gì?  
   a) minio.conf  
   b) minio.ini  
   c) config.json  
   d) server.conf  
   **Đáp án**: a
5. Lệnh nào kiểm tra trạng thái MinIO server?  
   a) mc admin info  
   b) minio status  
   c) systemctl status minio  
   d) Cả a và c  
   **Đáp án**: d
6. Lệnh nào upload file lên bucket?  
   a) mc cp  
   b) mc mv  
   c) mc ls  
   d) mc rm  
   **Đáp án**: a
7. MinIO Console dùng để làm gì?  
   a) Quản lý bucket qua GUI  
   b) Tạo index  
   c) Sao lưu dữ liệu  
   d) Giám sát hiệu suất  
   **Đáp án**: a
8. Lệnh nào gán policy cho bucket?  
   a) mc policy set  
   b) mc policy add  
   c) mc policy create  
   d) mc policy assign  
   **Đáp án**: a
9. MinIO hỗ trợ giao thức nào?  
   a) S3-compatible API  
   b) SQL  
   c) SSH  
   d) FTP  
   **Đáp án**: a
10. Lệnh nào liệt kê bucket?  
    a) mc ls  
    b) mc dir  
    c) mc list  
    d) mc show  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao MinIO phù hợp với DevOps?
2. Mô tả kiến trúc của MinIO server.
3. Làm thế nào để cấu hình MinIO tự khởi động?
4. Giải thích cách gán policy cho bucket trong MinIO.
5. Sự khác biệt giữa MinIO server và client là gì?

## Ngày 2: Sao Lưu, Khôi Phục và Giám Sát

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Sao Lưu và Khôi Phục** | - Sao lưu bucket bằng `mc mirror`.<br>- Đồng bộ dữ liệu sang bucket khác.<br>- Quy trình khôi phục bucket. | 2.5 giờ | [MinIO Backup](https://docs.min.io/docs/minio-client-complete-guide.html#mirror) | 1. Sao lưu bucket `products` sang bucket `products_backup` bằng `mc mirror`.<br>2. Khôi phục bucket `products` từ `products_backup`.<br>3. Đồng bộ bucket sang server MinIO khác bằng `mc mirror`. |
| **Giám Sát MinIO** | - Sử dụng MinIO Prometheus endpoint.<br>- Theo dõi metrics (storage, requests).<br>- Cấu hình alert với Prometheus. | 2.5 giờ | [MinIO Monitoring](https://docs.min.io/docs/minio-monitoring-guide.html) | 1. Kích hoạt Prometheus endpoint và kiểm tra metrics bằng `curl`.<br>2. Tạo alert rule trong Prometheus cho storage usage vượt 80%.<br>3. Kiểm tra metrics request latency trong Prometheus. |
| **Quản Lý Log** | - Cấu hình audit log.<br>- Phân tích log với `mc admin logs`.<br>- Best practices cho logging. | 1 giờ | [MinIO Logging](https://docs.min.io/docs/minio-logging.html) | 1. Kích hoạt audit log cho server MinIO.<br>2. Kiểm tra audit log bằng `mc admin logs`.<br>3. Cấu hình log rotation cho audit log bằng `logrotate`. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Lệnh nào sao lưu bucket trong MinIO?  
   a) mc mirror  
   b) mc cp  
   c) mc mv  
   d) mc ls  
   **Đáp án**: a
2. MinIO Prometheus endpoint dùng để làm gì?  
   a) Theo dõi metrics  
   b) Sao lưu dữ liệu  
   c) Tạo bucket  
   d) Quản lý user  
   **Đáp án**: a
3. Lệnh nào kiểm tra audit log?  
   a) mc admin logs  
   b) mc logs  
   c) mc audit  
   d) mc status  
   **Đáp án**: a
4. Log rotation trong MinIO được cấu hình bằng gì?  
   a) logrotate  
   b) mc log  
   c) cron  
   d) minio.conf  
   **Đáp án**: a
5. Metric nào đo storage usage trong MinIO?  
   a) minio_bucket_usage_total  
   b) minio_request_count  
   c) minio_latency  
   d) minio_errors  
   **Đáp án**: a
6. Lệnh nào đồng bộ bucket sang server khác?  
   a) mc mirror  
   b) mc sync  
   c) mc cp  
   d) mc mv  
   **Đáp án**: a
7. Audit log trong MinIO ghi lại gì?  
   a) Hoạt động trên bucket  
   b) Lỗi server  
   c) Kết nối user  
   d) Tất cả  
   **Đáp án**: d
8. Best practice khi sao lưu MinIO là gì?  
   a) Sử dụng `mc mirror`  
   b) Tắt logging  
   c) Không dùng Prometheus  
   d) Xóa bucket  
   **Đáp án**: a
9. Lệnh nào kiểm tra trạng thái server?  
   a) mc admin info  
   b) mc status  
   c) minio status  
   d) mc ls  
   **Đáp án**: a
10. Prometheus endpoint của MinIO nằm ở đâu?  
    a) /minio/v2/metrics/cluster  
    b) /minio/logs  
    c) /minio/status  
    d) /minio/backup  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao sao lưu bucket quan trọng trong vận hành MinIO?
2. Mô tả quy trình sao lưu và khôi phục bằng `mc mirror`.
3. Làm thế nào để giám sát MinIO bằng Prometheus?
4. Giải thích cách cấu hình audit log trong MinIO.
5. Các best practice khi giám sát MinIO là gì?

## Ngày 3: Tối Ưu Hiệu Suất

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Tối Ưu Hiệu Suất Bucket** | - Cấu hình versioning và lifecycle rules.<br>- Tối ưu hóa upload/download.<br>- Sử dụng multipart upload. | 2 giờ | [MinIO Versioning](https://docs.min.io/docs/minio-bucket-versioning.html) | 1. Kích hoạt versioning trên bucket `products`.<br>2. Tạo lifecycle rule để xóa object cũ sau 30 ngày.<br>3. Upload file lớn bằng multipart upload với `mc cp`. |
| **Load Balancing** | - Sử dụng load balancer (Nginx, HAProxy).<br>- Phân phối request đến MinIO nodes.<br>- Best practices cho load balancing. | 2 giờ | [MinIO Load Balancing](https://docs.min.io/docs/minio-multi-site-deployment.html) | 1. Cấu hình Nginx làm load balancer cho MinIO server.<br>2. Kiểm tra phân phối request bằng `mc stat`.<br>3. Thêm health check trong Nginx cho MinIO nodes. |
| **Caching** | - Sử dụng caching với MinIO.<br>- Cấu hình CDN (Cloudflare).<br>- Tối ưu hóa hiệu suất với cache. | 2 giờ | [MinIO Caching](https://docs.min.io/docs/minio-cache.html) | 1. Cấu hình caching cho bucket `products` với `mc cache`.<br>2. Kiểm tra cache hit/miss bằng metrics Prometheus.<br>3. Mô phỏng CDN với Cloudflare (hoặc đọc tài liệu). |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Versioning trong MinIO dùng để làm gì?  
   a) Lưu trữ nhiều phiên bản object  
   b) Sao lưu bucket  
   c) Tạo index  
   d) Giám sát hiệu suất  
   **Đáp án**: a
2. Lệnh nào kích hoạt versioning?  
   a) mc version enable  
   b) mc version add  
   c) mc version create  
   d) mc version set  
   **Đáp án**: a
3. Lifecycle rule trong MinIO làm gì?  
   a) Xóa object cũ  
   b) Tạo bucket  
   c) Tăng tốc upload  
   d) Giám sát server  
   **Đáp án**: a
4. Load balancer giúp gì cho MinIO?  
   a) Phân phối request  
   b) Tạo bucket  
   c) Sao lưu dữ liệu  
   d) Tạo index  
   **Đáp án**: a
5. Lệnh nào cấu hình caching trong MinIO?  
   a) mc cache  
   b) mc policy  
   c) mc version  
   d) mc mirror  
   **Đáp án**: a
6. Multipart upload dùng để làm gì?  
   a) Upload file lớn  
   b) Sao lưu bucket  
   c) Tạo index  
   d) Giám sát server  
   **Đáp án**: a
7. Metric nào đo cache hit trong MinIO?  
   a) minio_cache_hit  
   b) minio_bucket_usage  
   c) minio_request_count  
   d) minio_latency  
   **Đáp án**: a
8. Lệnh nào kiểm tra object trong bucket?  
   a) mc stat  
   b) mc ls  
   c) mc cp  
   d) mc rm  
   **Đáp án**: a
9. CDN cải thiện gì cho MinIO?  
   a) Hiệu suất truy cập  
   b) Bảo mật dữ liệu  
   c) Sao lưu bucket  
   d) Tạo index  
   **Đáp án**: a
10. Best practice khi dùng load balancer là gì?  
    a) Sử dụng health check  
    b) Tắt caching  
    c) Không dùng versioning  
    d) Xóa bucket  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao versioning quan trọng trong MinIO?
2. Mô tả cách cấu hình lifecycle rule trong MinIO.
3. Làm thế nào để sử dụng load balancer với MinIO?
4. Giải thích vai trò của caching trong cải thiện hiệu suất MinIO.
5. Các best practice khi tối ưu hóa hiệu suất MinIO là gì?

## Ngày 4: Bảo Mật và Bảo Trì

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Bảo Mật MinIO** | - Kích hoạt TLS cho kết nối an toàn.<br>- Server-side encryption (SSE).<br>- Quản lý user và policy. | 2.5 giờ | [MinIO Security](https://docs.min.io/docs/minio-security-overview.html) | 1. Kích hoạt TLS cho MinIO server bằng certificate tự ký.<br>2. Cấu hình SSE cho bucket `products`.<br>3. Tạo user mới và gán policy read-only bằng `mc admin user`. |
| **Bảo Trì Server** | - Quản lý disk usage.<br>- Xử lý bloat với lifecycle rules.<br>- Nâng cấp MinIO server. | 2.5 giờ | [MinIO Maintenance](https://docs.min.io/docs/minio-server-maintenance.html) | 1. Kiểm tra disk usage bằng `mc admin info`.<br>2. Tạo lifecycle rule để xóa object hết hạn.<br>3. Mô phỏng nâng cấp MinIO server bằng Docker (hoặc đọc tài liệu). |
| **Quản Lý Lỗi** | - Xử lý lỗi phổ biến (connection issues, disk full).<br>- Phân tích log để debug.<br>- Best practices cho xử lý lỗi. | 1 giờ | [MinIO Error Handling](https://docs.min.io/docs/minio-logging.html) | 1. Tạo tình huống disk full và kiểm tra log để xác định nguyên nhân.<br>2. Kiểm tra lỗi kết nối bằng cách sửa sai endpoint và khắc phục.<br>3. Kích hoạt audit log chi tiết để ghi lại lỗi. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. TLS trong MinIO dùng để làm gì?  
   a) Mã hóa kết nối  
   b) Tạo bucket  
   c) Sao lưu dữ liệu  
   d) Giám sát server  
   **Đáp án**: a
2. Lệnh nào tạo user mới trong MinIO?  
   a) mc admin user add  
   b) mc user create  
   c) mc add user  
   d) mc policy user  
   **Đáp án**: a
3. SSE trong MinIO là gì?  
   a) Server-side encryption  
   b) Client-side encryption  
   c) Bucket versioning  
   d) Load balancing  
   **Đáp án**: a
4. Lệnh nào kiểm tra disk usage?  
   a) mc admin info  
   b) mc stat  
   c) mc ls  
   d) mc cp  
   **Đáp án**: a
5. Lifecycle rule giúp gì trong bảo trì MinIO?  
   a) Xóa object cũ  
   b) Tạo bucket  
   c) Tăng tốc upload  
   d) Giám sát server  
   **Đáp án**: a
6. Lệnh nào kích hoạt audit log chi tiết?  
   a) mc admin config set audit  
   b) mc log enable  
   c) mc audit set  
   d) mc config log  
   **Đáp án**: a
7. Lỗi disk full xử lý thế nào?  
   a) Thêm disk hoặc xóa object  
   b) Tắt server  
   c) Tạo bucket mới  
   d) Xóa policy  
   **Đáp án**: a
8. Lệnh nào nâng cấp MinIO server?  
   a) minio server --upgrade  
   b) docker pull minio/minio  
   c) mc admin update  
   d) Cả b và c  
   **Đáp án**: d
9. Audit log ghi lại gì?  
   a) Hoạt động trên bucket  
   b) Lỗi server  
   c) Kết nối user  
   d) Tất cả  
   **Đáp án**: d
10. Best practice khi cấu hình bảo mật MinIO là gì?  
    a) Sử dụng TLS và SSE  
    b) Tắt versioning  
    c) Không dùng policy  
    d) Xóa log  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao cần TLS trong MinIO? Làm thế nào để kích hoạt?
2. Mô tả cách cấu hình server-side encryption trong MinIO.
3. Làm thế nào để xử lý lỗi disk full trong MinIO?
4. Giải thích vai trò của lifecycle rules trong bảo trì MinIO.
5. Các best practice khi quản lý lỗi trong MinIO là gì?

## Ngày 5: Final Lab và Đánh Giá

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Final Lab** | Triển khai MinIO cho ứng dụng e-commerce, với quản lý bucket, versioning, bảo mật, và giám sát. | 4 giờ | [MinIO Documentation](https://docs.min.io/) | **Mô tả**: Thiết lập MinIO server cho ứng dụng e-commerce, lưu trữ hình ảnh sản phẩm, tài liệu đơn hàng, và log, đảm bảo versioning, bảo mật, và giám sát.<br>**Yêu cầu**:<br>- **Môi trường**: Máy local Ubuntu/CentOS với MinIO hoặc container Docker `minio/minio`.<br>- **Đề mục**:<br>  1. **Thiết lập server**: Cài đặt MinIO server và tạo bucket `images`, `orders`, `logs`.<br>  2. **Quản lý user**: Tạo user `app_user` với quyền read/write trên `images`.<br>  3. **Versioning**: Kích hoạt versioning trên bucket `images`.<br>  4. **Sao lưu**: Sao lưu bucket `images` sang bucket `images_backup`.<br>  5. **Bảo mật**: Kích hoạt TLS và SSE cho bucket `orders`.<br>  6. **Giám sát**: Cấu hình Prometheus endpoint và alert cho storage usage.<br>  7. **Tài liệu**: Cung cấp README.md với cấu hình, policy, và quy trình sao lưu.<br>**Guideline**:<br>- Sử dụng `mc` client hoặc MinIO Console để quản lý bucket.<br>- Đảm bảo bucket hỗ trợ ứng dụng e-commerce (lưu trữ hình ảnh, đơn hàng).<br>- Kiểm tra quyền user để đảm bảo chỉ truy cập dữ liệu cần thiết.<br>- Tài liệu hóa rõ ràng, bao gồm sơ đồ bucket và hướng dẫn tái tạo.<br>- Kiểm tra metrics Prometheus để đảm bảo hiệu suất.<br>- Đảm bảo backup có thể khôi phục thành công. |
| **MCQ** | Bài kiểm tra trắc nghiệm về các tác vụ vận hành MinIO. | 2 giờ | [MinIO Documentation](https://docs.min.io/) | Tạo và trả lời 20 câu hỏi trắc nghiệm về kiến trúc, quản lý bucket, sao lưu, giám sát, tối ưu, và bảo mật. Sample MCQs:<br>1. MinIO là loại storage nào? (a) Object storage **(Đáp án: a)**<br>2. Lệnh nào tạo bucket? (a) mc mb **(Đáp án: a)**<br>3. Versioning dùng để làm gì? (a) Lưu trữ nhiều phiên bản object **(Đáp án: a)**<br>4. Metric nào đo storage usage? (a) minio_bucket_usage_total **(Đáp án: a)**<br>5. TLS dùng để làm gì? (a) Mã hóa kết nối **(Đáp án: a)** |

**Tổng thời gian**: 6 giờ

## Ghi Chú
- **Tổng thời gian**: 30 giờ (6 giờ/ngày).
- **Môi trường thực hành**: Máy local với MinIO hoặc container Docker, `mc` client, MinIO Console.
- **Tài liệu chính**: [MinIO Documentation](https://docs.min.io/).
- **Final Lab**: Dự án thực tế triển khai object storage cho e-commerce, tập trung vào vận hành.
- **Đánh giá**: MCQ và câu hỏi vấn đáp củng cố kiến thức; Final Lab kiểm tra khả năng áp dụng.[](https://min.io/product/multicloud-elastic-kubernetes-service)