# Lịch Trình Đào Tạo PostgreSQL (Tập Trung Vào Operation) Trong 5 Ngày

## Ngày 1: Giới Thiệu và Quản Lý Cơ Bản

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Kiến trúc PostgreSQL** | - Tổng quan về PostgreSQL: lịch sử, tính năng, vai trò trong DevOps.<br>- Kiến trúc: server, client, data directory, WAL.<br>- Các thành phần chính: `psql`, `pgAdmin`, `pg_ctl`. | 2 giờ | [PostgreSQL Architecture](https://www.postgresql.org/docs/current/runtime-architecture.html) | 1. Cài đặt PostgreSQL trên Ubuntu/CentOS và kiểm tra phiên bản bằng `psql --version`.<br>2. Kiểm tra data directory bằng `SHOW data_directory` trong `psql`.<br>3. Sử dụng `pg_controldata` để xem thông tin control data của PostgreSQL instance. |
| **Quản lý Server** | - Khởi động, dừng, và kiểm tra trạng thái server (`pg_ctl`, `systemctl`).<br>- Cấu hình cơ bản trong `postgresql.conf` và `pg_hba.conf`.<br>- Tự động khởi động PostgreSQL khi boot. | 2 giờ | [PostgreSQL Server Operation](https://www.postgresql.org/docs/current/server-operation.html) | 1. Khởi động và dừng PostgreSQL bằng `pg_ctl start` và `pg_ctl stop`.<br>2. Kích hoạt PostgreSQL tự khởi động bằng `systemctl enable postgresql`.<br>3. Sửa đổi `postgresql.conf` để thay đổi `listen_addresses` và kiểm tra kết nối. |
| **Quản lý Người Dùng và Cơ Sở Dữ Liệu** | - Tạo và quản lý database, user, role.<br>- Gán quyền (`GRANT`, `REVOKE`).<br>- Kết nối với database bằng `psql` và `pgAdmin`. | 2 giờ | [PostgreSQL Managing Databases](https://www.postgresql.org/docs/current/manage-ag-createdb.html) | 1. Tạo database `mydb` và user `myuser` với mật khẩu `mypassword`.<br>2. Gán quyền `SELECT`, `INSERT` cho `myuser` trên bảng trong `mydb`.<br>3. Kết nối đến `mydb` bằng `psql` và `pgAdmin` với `myuser`. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Port mặc định của PostgreSQL là gì?  
   a) 3306  
   b) 5432  
   c) 1521  
   d) 5433  
   **Đáp án**: b
2. Lệnh nào tạo database mới trong PostgreSQL?  
   a) CREATE DATABASE  
   b) MAKE DATABASE  
   c) NEW DATABASE  
   d) ADD DATABASE  
   **Đáp án**: a
3. Công cụ nào dùng để kết nối PostgreSQL qua CLI?  
   a) pgAdmin  
   b) psql  
   c) pg_ctl  
   d) pg_dump  
   **Đáp án**: b
4. File nào cấu hình quyền truy cập trong PostgreSQL?  
   a) postgresql.conf  
   b) pg_hba.conf  
   c) recovery.conf  
   d) pg_log.conf  
   **Đáp án**: b
5. Lệnh nào kiểm tra trạng thái PostgreSQL server?  
   a) pg_ctl status  
   b) psql status  
   c) systemctl status postgresql  
   d) Cả a và c  
   **Đáp án**: d
6. Lệnh nào tạo user mới trong PostgreSQL?  
   a) CREATE USER  
   b) ADD USER  
   c) NEW USER  
   d) MAKE USER  
   **Đáp án**: a
7. `listen_addresses` trong `postgresql.conf` dùng để làm gì?  
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
9. `pg_controldata` hiển thị thông tin gì?  
   a) Trạng thái kết nối  
   b) Control data của PostgreSQL instance  
   c) Log server  
   d) Backup status  
   **Đáp án**: b
10. Lệnh nào dừng PostgreSQL server?  
    a) pg_ctl stop  
    b) systemctl stop postgresql  
    c) Cả a và b  
    d) psql stop  
    **Đáp án**: c

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao PostgreSQL được sử dụng phổ biến trong DevOps?
2. Mô tả các thành phần chính trong kiến trúc PostgreSQL.
3. Làm thế nào để cấu hình PostgreSQL tự khởi động khi boot?
4. Giải thích cách gán quyền cho user trong PostgreSQL.
5. Sự khác biệt giữa `postgresql.conf` và `pg_hba.conf` là gì?

## Ngày 2: Sao Lưu, Khôi Phục và Giám Sát

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Sao Lưu và Khôi Phục** | - Các loại sao lưu: full, incremental.<br>- Sử dụng `pg_dump`, `pg_dumpall`, `pg_basebackup`.<br>- Quy trình khôi phục từ backup. | 2.5 giờ | [PostgreSQL Backup and Restore](https://www.postgresql.org/docs/current/backup.html) | 1. Sử dụng `pg_dump` để sao lưu database `mydb` vào file `mydb_backup.sql`.<br>2. Khôi phục `mydb_backup.sql` vào database mới `mydb_restore`.<br>3. Thực hiện sao lưu toàn bộ cluster bằng `pg_dumpall` và kiểm tra file backup. |
| **Giám Sát Cơ Sở Dữ Liệu** | - Sử dụng `pg_stat_activity`, `pg_stat_user_tables`.<br>- Cấu hình logging trong `postgresql.conf`.<br>- Phân tích log để phát hiện vấn đề. | 2.5 giờ | [PostgreSQL Monitoring](https://www.postgresql.org/docs/current/monitoring-stats.html) | 1. Xem hoạt động hiện tại bằng `SELECT * FROM pg_stat_activity`.<br>2. Cấu hình logging để ghi lại các truy vấn chậm (`log_min_duration_statement`).<br>3. Kiểm tra log file PostgreSQL để phân tích lỗi hoặc truy vấn. |
| **Quản Lý Log** | - Cấu hình log rotation.<br>- Xem và phân tích log file.<br>- Best practices cho logging. | 1 giờ | [PostgreSQL Logging](https://www.postgresql.org/docs/current/runtime-config-logging.html) | 1. Cấu hình log rotation bằng `logrotate` cho PostgreSQL log.<br>2. Tạo truy vấn chậm và kiểm tra log để xác định vấn đề.<br>3. Thay đổi `log_destination` trong `postgresql.conf` để ghi log vào `csvlog`. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Công cụ nào dùng để sao lưu một database trong PostgreSQL?  
   a) pg_dump  
   b) pg_ctl  
   c) psql  
   d) pg_stat  
   **Đáp án**: a
2. Lệnh nào sao lưu toàn bộ cluster PostgreSQL?  
   a) pg_dumpall  
   b) pg_dump  
   c) pg_basebackup  
   d) Cả a và c  
   **Đáp án**: d
3. Lệnh nào khôi phục database từ file backup?  
   a) psql -f  
   b) pg_restore  
   c) Cả a và b  
   d) pg_dump  
   **Đáp án**: c
4. `pg_stat_activity` hiển thị thông tin gì?  
   a) Hoạt động hiện tại của server  
   b) Thống kê bảng  
   c) Log file  
   d) Backup status  
   **Đáp án**: a
5. Tham số nào cấu hình ghi lại truy vấn chậm?  
   a) log_min_duration_statement  
   b) log_destination  
   c) log_rotation_age  
   d) log_level  
   **Đáp án**: a
6. Lệnh nào kiểm tra thống kê bảng người dùng?  
   a) SELECT * FROM pg_stat_user_tables  
   b) SELECT * FROM pg_stat_activity  
   c) SELECT * FROM pg_log  
   d) SELECT * FROM pg_backup  
   **Đáp án**: a
7. Log rotation trong PostgreSQL được cấu hình bằng công cụ nào?  
   a) logrotate  
   b) pg_log  
   c) cron  
   d) psql  
   **Đáp án**: a
8. `pg_basebackup` dùng để làm gì?  
   a) Sao lưu toàn bộ cluster  
   b) Sao lưu một database  
   c) Khôi phục database  
   d) Giám sát server  
   **Đáp án**: a
9. File log PostgreSQL thường nằm ở đâu?  
   a) Data directory  
   b) /var/log/postgresql  
   c) Cả hai  
   d) /etc/postgresql  
   **Đáp án**: c
10. Tham số nào thay đổi định dạng log?  
    a) log_destination  
    b) log_min_duration_statement  
    c) log_rotation_age  
    d) log_level  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao sao lưu và khôi phục quan trọng trong vận hành PostgreSQL?
2. Mô tả quy trình sao lưu và khôi phục bằng `pg_dump`.
3. Làm thế nào để phát hiện truy vấn chậm bằng log PostgreSQL?
4. Giải thích cách cấu hình log rotation cho PostgreSQL.
5. Các best practice khi giám sát PostgreSQL là gì?

## Ngày 3: Tối Ưu Hiệu Suất

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Indexing** | - Index là gì? Các loại index (B-tree, GIN, GiST).<br>- Khi nào nên tạo index.<br>- Bảo trì index. | 2 giờ | [PostgreSQL Indexes](https://www.postgresql.org/docs/current/indexes.html) | 1. Tạo B-tree index trên cột thường xuyên truy vấn trong bảng `employees`.<br>2. So sánh hiệu suất truy vấn với và không có index bằng `EXPLAIN`.<br>3. Thực hiện `REINDEX` trên một bảng và kiểm tra hiệu quả. |
| **Query Optimization** | - Sử dụng `EXPLAIN`, `ANALYZE` để phân tích query plan.<br>- Viết lại truy vấn để tối ưu hiệu suất.<br>- Tác động của thống kê đến query planner. | 2 giờ | [PostgreSQL Query Planning](https://www.postgresql.org/docs/current/using-explain.html) | 1. Sử dụng `EXPLAIN` để phân tích truy vấn `SELECT` phức tạp.<br>2. Viết lại truy vấn sử dụng JOIN thay vì subquery và so sánh hiệu suất.<br>3. Chạy `ANALYZE` trên bảng và kiểm tra thay đổi trong query plan. |
| **Cấu Hình Server** | - Các tham số quan trọng: `shared_buffers`, `work_mem`, `maintenance_work_mem`.<br>- Autovacuum và tuning.<br>- Tối ưu hóa hiệu suất server. | 2 giờ | [PostgreSQL Runtime Configuration](https://www.postgresql.org/docs/current/runtime-config.html) | 1. Thay đổi `shared_buffers` trong `postgresql.conf` và khởi động lại server.<br>2. Cấu hình `work_mem` để cải thiện hiệu suất truy vấn phức tạp.<br>3. Kích hoạt autovacuum và kiểm tra log autovacuum. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Index nào là mặc định trong PostgreSQL?  
   a) B-tree  
   b) GIN  
   c) GiST  
   d) Hash  
   **Đáp án**: a
2. Lệnh nào phân tích query plan?  
   a) EXPLAIN  
   b) ANALYZE  
   c) REINDEX  
   d) VACUUM  
   **Đáp án**: a
3. `ANALYZE` làm gì trong PostgreSQL?  
   a) Cập nhật thống kê bảng  
   b) Tạo index  
   c) Sao lưu database  
   d) Giám sát server  
   **Đáp án**: a
4. Tham số nào ảnh hưởng đến bộ nhớ cho truy vấn?  
   a) work_mem  
   b) shared_buffers  
   c) maintenance_work_mem  
   d) max_connections  
   **Đáp án**: a
5. Khi nào nên tạo index?  
   a) Cột thường xuyên truy vấn  
   b) Cột hiếm khi truy vấn  
   c) Cột không có dữ liệu  
   d) Cột chỉ có giá trị NULL  
   **Đáp án**: a
6. Lệnh nào tái tạo index?  
   a) REINDEX  
   b) ANALYZE  
   c) VACUUM  
   d) EXPLAIN  
   **Đáp án**: a
7. `shared_buffers` dùng để làm gì?  
   a) Lưu trữ dữ liệu tạm thời trong RAM  
   b) Cấu hình logging  
   c) Quản lý kết nối  
   d) Tạo backup  
   **Đáp án**: a
8. Autovacuum làm gì?  
   a) Dọn dẹp dữ liệu cũ và cập nhật thống kê  
   b) Tạo index  
   c) Sao lưu database  
   d) Giám sát server  
   **Đáp án**: a
9. Lệnh nào kiểm tra hiệu suất truy vấn thực tế?  
   a) EXPLAIN ANALYZE  
   b) EXPLAIN  
   c) ANALYZE  
   d) REINDEX  
   **Đáp án**: a
10. Tham số nào tối ưu hóa bảo trì database?  
    a) maintenance_work_mem  
    b) work_mem  
    c) shared_buffers  
    d) max_connections  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao index quan trọng trong tối ưu hóa PostgreSQL?
2. Mô tả cách sử dụng `EXPLAIN` để phân tích truy vấn.
3. Làm thế nào để xác định cột cần index?
4. Giải thích vai trò của `shared_buffers` trong hiệu suất PostgreSQL.
5. Autovacuum giúp cải thiện hiệu suất database như thế nào?

## Ngày 4: Bảo Mật và Bảo Trì Cơ Sở Dữ Liệu

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Bảo Mật PostgreSQL** | - Cấu hình SSL/TLS cho kết nối an toàn.<br>- Row-level security.<br>- Quản lý quyền truy cập qua `pg_hba.conf`. | 2.5 giờ | [PostgreSQL Security](https://www.postgresql.org/docs/current/security.html) | 1. Kích hoạt SSL trong `postgresql.conf` và kiểm tra kết nối bằng `psql`.<br>2. Tạo policy row-level security cho bảng `employees`.<br>3. Sửa `pg_hba.conf` để chỉ cho phép kết nối từ IP cụ thể (ví dụ: 127.0.0.1). |
| **Bảo Trì Cơ Sở Dữ Liệu** | - Vacuuming và analyzing.<br>- Reindexing và quản lý bloat.<br>- Nâng cấp PostgreSQL. | 2.5 giờ | [PostgreSQL Routine Database Maintenance](https://www.postgresql.org/docs/current/routine-vacuuming.html) | 1. Chạy `VACUUM FULL` và `ANALYZE` trên bảng `employees`.<br>2. Lên lịch vacuum tự động bằng `cron`.<br>3. Mô phỏng nâng cấp PostgreSQL bằng `pg_upgrade` (hoặc đọc tài liệu). |
| **Quản Lý Lỗi** | - Xử lý lỗi phổ biến (deadlock, connection issues).<br>- Phân tích log để debug.<br>- Best practices cho xử lý lỗi. | 1 giờ | [PostgreSQL Error Reporting](https://www.postgresql.org/docs/current/error-reporting-and-logging.html) | 1. Tạo tình huống deadlock và kiểm tra log để xác định nguyên nhân.<br>2. Kiểm tra lỗi kết nối bằng cách sửa sai `pg_hba.conf` và khắc phục.<br>3. Cấu hình `log_connections` để ghi lại thông tin kết nối. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. File nào cấu hình quyền truy cập trong PostgreSQL?  
   a) pg_hba.conf  
   b) postgresql.conf  
   c) recovery.conf  
   d) log.conf  
   **Đáp án**: a
2. Lệnh nào kích hoạt SSL trong PostgreSQL?  
   a) ssl = on  
   b) ssl_enabled = true  
   c) secure = on  
   d) tls = true  
   **Đáp án**: a
3. Row-level security làm gì?  
   a) Hạn chế truy cập theo hàng  
   b) Hạn chế truy cập theo cột  
   c) Tạo index  
   d) Sao lưu database  
   **Đáp án**: a
4. Lệnh nào dọn dẹp dữ liệu cũ trong PostgreSQL?  
   a) VACUUM  
   b) ANALYZE  
   c) REINDEX  
   d) EXPLAIN  
   **Đáp án**: a
5. Lệnh nào nâng cấp PostgreSQL?  
   a) pg_upgrade  
   b) pg_dump  
   c) pg_restore  
   d) pg_ctl  
   **Đáp án**: a
6. Deadlock trong PostgreSQL là gì?  
   a) Hai giao dịch khóa lẫn nhau  
   b) Lỗi kết nối  
   c) Lỗi index  
   d) Lỗi backup  
   **Đáp án**: a
7. Tham số nào ghi lại thông tin kết nối?  
   a) log_connections  
   b) log_min_duration_statement  
   c) log_destination  
   d) log_rotation_age  
   **Đáp án**: a
8. Lệnh nào phân tích thống kê bảng?  
   a) ANALYZE  
   b) VACUUM  
   c) REINDEX  
   d) EXPLAIN  
   **Đáp án**: a
9. `pg_hba.conf` kiểm soát gì?  
   a) Quyền truy cập client  
   b) Hiệu suất server  
   c) Logging  
   d) Backup  
   **Đáp án**: a
10. Lệnh nào kiểm tra bloat trong bảng?  
    a) SELECT * FROM pg_stat_user_tables  
    b) SELECT * FROM pg_stat_activity  
    c) VACUUM  
    d) ANALYZE  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao cần SSL trong PostgreSQL? Làm thế nào để kích hoạt?
2. Mô tả cách sử dụng row-level security trong PostgreSQL.
3. Làm thế nào để phát hiện và xử lý deadlock trong PostgreSQL?
4. Giải thích vai trò của `VACUUM` trong bảo trì cơ sở dữ liệu.
5. Các best practice khi cấu hình `pg_hba.conf` là gì?

## Ngày 5: Final Lab và Đánh Giá

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Final Lab** | Triển khai cơ sở dữ liệu PostgreSQL cho ứng dụng e-commerce, với quản lý người dùng, indexing, sao lưu, bảo mật, và tối ưu hiệu suất. | 4 giờ | [PostgreSQL Documentation](https://www.postgresql.org/docs/current/) | **Mô tả**: Thiết lập cơ sở dữ liệu cho ứng dụng e-commerce với các bảng `customers`, `products`, `orders`, `order_items`, đảm bảo quản lý người dùng, hiệu suất, bảo mật, và sao lưu.<br>**Yêu cầu**:<br>- **Môi trường**: Máy local Ubuntu/CentOS với PostgreSQL hoặc container Docker `postgres`.<br>- **Đề mục**:<br>  1. **Thiết kế cơ sở dữ liệu**: Tạo các bảng với data types, primary key, foreign key, và constraints phù hợp.<br>  2. **Quản lý người dùng**: Tạo user `admin`, `sales`, `support` với quyền phù hợp (`SELECT`, `INSERT`, `UPDATE`).<br>  3. **Indexing**: Tạo index trên các cột thường xuyên truy vấn (ví dụ: `customer_id`, `product_name`).<br>  4. **Sao lưu và khôi phục**: Lên lịch sao lưu hàng ngày bằng `pg_dump` và kiểm tra khôi phục.<br>  5. **Tối ưu hiệu suất**: Sử dụng `EXPLAIN` để phân tích và tối ưu truy vấn mẫu (ví dụ: tìm đơn hàng theo khách hàng).<br>  6. **Bảo mật**: Cấu hình `pg_hba.conf` để giới hạn truy cập từ `localhost`, kích hoạt SSL.<br>  7. **Tài liệu**: Cung cấp README.md với schema, quyền user, quy trình sao lưu, và tối ưu hóa.<br>**Guideline**:<br>- Sử dụng `psql` hoặc `pgAdmin` để quản lý database.<br>- Đảm bảo schema hỗ trợ ứng dụng e-commerce (ví dụ: tìm kiếm sản phẩm, quản lý đơn hàng).<br>- Kiểm tra quyền user để đảm bảo chỉ truy cập dữ liệu cần thiết.<br>- Tài liệu hóa rõ ràng, bao gồm sơ đồ schema và hướng dẫn tái tạo.<br>- Kiểm tra hiệu suất truy vấn bằng `EXPLAIN ANALYZE`.<br>- Đảm bảo backup có thể khôi phục thành công. |
| **MCQ** | Bài kiểm tra trắc nghiệm về các tác vụ vận hành PostgreSQL. | 2 giờ | [PostgreSQL Documentation](https://www.postgresql.org/docs/current/) | Tạo và trả lời 20 câu hỏi trắc nghiệm về kiến trúc, quản lý server, sao lưu, giám sát, tối ưu, và bảo mật. Sample MCQs:<br>1. Port mặc định của PostgreSQL? (a) 5432 **(Đáp án: a)**<br>2. Lệnh nào sao lưu database? (a) pg_dump **(Đáp án: a)**<br>3. `EXPLAIN ANALYZE` làm gì? (a) Phân tích hiệu suất truy vấn **(Đáp án: a)**<br>4. File nào cấu hình quyền truy cập? (a) pg_hba.conf **(Đáp án: a)**<br>5. `VACUUM` dùng để làm gì? (a) Dọn dẹp dữ liệu cũ **(Đáp án: a)** |

**Tổng thời gian**: 6 giờ

## Ghi Chú
- **Tổng thời gian**: 30 giờ (6 giờ/ngày).
- **Môi trường thực hành**: Máy local với PostgreSQL hoặc container Docker, công cụ `psql`, `pgAdmin`.
- **Tài liệu chính**: [PostgreSQL Documentation](https://www.postgresql.org/docs/current/).
- **Final Lab**: Dự án thực tế triển khai cơ sở dữ liệu e-commerce, tập trung vào vận hành.
- **Đánh giá**: MCQ và câu hỏi vấn đáp củng cố kiến thức; Final Lab kiểm tra khả năng áp dụng.