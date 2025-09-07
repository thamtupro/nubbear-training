# Lịch Trình Đào Tạo Amazon DynamoDB (Tập Trung Vào Operation) Trong 5 Ngày

## Ngày 1: Giới Thiệu và Quản Lý Cơ Bản

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Giới thiệu DynamoDB** | - Tổng quan về DynamoDB: NoSQL, serverless, vai trò trong DevOps.<br>- Kiến trúc: table, item, attribute, partition key, sort key.<br>- Quản lý qua AWS CLI, AWS Console, hoặc SDK. | 2 giờ | [DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/) | 1. Tạo table `employees` với partition key `user_id` và sort key `username` bằng AWS CLI.<br>2. Kiểm tra cấu hình table bằng AWS Console.<br>3. Thêm 5 item vào table `employees` bằng AWS CLI hoặc SDK. |
| **Quản lý Table** | - Tạo, xóa, và cập nhật table.<br>- Cấu hình read/write capacity (on-demand vs. provisioned).<br>- Kết nối và truy vấn cơ bản. | 2 giờ | [DynamoDB Table Management](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html) | 1. Cập nhật table `employees` sang chế độ on-demand capacity.<br>2. Xóa table và tạo lại với provisioned capacity (5 RCU, 5 WCU).<br>3. Truy vấn item trong `employees` bằng `aws dynamodb query`. |
| **Quản lý IAM và Quyền Truy Cập** | - IAM policies cho DynamoDB.<br>- Gán quyền truy cập table/user.<br>- Kiểm tra quyền bằng AWS CLI. | 2 giờ | [DynamoDB IAM Policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security-iam.html) | 1. Tạo IAM role cho phép `dynamodb:PutItem` trên table `employees`.<br>2. Gán IAM policy cho user và kiểm tra quyền bằng AWS CLI.<br>3. Thử truy cập table với user không có quyền và phân tích lỗi. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. DynamoDB là loại cơ sở dữ liệu nào?  
   a) Relational  
   b) NoSQL  
   c) Graph  
   d) Document  
   **Đáp án**: b
2. Partition key trong DynamoDB dùng để làm gì?  
   a) Sắp xếp dữ liệu  
   b) Phân chia dữ liệu trên các node  
   c) Tạo index  
   d) Lưu trữ metadata  
   **Đáp án**: b
3. Lệnh nào tạo table trong DynamoDB?  
   a) aws dynamodb create-table  
   b) aws dynamodb make-table  
   c) aws dynamodb new-table  
   d) aws dynamodb add-table  
   **Đáp án**: a
4. Chế độ nào không yêu cầu cấu hình RCU/WCU?  
   a) Provisioned  
   b) On-demand  
   c) Global  
   d) Local  
   **Đáp án**: b
5. IAM role cần quyền nào để thêm item vào table?  
   a) dynamodb:PutItem  
   b) dynamodb:GetItem  
   c) dynamodb:Query  
   d) dynamodb:Scan  
   **Đáp án**: a
6. DynamoDB hỗ trợ truy vấn nào?  
   a) Query  
   b) Scan  
   c) Cả hai  
   d) Không hỗ trợ truy vấn  
   **Đáp án**: c
7. Sort key dùng để làm gì?  
   a) Phân chia dữ liệu  
   b) Sắp xếp item trong partition  
   c) Tạo index phụ  
   d) Lưu trữ metadata  
   **Đáp án**: b
8. Lệnh nào truy vấn item theo partition key?  
   a) aws dynamodb query  
   b) aws dynamodb scan  
   c) aws dynamodb get-item  
   d) Cả a và c  
   **Đáp án**: d
9. DynamoDB sử dụng giao thức nào?  
   a) HTTP/HTTPS  
   b) SQL  
   c) SSH  
   d) FTP  
   **Đáp án**: a
10. AWS CLI dùng để làm gì với DynamoDB?  
    a) Quản lý table và dữ liệu  
    b) Tạo index  
    c) Sao lưu dữ liệu  
    d) Giám sát hiệu suất  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao DynamoDB phù hợp với ứng dụng serverless?
2. Mô tả vai trò của partition key và sort key trong DynamoDB.
3. Làm thế nào để cấu hình IAM policy cho DynamoDB?
4. Sự khác biệt giữa Query và Scan trong DynamoDB là gì?
5. Tại sao cần quản lý capacity trong DynamoDB?

## Ngày 2: Sao Lưu, Khôi Phục và Giám Sát

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Sao Lưu và Khôi Phục** | - Point-in-time recovery (PITR).<br>- Export/import dữ liệu sang S3.<br>- Quy trình khôi phục table. | 2.5 giờ | [DynamoDB Backup and Restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html) | 1. Kích hoạt PITR cho table `employees`.<br>2. Export table `employees` sang S3 bằng AWS Console.<br>3. Khôi phục table từ PITR vào table mới `employees_restore`. |
| **Giám Sát với CloudWatch** | - Sử dụng CloudWatch Metrics cho DynamoDB.<br>- Theo dõi RCU/WCU, latency, errors.<br>- Cấu hình CloudWatch Alarms. | 2.5 giờ | [DynamoDB Monitoring](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/monitoring-cloudwatch.html) | 1. Tạo CloudWatch Alarm cho RCU vượt quá 80%.<br>2. Kiểm tra metrics latency của table `employees` trong CloudWatch.<br>3. Mô phỏng lỗi `ProvisionedThroughputExceeded` và kiểm tra log. |
| **Quản Lý Log** | - Sử dụng CloudWatch Logs Insights.<br>- Phân tích log DynamoDB Streams.<br>- Best practices cho logging. | 1 giờ | [DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) | 1. Kích hoạt DynamoDB Streams cho table `employees`.<br>2. Sử dụng CloudWatch Logs Insights để phân tích log stream.<br>3. Cấu hình log retention cho CloudWatch Logs. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. PITR trong DynamoDB dùng để làm gì?  
   a) Sao lưu liên tục  
   b) Khôi phục table tại thời điểm cụ thể  
   c) Tạo index  
   d) Giám sát hiệu suất  
   **Đáp án**: b
2. Lệnh nào export table sang S3?  
   a) aws dynamodb export-table-to-point-in-time  
   b) aws dynamodb backup-table  
   c) aws dynamodb scan  
   d) aws dynamodb query  
   **Đáp án**: a
3. CloudWatch Metrics theo dõi gì trong DynamoDB?  
   a) RCU/WCU  
   b) Latency  
   c) Errors  
   d) Tất cả  
   **Đáp án**: d
4. Lệnh nào kích hoạt DynamoDB Streams?  
   a) aws dynamodb update-table  
   b) aws dynamodb create-stream  
   c) aws dynamodb enable-stream  
   d) aws dynamodb stream-table  
   **Đáp án**: a
5. CloudWatch Alarm dùng để làm gì?  
   a) Cảnh báo khi vượt ngưỡng  
   b) Tạo backup  
   c) Tăng capacity  
   d) Tạo index  
   **Đáp án**: a
6. DynamoDB Streams lưu trữ dữ liệu trong bao lâu?  
   a) 24 giờ  
   b) 48 giờ  
   c) 7 ngày  
   d) Vô hạn  
   **Đáp án**: a
7. Log nào giúp phân tích hoạt động DynamoDB?  
   a) CloudWatch Logs Insights  
   b) S3 Logs  
   c) DynamoDB Logs  
   d) EC2 Logs  
   **Đáp án**: a
8. Lệnh nào khôi phục table từ PITR?  
   a) aws dynamodb restore-table-from-backup  
   b) aws dynamodb restore-table-to-point-in-time  
   c) aws dynamodb import-table  
   d) aws dynamodb scan  
   **Đáp án**: b
9. Metric nào đo độ trễ trong DynamoDB?  
   a) SuccessfulRequestLatency  
   b) ProvisionedThroughput  
   c) ConsumedCapacity  
   d) ErrorCount  
   **Đáp án**: a
10. Best practice khi giám sát DynamoDB là gì?  
    a) Sử dụng CloudWatch Alarms  
    b) Tắt logging  
    c) Không dùng Streams  
    d) Chỉ dùng S3  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao PITR quan trọng trong vận hành DynamoDB?
2. Mô tả quy trình khôi phục table từ S3 export.
3. Làm thế nào để phát hiện lỗi `ProvisionedThroughputExceeded`?
4. DynamoDB Streams có thể được sử dụng như thế nào trong DevOps?
5. Các best practice khi giám sát DynamoDB là gì?

## Ngày 3: Tối Ưu Hiệu Suất

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Global Secondary Index (GSI)** | - GSI là gì? Khi nào sử dụng.<br>- Tạo và quản lý GSI.<br>- Tác động đến capacity. | 2 giờ | [DynamoDB Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html) | 1. Tạo GSI trên cột `department` của table `employees`.<br>2. Truy vấn GSI bằng AWS CLI và so sánh hiệu suất.<br>3. Cập nhật capacity của GSI và kiểm tra metrics. |
| **Query và Scan Optimization** | - Query vs. Scan: Hiệu suất và chi phí.<br>- Sử dụng `ProjectionExpression`, `FilterExpression`.<br>- Tối ưu hóa truy vấn. | 2 giờ | [DynamoDB Query and Scan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html) | 1. Viết truy vấn sử dụng `ProjectionExpression` để giảm dữ liệu trả về.<br>2. Thực hiện Scan với `FilterExpression` và so sánh RCU với Query.<br>3. Tối ưu hóa truy vấn bằng cách thêm sort key condition. |
| **DAX (DynamoDB Accelerator)** | - DAX là gì? Lợi ích caching.<br>- Cấu hình DAX cluster.<br>- Best practices cho DAX. | 2 giờ | [DynamoDB DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) | 1. Cấu hình DAX cluster cho table `employees` (mô phỏng local với LocalStack nếu không có AWS).<br>2. So sánh latency với và không có DAX.<br>3. Kiểm tra cache hit/miss trong CloudWatch Metrics. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. GSI trong DynamoDB dùng để làm gì?  
   a) Tăng tốc truy vấn phụ  
   b) Sao lưu dữ liệu  
   c) Tạo partition key  
   d) Giám sát hiệu suất  
   **Đáp án**: a
2. Scan khác Query như thế nào?  
   a) Scan đọc toàn bộ table, Query chỉ đọc partition  
   b) Query đọc toàn bộ table  
   c) Scan nhanh hơn Query  
   d) Query dùng GSI  
   **Đáp án**: a
3. `ProjectionExpression` làm gì?  
   a) Giảm dữ liệu trả về  
   b) Tăng RCU  
   c) Tạo index  
   d) Lọc dữ liệu trước khi đọc  
   **Đáp án**: a
4. DAX là gì?  
   a) In-memory cache  
   b) Backup tool  
   c) Monitoring tool  
   d) Indexing tool  
   **Đáp án**: a
5. Lệnh nào tạo GSI?  
   a) aws dynamodb update-table  
   b) aws dynamodb create-table  
   c) aws dynamodb add-index  
   d) aws dynamodb modify-table  
   **Đáp án**: a
6. Scan tiêu tốn bao nhiêu RCU?  
   a) Dựa trên số item đọc  
   b) Dựa trên số partition  
   c) Cố định 1 RCU  
   d) Không tiêu tốn RCU  
   **Đáp án**: a
7. DAX cải thiện gì cho DynamoDB?  
   a) Latency  
   b) Throughput  
   c) Storage  
   d) Backup  
   **Đáp án**: a
8. `FilterExpression` được áp dụng khi nào?  
   a) Sau khi đọc dữ liệu  
   b) Trước khi đọc dữ liệu  
   c) Trong khi tạo index  
   d) Trong khi sao lưu  
   **Đáp án**: a
9. GSI có thể cập nhật capacity riêng biệt không?  
   a) Có  
   b) Không  
   c) Chỉ trong on-demand mode  
   d) Chỉ trong provisioned mode  
   **Đáp án**: a
10. Best practice khi dùng Scan là gì?  
    a) Sử dụng `FilterExpression`  
    b) Tắt GSI  
    c) Tăng RCU  
    d) Không dùng `ProjectionExpression`  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao cần GSI trong DynamoDB? Khi nào nên sử dụng?
2. Mô tả cách tối ưu hóa Scan để giảm chi phí RCU.
3. DAX cải thiện hiệu suất DynamoDB như thế nào?
4. Sự khác biệt giữa `ProjectionExpression` và `FilterExpression` là gì?
5. Làm thế nào để xác định khi nào cần dùng Query thay vì Scan?

## Ngày 4: Bảo Mật và Bảo Trì

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Bảo Mật DynamoDB** | - Mã hóa dữ liệu (at-rest, in-transit).<br>- Fine-grained access control.<br>- KMS integration cho encryption. | 2.5 giờ | [DynamoDB Security](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html) | 1. Kích hoạt mã hóa at-rest cho table `employees` bằng AWS KMS.<br>2. Tạo IAM policy fine-grained để chỉ cho phép `GetItem` trên cột `user_id`.<br>3. Kiểm tra kết nối HTTPS đến DynamoDB endpoint. |
| **Bảo Trì Table** | - Quản lý capacity (auto-scaling).<br>- Xóa item hết hạn bằng TTL.<br>- Xử lý lỗi `ProvisionedThroughputExceeded`. | 2.5 giờ | [DynamoDB TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) | 1. Kích hoạt auto-scaling cho table `employees`.<br>2. Cấu hình TTL trên cột `expiry_time` và kiểm tra xóa item tự động.<br>3. Mô phỏng lỗi `ProvisionedThroughputExceeded` và khắc phục bằng auto-scaling. |
| **Quản Lý Lỗi** | - Xử lý lỗi phổ biến (throttling, timeout).<br>- Phân tích log CloudWatch.<br>- Best practices cho xử lý lỗi. | 1 giờ | [DynamoDB Error Handling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProgrammingErrors.html) | 1. Tạo tình huống throttling bằng cách vượt RCU và kiểm tra log.<br>2. Cấu hình retry logic trong AWS SDK cho lỗi timeout.<br>3. Phân tích log CloudWatch để tìm nguyên nhân lỗi. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Mã hóa at-rest trong DynamoDB sử dụng gì?  
   a) AWS KMS  
   b) SSL/TLS  
   c) IAM  
   d) VPC  
   **Đáp án**: a
2. TTL trong DynamoDB làm gì?  
   a) Xóa item hết hạn  
   b) Tạo index  
   c) Sao lưu dữ liệu  
   d) Giám sát hiệu suất  
   **Đáp án**: a
3. Lỗi `ProvisionedThroughputExceeded` xảy ra khi nào?  
   a) Vượt capacity  
   b) Lỗi kết nối  
   c) Lỗi IAM  
   d) Lỗi KMS  
   **Đáp án**: a
4. Fine-grained access control dựa trên gì?  
   a) IAM policies  
   b) Table attributes  
   c) Cả hai  
   d) KMS keys  
   **Đáp án**: c
5. Lệnh nào kích hoạt auto-scaling?  
   a) aws application-autoscaling register-scalable-target  
   b) aws dynamodb update-table  
   c) aws dynamodb auto-scale  
   d) aws dynamodb enable-scaling  
   **Đáp án**: a
6. KMS dùng để làm gì trong DynamoDB?  
   a) Mã hóa dữ liệu  
   b) Tạo index  
   c) Giám sát hiệu suất  
   d) Sao lưu dữ liệu  
   **Đáp án**: a
7. Lệnh nào cấu hình TTL?  
   a) aws dynamodb update-time-to-live  
   b) aws dynamodb set-ttl  
   c) aws dynamodb enable-ttl  
   d) aws dynamodb modify-table  
   **Đáp án**: a
8. Lỗi timeout trong DynamoDB nên xử lý thế nào?  
   a) Retry logic  
   b) Tăng RCU  
   c) Tắt Streams  
   d) Xóa table  
   **Đáp án**: a
9. CloudWatch Logs Insights dùng để làm gì?  
   a) Phân tích log DynamoDB  
   b) Tạo backup  
   c) Tăng capacity  
   d) Tạo index  
   **Đáp án**: a
10. Best practice khi xử lý lỗi là gì?  
    a) Sử dụng retry logic  
    b) Tắt logging  
    c) Không dùng auto-scaling  
    d) Xóa GSI  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao cần mã hóa dữ liệu trong DynamoDB?
2. Mô tả cách cấu hình TTL để xóa item tự động.
3. Làm thế nào để xử lý lỗi `ProvisionedThroughputExceeded`?
4. Fine-grained access control giúp bảo mật DynamoDB như thế nào?
5. Các best practice khi quản lý lỗi trong DynamoDB là gì?

## Ngày 5: Final Lab và Đánh Giá

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Final Lab** | Triển khai DynamoDB table cho ứng dụng e-commerce, với quản lý capacity, GSI, sao lưu, bảo mật, và giám sát. | 4 giờ | [DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/) | **Mô tả**: Thiết lập table DynamoDB cho ứng dụng e-commerce với các bảng `customers`, `products`, `orders`, đảm bảo quản lý quyền, hiệu suất, bảo mật, và sao lưu.<br>**Yêu cầu**:<br>- **Môi trường**: AWS Free Tier hoặc LocalStack với DynamoDB.<br>- **Đề mục**:<br>  1. **Thiết kế table**: Tạo các bảng với partition key, sort key, và attributes phù hợp.<br>  2. **Quản lý quyền**: Tạo IAM policy cho phép `sales` user chỉ truy cập `orders`.<br>  3. **GSI**: Tạo GSI trên cột `product_category` của table `products`.<br>  4. **Sao lưu**: Kích hoạt PITR và export table `orders` sang S3.<br>  5. **Tối ưu hiệu suất**: Sử dụng `ProjectionExpression` để tối ưu truy vấn.<br>  6. **Bảo mật**: Kích hoạt mã hóa at-rest bằng KMS và cấu hình HTTPS.<br>  7. **Giám sát**: Tạo CloudWatch Alarm cho RCU/WCU vượt ngưỡng.<br>  8. **Tài liệu**: Cung cấp README.md với schema, quyền, quy trình sao lưu, và giám sát.<br>**Guideline**:<br>- Sử dụng AWS CLI hoặc Console để quản lý table.<br>- Đảm bảo schema hỗ trợ ứng dụng e-commerce (tìm kiếm sản phẩm, quản lý đơn hàng).<br>- Kiểm tra quyền IAM để đảm bảo chỉ truy cập dữ liệu cần thiết.<br>- Tài liệu hóa rõ ràng, bao gồm sơ đồ schema và hướng dẫn tái tạo.<br>- Kiểm tra hiệu suất truy vấn bằng CloudWatch Metrics.<br>- Đảm bảo backup có thể khôi phục thành công. |
| **MCQ** | Bài kiểm tra trắc nghiệm về các tác vụ vận hành DynamoDB. | 2 giờ | [DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/) | Tạo và trả lời 20 câu hỏi trắc nghiệm về kiến trúc, quản lý table, sao lưu, giám sát, tối ưu, và bảo mật. Sample MCQs:<br>1. DynamoDB là loại database nào? (a) NoSQL **(Đáp án: a)**<br>2. Lệnh nào tạo GSI? (a) aws dynamodb update-table **(Đáp án: a)**<br>3. TTL dùng để làm gì? (a) Xóa item hết hạn **(Đáp án: a)**<br>4. CloudWatch Metrics theo dõi gì? (a) RCU/WCU, latency **(Đáp án: a)**<br>5. Lỗi `ProvisionedThroughputExceeded` xử lý thế nào? (a) Auto-scaling **(Đáp án: a)** |

**Tổng thời gian**: 6 giờ

## Ghi Chú
- **Tổng thời gian**: 30 giờ (6 giờ/ngày).
- **Môi trường thực hành**: AWS Free Tier hoặc LocalStack với DynamoDB, AWS CLI, Console.
- **Tài liệu chính**: [AWS DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/).
- **Final Lab**: Dự án thực tế triển khai table cho e-commerce, tập trung vào vận hành.
- **Đánh giá**: MCQ và câu hỏi vấn đáp củng cố kiến thức; Final Lab kiểm tra khả năng áp dụng.[](https://aws.amazon.com/dynamodb/)