# Lịch Trình Đào Tạo MariaDB (Tập Trung Vào Operation) Trong 5 Ngày

## Ngày 1: Giới Thiệu và Quản Lý Cơ Bản

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Giới thiệu MariaDB** | - Tổng quan về MariaDB: Relational database, vai trò trong DevOps.<br>- Kiến trúc: server, storage engines (InnoDB, MyISAM).<br>- Cài đặt và kết nối bằng `mysql` client. | 2 giờ | [MariaDB Documentation](https://mariadb.com/kb/en/documentation/) | 1. Cài đặt MariaDB trên Ubuntu/CentOS và kiểm tra phiên bản bằng `mysql --version`.<br>2. Kết nối đến MariaDB bằng `mysql` client với user `root`.<br>3. Kiểm tra storage engine mặc định bằng `SHOW ENGINES`. |
| **Quản lý Server** | - Khởi động, dừng, và kiểm tra trạng thái (`systemctl`, `mysqladmin`).<br>- Cấu hình `my.cnf` (bind-address, port).<br>- Tự động khởi động MariaDB. | 2 giờ | [MariaDB Server Administration](https://mariadb.com/kb/en/administration/) | 1. Khởi động và dừng MariaDB bằng `systemctl start mariadb` và `systemctl stop mariadb`.<br>2. Thay đổi `bind-address` trong `my.cnf` để cho phép remote access.<br>3. Kích hoạt tự khởi động bằng `systemctl enable mariadb`. |
| **Quản lý Người Dùng và Database** | - Tạo database, user, và quyền (`GRANT`, `REVOKE`).<br>- Kết nối bằng `mysql` client hoặc phpMyAdmin.<br>- Quản lý schema cơ bản. | 2 giờ | [MariaDB User Management](https://mariadb.com/kb/en/user-and-privilege-management/) | 1. Tạo database `ecommerce` và user `app_user` với mật khẩu.<br>2. Gán quyền `SELECT`, `INSERT` cho `app_user` trên `ecommerce`.<br>3. Kết nối đến `ecommerce` bằng `mysql` client và phpMyAdmin. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. MariaDB là loại cơ sở dữ liệu nào?  
   a) NoSQL  
   b) Relational  
   c) Graph  
   d) Document  
   **Đáp án**: b
2. Storage engine mặc định của MariaDB là gì?  
   a) MyISAM  
   b) InnoDB  
   c) Aria  
   d) TokuDB  
   **Đáp án**: b
3. Lệnh nào tạo database trong MariaDB?  
   a) CREATE DATABASE  
   b) MAKE DATABASE  
   c) NEW DATABASE  
   d) ADD DATABASE  
   **Đáp án**: a
4. File cấu hình chính của MariaDB là gì?  
   a) my.cnf  
   b) mariadb.conf  
   c) config.ini  
   d) db.conf  
   **Đáp án**: a
5. Lệnh nào kiểm tra trạng thái MariaDB server?  
   a) systemctl status mariadb  
   b) mysqladmin status  
   c) Cả hai  
   d) mysql status  
   **Đáp án**: c
6. Lệnh nào tạo user mới trong MariaDB?  
   a) CREATE USER  
   b) ADD USER  
   c) NEW USER  
   d) MAKE USER  
   **Đáp án**: a
7. `bind-address` trong `my.cnf` dùng để làm gì?  
   a) Cấu hình IP server lắng nghe  
   b) Cấu hình port  
   c) Cấu hình logging  
   d) Cấu hình backup  
   **Đáp án**: a
8. Lệnh nào gán quyền `SELECT` cho user?  
   a) GRANT SELECT  
   b) ALLOW SELECT  
   c) PERMIT SELECT  
   d) ASSIGN SELECT  
   **Đáp án**: a
9. Công cụ nào dùng để quản lý MariaDB qua GUI?  
   a) phpMyAdmin  
   b) mysql  
   c) mariadb-admin  
   d) innodb  
   **Đáp án**: a
10. Lệnh nào kiểm tra storage engines?  
    a) SHOW ENGINES  
    b) SHOW DATABASES  
    c) SHOW TABLES  
    d) SHOW STATUS  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao MariaDB được sử dụng trong DevOps?
2. Mô tả các thành phần chính trong kiến trúc MariaDB.
3. Làm thế nào để cấu hình MariaDB tự khởi động?
4. Giải thích cách gán quyền cho user trong MariaDB.
5. Sự khác biệt giữa InnoDB và MyISAM là gì?

## Ngày 2: Sao Lưu, Khôi Phục và Giám Sát

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Sao Lưu và Khôi Phục** | - Sử dụng `mysqldump` cho logical backup.<br>- Physical backup với `mariabackup`.<br>- Quy trình khôi phục database. | 2.5 giờ | [MariaDB Backup](https://mariadb.com/kb/en/backup-and-restore/) | 1. Sao lưu database `ecommerce` bằng `mysqldump` vào file `ecommerce.sql`.<br>2. Khôi phục `ecommerce.sql` vào database mới `ecommerce_restore`.<br>3. Thực hiện physical backup bằng `mariabackup` và kiểm tra file backup. |
| **Giám Sát MariaDB** | - Sử dụng `SHOW STATUS`, `INFORMATION_SCHEMA`.<br>- Cấu hình logging (`slow_query_log`).<br>- Phân tích log để phát hiện vấn đề. | 2.5 giờ | [MariaDB Monitoring](https://mariadb.com/kb/en/monitoring/) | 1. Kiểm tra trạng thái server bằng `SHOW GLOBAL STATUS`.<br>2. Kích hoạt `slow_query_log` và tạo truy vấn chậm để kiểm tra log.<br>3. Sử dụng `INFORMATION_SCHEMA` để xem thông tin bảng. |
| **Quản Lý Log** | - Cấu hình log rotation với `logrotate`.<br>- Xem và phân tích log file.<br>- Best practices cho logging. | 1 giờ | [MariaDB Logging](https://mariadb.com/kb/en/error-log/) | 1. Cấu hình log rotation cho MariaDB log bằng `logrotate`.<br>2. Kiểm tra slow query log để xác định truy vấn chậm.<br>3. Thay đổi `log_error` để ghi log vào file tùy chỉnh. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Công cụ nào dùng để sao lưu logical trong MariaDB?  
   a) mysqldump  
   b) mariabackup  
   c) mysqladmin  
   d) mysql  
   **Đáp án**: a
2. Lệnh nào khôi phục database từ file backup?  
   a) mysql < file.sql  
   b) mysqldump  
   c) mariabackup  
   d) mysqladmin  
   **Đáp án**: a
3. `mariabackup` dùng để làm gì?  
   a) Physical backup  
   b) Logical backup  
   c) Monitoring  
   d) Indexing  
   **Đáp án**: a
4. `slow_query_log` làm gì?  
   a) Ghi lại truy vấn chậm  
   b) Ghi lại lỗi server  
   c) Ghi lại kết nối  
   d) Ghi lại backup  
   **Đáp án**: a
5. Lệnh nào kiểm tra trạng thái server?  
   a) SHOW GLOBAL STATUS  
   b) SHOW DATABASES  
   c) SHOW TABLES  
   d) SHOW LOGS  
   **Đáp án**: a
6. Log rotation trong MariaDB được cấu hình bằng gì?  
   a) logrotate  
   b) mysqladmin  
   c) cron  
   d) mysqldump  
   **Đáp án**: a
7. `INFORMATION_SCHEMA` cung cấp thông tin gì?  
   a) Metadata của database  
   b) Log server  
   c) Backup status  
   d) Truy vấn chậm  
   **Đáp án**: a
8. Lệnh nào kích hoạt `slow_query_log`?  
   a) SET GLOBAL slow_query_log = 'ON'  
   b) SET GLOBAL log = 'ON'  
   c) SET GLOBAL error_log = 'ON'  
   d) SET GLOBAL query_log = 'ON'  
   **Đáp án**: a
9. File log MariaDB thường nằm ở đâu?  
   a) /var/log/mariadb  
   b) Data directory  
   c) Cả hai  
   d) /etc/mariadb  
   **Đáp án**: c
10. Best practice khi sao lưu MariaDB là gì?  
    a) Sử dụng cả logical và physical backup  
    b) Chỉ dùng mysqldump  
    c) Tắt logging  
    d) Không dùng mariabackup  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao sao lưu và khôi phục quan trọng trong vận hành MariaDB?
2. Mô tả quy trình sao lưu bằng `mysqldump` và khôi phục.
3. Làm thế nào để phát hiện truy vấn chậm trong MariaDB?
4. Giải thích cách cấu hình log rotation cho MariaDB.
5. Các best practice khi giám sát MariaDB là gì?

## Ngày 3: Tối Ưu Hiệu Suất

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Indexing** | - Index là gì? Các loại index (B-tree, Full-text).<br>- Khi nào nên tạo index.<br>- Bảo trì index. | 2 giờ | [MariaDB Indexes](https://mariadb.com/kb/en/indexes/) | 1. Tạo B-tree index trên cột `customer_id` của bảng `orders`.<br>2. So sánh hiệu suất truy vấn với và không có index bằng `EXPLAIN`.<br>3. Thực hiện `OPTIMIZE TABLE` để bảo trì index. |
| **Query Optimization** | - Sử dụng `EXPLAIN`, `ANALYZE` để phân tích query plan.<br>- Viết lại truy vấn để tối ưu hiệu suất.<br>- Tác động của thống kê đến query planner. | 2 giờ | [MariaDB Query Optimization](https://mariadb.com/kb/en/optimization-and-tuning/) | 1. Sử dụng `EXPLAIN` để phân tích truy vấn `SELECT` phức tạp.<br>2. Viết lại truy vấn sử dụng JOIN thay vì subquery và so sánh hiệu suất.<br>3. Chạy `ANALYZE TABLE` và kiểm tra thay đổi trong query plan. |
| **Cấu Hình Server** | - Các tham số: `innodb_buffer_pool_size`, `query_cache_size`.<br>- Tối ưu hóa hiệu suất server.<br>- Quản lý connection pool. | 2 giờ | [MariaDB Server Configuration](https://mariadb.com/kb/en/configuring-mariadb/) | 1. Thay đổi `innodb_buffer_pool_size` trong `my.cnf` và khởi động lại server.<br>2. Cấu hình `query_cache_size` để cải thiện hiệu suất truy vấn.<br>3. Kiểm tra số kết nối bằng `SHOW STATUS LIKE 'Threads_connected'`. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Index nào là mặc định trong MariaDB?  
   a) B-tree  
   b) Full-text  
   c) Hash  
   d) Spatial  
   **Đáp án**: a
2. Lệnh nào phân tích query plan trong MariaDB?  
   a) EXPLAIN  
   b) ANALYZE  
   c) OPTIMIZE  
   d) CHECK  
   **Đáp án**: a
3. `ANALYZE TABLE` làm gì?  
   a) Cập nhật thống kê bảng  
   b) Tạo index  
   c) Sao lưu database  
   d) Giám sát server  
   **Đáp án**: a
4. Tham số nào ảnh hưởng đến bộ nhớ cho InnoDB?  
   a) innodb_buffer_pool_size  
   b) query_cache_size  
   c) max_connections  
   d) tmp_table_size  
   **Đáp án**: a
5. Khi nào nên tạo index?  
   a) Cột thường xuyên truy vấn  
   b) Cột hiếm khi truy vấn  
   c) Cột không có dữ liệu  
   d) Cột chỉ có NULL  
   **Đáp án**: a
6. Lệnh nào tối ưu hóa bảng?  
   a) OPTIMIZE TABLE  
   b) ANALYZE TABLE  
   c) CHECK TABLE  
   d) REPAIR TABLE  
   **Đáp án**: a
7. `query_cache_size` dùng để làm gì?  
   a) Lưu trữ kết quả truy vấn  
   b) Lưu trữ log  
   c) Quản lý kết nối  
   d) Tạo backup  
   **Đáp án**: a
8. Lệnh nào kiểm tra số kết nối hiện tại?  
   a) SHOW STATUS LIKE 'Threads_connected'  
   b) SHOW DATABASES  
   c) SHOW TABLES  
   d) SHOW LOGS  
   **Đáp án**: a
9. Lệnh nào phân tích hiệu suất truy vấn thực tế?  
   a) EXPLAIN ANALYZE  
   b) EXPLAIN  
   c) ANALYZE TABLE  
   d) OPTIMIZE TABLE  
   **Đáp án**: a
10. Tham số nào tối ưu hóa kết nối?  
    a) max_connections  
    b) innodb_buffer_pool_size  
    c) query_cache_size  
    d) tmp_table_size  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao index quan trọng trong tối ưu hóa MariaDB?
2. Mô tả cách sử dụng `EXPLAIN` để phân tích truy vấn.
3. Làm thế nào để xác định cột cần index?
4. Giải thích vai trò của `innodb_buffer_pool_size` trong hiệu suất MariaDB.
5. Các best practice khi tối ưu hóa truy vấn trong MariaDB là gì?

## Ngày 4: Bảo Mật và Bảo Trì

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Bảo Mật MariaDB** | - Kích hoạt SSL/TLS cho kết nối an toàn.<br>- Row-level privileges.<br>- Cấu hình `mysql.user` và host-based access. | 2.5 giờ | [MariaDB Security](https://mariadb.com/kb/en/security/) | 1. Kích hoạt SSL trong `my.cnf` và kiểm tra kết nối bằng `mysql --ssl`.<br>2. Tạo privilege row-level cho bảng `orders`.<br>3. Cấu hình `mysql.user` để chỉ cho phép kết nối từ `localhost`. |
| **Bảo Trì Database** | - Optimize và repair table.<br>- Quản lý bloat với `OPTIMIZE TABLE`.<br>- Nâng cấp MariaDB. | 2.5 giờ | [MariaDB Maintenance](https://mariadb.com/kb/en/maintenance/) | 1. Chạy `OPTIMIZE TABLE` trên bảng `orders`.<br>2. Lên lịch `OPTIMIZE TABLE` tự động bằng `cron`.<br>3. Mô phỏng nâng cấp MariaDB bằng gói mới (hoặc đọc tài liệu). |
| **Quản Lý Lỗi** | - Xử lý lỗi phổ biến (deadlock, connection issues).<br>- Phân tích log để debug.<br>- Best practices cho xử lý lỗi. | 1 giờ | [MariaDB Error Handling](https://mariadb.com/kb/en/error-handling/) | 1. Tạo tình huống deadlock và kiểm tra log để xác định nguyên nhân.<br>2. Kiểm tra lỗi kết nối bằng cách sửa sai host và khắc phục.<br>3. Kích hoạt `log_warnings` để ghi lại thông tin lỗi chi tiết. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. File nào lưu thông tin user trong MariaDB?  
   a) mysql.user  
   b) my.cnf  
   c) mariadb.conf  
   d) error.log  
   **Đáp án**: a
2. Lệnh nào kích hoạt SSL trong MariaDB?  
   a) ssl = ON  
   b) ssl_enabled = TRUE  
   c) secure = ON  
   d) tls = TRUE  
   **Đáp án**: a
3. Row-level privileges làm gì?  
   a) Hạn chế truy cập theo hàng  
   b) Hạn chế truy cập theo cột  
   c) Tạo index  
   d) Sao lưu database  
   **Đáp án**: a
4. Lệnh nào tối ưu hóa bảng trong MariaDB?  
   a) OPTIMIZE TABLE  
   b) ANALYZE TABLE  
   c) CHECK TABLE  
   d) REPAIR TABLE  
   **Đáp án**: a
5. Lệnh nào sửa chữa bảng bị lỗi?  
   a) REPAIR TABLE  
   b) OPTIMIZE TABLE  
   c) ANALYZE TABLE  
   d) CHECK TABLE  
   **Đáp án**: a
6. Deadlock trong MariaDB là gì?  
   a) Hai giao dịch khóa lẫn nhau  
   b) Lỗi kết nối  
   c) Lỗi index  
   d) Lỗi backup  
   **Đáp án**: a
7. Tham số nào ghi lại thông tin lỗi chi tiết?  
   a) log_warnings  
   b) slow_query_log  
   c) log_error  
   d) general_log  
   **Đáp án**: a
8. Lệnh nào kiểm tra bảng bị lỗi?  
   a) CHECK TABLE  
   b) OPTIMIZE TABLE  
   c) ANALYZE TABLE  
   d) REPAIR TABLE  
   **Đáp án**: a
9. Host-based access được cấu hình ở đâu?  
   a) mysql.user  
   b) my.cnf  
   c) error.log  
   d) mariadb.conf  
   **Đáp án**: a
10. Best practice khi nâng cấp MariaDB là gì?  
    a) Sao lưu trước khi nâng cấp  
    b) Tắt logging  
    c) Không dùng SSL  
    d) Xóa index  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao cần SSL trong MariaDB? Làm thế nào để kích hoạt?
2. Mô tả cách sử dụng row-level privileges trong MariaDB.
3. Làm thế nào để phát hiện và xử lý deadlock trong MariaDB?
4. Giải thích vai trò của `OPTIMIZE TABLE` trong bảo trì.
5. Các best practice khi cấu hình bảo mật MariaDB là gì?

## Ngày 5: Final Lab và Đánh Giá

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Final Lab** | Triển khai MariaDB cho ứng dụng e-commerce, với quản lý người dùng, indexing, sao lưu, bảo mật, và tối ưu hiệu suất. | 4 giờ | [MariaDB Documentation](https://mariadb.com/kb/en/documentation/) | **Mô tả**: Thiết lập database MariaDB cho ứng dụng e-commerce với các bảng `customers`, `products`, `orders`, `order_items`, đảm bảo quản lý người dùng, hiệu suất, bảo mật, và sao lưu.<br>**Yêu cầu**:<br>- **Môi trường**: Máy local Ubuntu/CentOS với MariaDB hoặc container Docker `mariadb`.<br>- **Đề mục**:<br>  1. **Thiết kế database**: Tạo các bảng với data types, primary key, foreign key, và constraints.<br>  2. **Quản lý người dùng**: Tạo user `admin`, `sales`, `support` với quyền phù hợp.<br>  3. **Indexing**: Tạo index trên các cột thường xuyên truy vấn (ví dụ: `customer_id`).<br>  4. **Sao lưu**: Lên lịch sao lưu hàng ngày bằng `mysqldump` và kiểm tra khôi phục.<br>  5. **Tối ưu hiệu suất**: Sử dụng `EXPLAIN` để tối ưu truy vấn mẫu.<br>  6. **Bảo mật**: Cấu hình SSL và giới hạn truy cập từ `localhost`.<br>  7. **Tài liệu**: Cung cấp README.md với schema, quyền, quy trình sao lưu, và tối ưu hóa.<br>**Guideline**:<br>- Sử dụng `mysql` client hoặc phpMyAdmin để quản lý database.<br>- Đảm bảo schema hỗ trợ ứng dụng e-commerce.<br>- Kiểm tra quyền user để đảm bảo chỉ truy cập dữ liệu cần thiết.<br>- Tài liệu hóa rõ ràng, bao gồm sơ đồ schema và hướng dẫn tái tạo.<br>- Kiểm tra hiệu suất truy vấn bằng `EXPLAIN ANALYZE`.<br>- Đảm bảo backup có thể khôi phục thành công. |
| **MCQ** | Bài kiểm tra trắc nghiệm về các tác vụ vận hành MariaDB. | 2 giờ | [MariaDB Documentation](https://mariadb.com/kb/en/documentation/) | Tạo và trả lời 20 câu hỏi trắc nghiệm về kiến trúc, quản lý server, sao lưu, giám sát, tối ưu, và bảo mật. Sample MCQs:<br>1. MariaDB là loại database nào? (a) Relational **(Đáp án: a)**<br>2. Lệnh nào sao lưu database? (a) mysqldump **(Đáp án: a)**<br>3. `EXPLAIN ANALYZE` làm gì? (a) Phân tích hiệu suất truy vấn **(Đáp án: a)**<br>4. File nào cấu hình quyền truy cập? (a) mysql.user **(Đáp án: a)**<br>5. `OPTIMIZE TABLE` dùng để làm gì? (a) Tối ưu hóa bảng **(Đáp án: a)** |

**Tổng thời gian**: 6 giờ

## Ghi Chú
- **Tổng thời gian**: 30 giờ (6 giờ/ngày).
- **Môi trường thực hành**: Máy local với MariaDB hoặc container Docker, `mysql` client, phpMyAdmin.
- **Tài liệu chính**: [MariaDB Documentation](https://mariadb.com/kb/en/documentation/).
- **Final Lab**: Dự án thực tế triển khai database cho e-commerce, tập trung vào vận hành.
- **Đánh giá**: MCQ và câu hỏi vấn đáp củng cố kiến thức; Final Lab kiểm tra khả năng áp dụng.