Dưới đây là lịch trình đào tạo HashiCorp Vault trong 5 ngày đã được bổ sung chi tiết hơn về các bài tập thực hành và tài liệu tham khảo, đảm bảo đầy đủ và rõ ràng hơn. Các bài tập thực hành được thiết kế cụ thể hơn với hướng dẫn từng bước, và các tài liệu tham khảo được cập nhật để bao quát toàn bộ nội dung cần thiết. Lịch trình vẫn giữ cấu trúc 5 ngày, mỗi ngày 6-7 giờ, tổng cộng khoảng 31 giờ, phù hợp cho người mới bắt đầu và quản trị viên hệ thống.

---

# Lịch Trình Đào Tạo HashiCorp Vault Trong 5 Ngày (Đã Bổ Sung)

## Tổng Quan
- **Mục tiêu**: Cung cấp kiến thức toàn diện về HashiCorp Vault, từ cơ bản đến nâng cao, giúp người học quản lý secrets an toàn, triển khai Vault trong môi trường sản xuất, và chuẩn bị cho chứng chỉ [Vault Associate Certification](https://developer.hashicorp.com/vault/docs/certifications).
- **Đối tượng**: Người mới bắt đầu, quản trị viên hệ thống, kỹ sư DevOps.
- **Thời lượng**: 31 giờ (6-7 giờ/ngày trong 5 ngày).
- **Phương pháp**: Kết hợp lý thuyết, thực hành, và đánh giá (Final Lab và MCQ).
- **Môi trường thực hành**: Máy local (Vagrant/VirtualBox/Docker) hoặc [HashiCorp Learn](https://learn.hashicorp.com/vault).
- **Tài liệu chính**: [HashiCorp Vault Documentation](https://developer.hashicorp.com/vault/docs), [HashiCorp Learn Tutorials](https://learn.hashicorp.com/vault).

---

## Ngày 1: Giới Thiệu về HashiCorp Vault

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **What is HashiCorp Vault?** | Tổng quan về Vault, vai trò trong quản lý secrets, các trường hợp sử dụng (API keys, mật khẩu, chứng chỉ). So sánh với các công cụ khác như AWS Secrets Manager. | 1.5 giờ | - [What is Vault?](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault)<br>- [Vault Use Cases](https://developer.hashicorp.com/vault/docs/about-vault/use-cases)<br>- [Vault vs. Other Tools](https://www.hashicorp.com/resources/vault-vs-other-secrets-managers) | **Lab 1.1**: Cài đặt Vault trên máy local (hoặc Docker) và khởi động server ở chế độ dev.<br>1. Cài đặt Vault binary từ [Vault Downloads](https://www.vaultproject.io/downloads).<br>2. Chạy lệnh `vault server -dev` và kiểm tra trạng thái qua `vault status`.<br>3. Truy cập Vault UI tại `http://127.0.0.1:8200` và xác minh giao diện hoạt động. |
| **Vault Architecture** | Các thành phần cốt lõi: storage backends (Consul, Raft), seals, barrier, authentication/authorization. | 1.5 giờ | - [Vault Architecture](https://developer.hashicorp.com/vault/docs/concepts)<br>- [Storage Backends](https://developer.hashicorp.com/vault/docs/configuration/storage)<br>- [Seal/Unseal](https://developer.hashicorp.com/vault/docs/concepts/seal) | **Lab 1.2**: Khám phá kiến trúc Vault.<br>1. Sử dụng lệnh `vault operator init` để khởi tạo Vault.<br>2. Lưu các unseal keys và root token vào file an toàn.<br>3. Thực hiện `vault operator unseal` để mở Vault và kiểm tra trạng thái.<br>4. Truy cập UI để xem các thành phần (secrets, policies, auth methods). |
| **Basic Operations** | Lưu trữ, truy xuất, xóa secrets bằng CLI và API. Giới thiệu KV secrets engine (v1). | 2 giờ | - [KV Secrets Engine v1](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v1)<br>- [Vault CLI Reference](https://developer.hashicorp.com/vault/docs/commands)<br>- [Vault API Docs](https://developer.hashicorp.com/vault/api-docs) | **Lab 1.3**: Quản lý secrets cơ bản.<br>1. Kích hoạt KV secrets engine: `vault secrets enable -path=secret kv`.<br>2. Lưu secret: `vault kv put secret/my-secret my-key=my-value`.<br>3. Truy xuất secret: `vault kv get secret/my-secret`.<br>4. Sử dụng API (curl) để truy xuất secret: `curl -H "X-Vault-Token: $VAULT_TOKEN" $VAULT_ADDR/v1/secret/my-secret`. |
| **Initialization and Unsealing** | Quy trình khởi tạo Vault, seal/unseal, và bảo mật unseal keys. | 1 giờ | - [Initialize and Unseal](https://developer.hashicorp.com/vault/docs/concepts/seal)<br>- [Vault Security Model](https://developer.hashicorp.com/vault/docs/concepts/security) | **Lab 1.4**: Khởi tạo và unseal Vault.<br>1. Khởi tạo Vault với 3 unseal keys và threshold 2: `vault operator init -key-shares=3 -key-threshold=2`.<br>2. Unseal Vault bằng 2 unseal keys.<br>3. Seal lại Vault: `vault operator seal` và thử unseal lại.<br>4. Lưu unseal keys vào file mã hóa (ví dụ: sử dụng GPG). |

**Tổng thời gian**: 6 giờ  
**Ghi chú**: Các bài tập sử dụng Vault ở chế độ dev để đơn giản hóa. Người học cần cài đặt Vault binary và có quyền truy cập CLI/UI.

---

## Ngày 2: Authentication và Access Control

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Authentication Methods** | Tổng quan về các phương thức xác thực: token, userpass, AppRole, LDAP. Cách Vault xác thực danh tính. | 2 giờ | - [Authentication Methods](https://developer.hashicorp.com/vault/docs/auth)<br>- [Token Auth](https://developer.hashicorp.com/vault/docs/auth/token)<br>- [Userpass Auth](https://developer.hashicorp.com/vault/docs/auth/userpass) | **Lab 2.1**: Thiết lập userpass authentication.<br>1. Kích hoạt userpass: `vault auth enable userpass`.<br>2. Tạo user: `vault write auth/userpass/users/alice password=securepassword policies=default`.<br>3. Đăng nhập bằng userpass: `vault login -method=userpass username=alice password=securepassword`.<br>4. Kiểm tra token được cấp qua CLI và UI. |
| **Advanced Authentication** | Tích hợp với các nhà cung cấp danh tính bên ngoài: OIDC, AWS IAM, JWT. Quy trình máy với máy (machine-to-machine). | 2 giờ | - [OIDC Auth](https://developer.hashicorp.com/vault/docs/auth/jwt-oidc)<br>- [AWS IAM Auth](https://developer.hashicorp.com/vault/docs/auth/aws)<br>- [JWT Auth](https://developer.hashicorp.com/vault/docs/auth/jwt) | **Lab 2.2**: Cấu hình OIDC authentication với GitHub.<br>1. Đăng ký ứng dụng OAuth trên GitHub, lấy client ID và secret.<br>2. Kích hoạt OIDC: `vault auth enable oidc`.<br>3. Cấu hình OIDC: `vault write auth/oidc/config ...` (theo tài liệu).<br>4. Đăng nhập qua OIDC trên Vault UI và kiểm tra token.<br>5. (Tùy chọn) Cấu hình AWS IAM auth nếu có tài khoản AWS. |
| **Policies and ACLs** | Viết policies để kiểm soát truy cập. Cấu trúc policy, cú pháp HCL, và best practices. | 2 giờ | - [Policies](https://developer.hashicorp.com/vault/docs/concepts/policies)<br>- [Policy Syntax](https://developer.hashicorp.com/vault/docs/concepts/policy-syntax)<br>- [Default Policy](https://developer.hashicorp.com/vault/docs/concepts/policies#default-policy) | **Lab 2.3**: Viết và áp dụng policies.<br>1. Tạo file `restrict.hcl` với policy giới hạn đọc secret tại `secret/restricted/*`.<br>2. Áp dụng policy: `vault policy write restrict-policy restrict.hcl`.<br>3. Gán policy cho user: `vault write auth/userpass/users/alice policies=restrict-policy`.<br>4. Đăng nhập bằng user `alice` và thử truy cập secret ngoài phạm vi policy (nên thất bại). |

**Tổng thời gian**: 6 giờ  
**Ghi chú**: Các bài tập yêu cầu Vault server đã được khởi tạo từ Ngày 1. OIDC cần tài khoản GitHub hoặc Google để thực hành.

---

## Ngày 3: Secret Engines

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **KV Secret Engine** | Quản lý secrets tĩnh với KV v2, hỗ trợ versioning và soft delete. | 2 giờ | - [KV v2 Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2)<br>- [KV CLI Commands](https://developer.hashicorp.com/vault/docs/commands/kv) | **Lab 3.1**: Sử dụng KV v2.<br>1. Kích hoạt KV v2: `vault secrets enable -path=secret kv-v2`.<br>2. Lưu secret với versioning: `vault kv put secret/app/config api_key=abc123`.<br>3. Cập nhật secret để tạo version mới: `vault kv put secret/app/config api_key=xyz789`.<br>4. Truy xuất version cụ thể: `vault kv get -version=1 secret/app/config`.<br>5. Thử soft delete và undelete secret. |
| **Database Secrets Engine** | Tạo credentials động cho cơ sở dữ liệu (MySQL, PostgreSQL). | 2 giờ | - [Database Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/databases)<br>- [MySQL/PostgreSQL Setup](https://developer.hashicorp.com/vault/docs/secrets/databases/mysql-maria) | **Lab 3.2**: Cấu hình database secrets engine.<br>1. Cài đặt MySQL/PostgreSQL local hoặc dùng Docker.<br>2. Kích hoạt database engine: `vault secrets enable database`.<br>3. Cấu hình kết nối: `vault write database/config/my-database ...` (theo tài liệu).<br>4. Tạo role để sinh credentials động: `vault write database/roles/my-role ...`.<br>5. Lấy credentials: `vault read database/creds/my-role` và kiểm tra trên database. |
| **Transit Secrets Engine** | Mã hóa/giải mã dữ liệu với transit engine, hỗ trợ key rotation. | 1.5 giờ | - [Transit Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/transit)<br>- [Transit Key Rotation](https://developer.hashicorp.com/vault/docs/secrets/transit#key-rotation) | **Lab 3.3**: Mã hóa dữ liệu với transit engine.<br>1. Kích hoạt transit engine: `vault secrets enable transit`.<br>2. Tạo key: `vault write -f transit/keys/my-key`.<br>3. Mã hóa dữ liệu: `vault write transit/encrypt/my-key plaintext=$(base64 <<< "my secret data")`.<br>4. Giải mã dữ liệu: `vault write transit/decrypt/my-key ciphertext=<ciphertext>`.<br>5. Thử rotate key và giải mã lại. |
| **Introduction to Other Secret Engines** | Tổng quan về AWS, GCP, SSH, PKI secrets engines. | 1.5 giờ | - [Secrets Engines Overview](https://developer.hashicorp.com/vault/docs/secrets)<br>- [AWS Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/aws)<br>- [PKI Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/pki) | **Lab 3.4**: Cấu hình AWS secrets engine.<br>1. Kích hoạt AWS engine: `vault secrets enable aws`.<br>2. Cấu hình AWS credentials: `vault write aws/config/root access_key=<key> secret_key=<secret>`.<br>3. Tạo role: `vault write aws/roles/my-role ...`.<br>4. Sinh credentials động: `vault read aws/creds/my-role` và kiểm tra trên AWS CLI. |

**Tổng thời gian**: 7 giờ  
**Ghi chú**: Yêu cầu MySQL/PostgreSQL hoặc AWS account để thực hành đầy đủ. Có thể dùng [HashiCorp Learn](https://learn.hashicorp.com/vault) nếu thiếu tài nguyên.

---

## Ngày 4: Chủ Đề Nâng Cao và Best Practices

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **High Availability and Clustering** | Thiết lập Vault trong chế độ HA với Raft storage backend. Quản lý failover và replication. | 2 giờ | - [HA with Raft](https://developer.hashicorp.com/vault/tutorials/raft/raft-storage)<br>- [Vault HA Concepts](https://developer.hashicorp.com/vault/docs/concepts/ha) | **Lab 4.1**: Mô phỏng HA với Raft.<br>1. Cài đặt 3 Vault nodes (dùng Docker hoặc Vagrant).<br>2. Cấu hình Raft storage: chỉnh sửa file config Vault (`storage "raft" { ... }`).<br>3. Khởi tạo cluster: `vault operator init` trên node chính.<br>4. Join các node phụ: `vault operator raft join`.<br>5. Kiểm tra trạng thái cluster: `vault operator raft list-peers`. |
| **Auditing and Logging** | Cấu hình audit devices (file, syslog) để ghi lại các hoạt động trong Vault. | 1.5 giờ | - [Auditing](https://developer.hashicorp.com/vault/docs/audit)<br>- [Audit Devices](https://developer.hashicorp.com/vault/docs/audit/file) | **Lab 4.2**: Thiết lập audit logging.<br>1. Kích hoạt audit file: `vault audit enable file file_path=/vault/logs/audit.log`.<br>2. Thực hiện các thao tác (lưu secret, đăng nhập) và kiểm tra log.<br>3. (Tùy chọn) Cấu hình syslog audit nếu có syslog server.<br>4. Phân tích log để xác định các request và response. |
| **Best Practices and Security** | Áp dụng TLS, hạn chế quyền truy cập, quản lý unseal keys, và production hardening. | 2 giờ | - [Production Hardening](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)<br>- [Vault Security Best Practices](https://developer.hashicorp.com/vault/docs/concepts/security) | **Lab 4.3**: Áp dụng best practices.<br>1. Tạo certificate TLS cho Vault (dùng OpenSSL hoặc Certbot).<br>2. Cấu hình Vault với TLS: chỉnh sửa file config (`listener "tcp" { tls_cert_file = ... }`).<br>3. Hạn chế truy cập mạng bằng firewall (chỉ cho phép port 8200).<br>4. Kiểm tra Vault với HTTPS qua CLI/UI. |
| **Integrating with CI/CD and Cloud** | Tích hợp Vault với Jenkins, GitLab CI, hoặc AWS. Sử dụng Vault Agent. | 1.5 giờ | - [Vault Agent](https://developer.hashicorp.com/vault/docs/agent)<br>- [Vault Integrations](https://developer.hashicorp.com/vault/docs/integrations) | **Lab 4.4**: Tích hợp Vault với CI/CD.<br>1. Cài đặt Vault Agent trên máy local.<br>2. Cấu hình Vault Agent để lấy secret từ KV v2.<br>3. Tạo pipeline Jenkins/GitLab CI mẫu để truy xuất secret từ Vault.<br>4. Kiểm tra pipeline lấy secret và sử dụng trong ứng dụng. |

**Tổng thời gian**: 7 giờ  
**Ghi chú**: HA yêu cầu nhiều tài nguyên, có thể mô phỏng lý thuyết nếu thiếu máy chủ. Vault Agent cần cấu hình cẩn thận.

---

## Ngày 5: Final Lab và Đánh Giá

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|-----------------------|-----------------------|
| **Final Lab** | Triển khai một hệ thống Vault hoàn chỉnh với authentication, policies, secret engines, và tích hợp ứng dụng. | 4 giờ | - [Vault Documentation](https://developer.hashicorp.com/vault/docs)<br>- [Vault Agent Auto-Auth](https://developer.hashicorp.com/vault/docs/agent/autoauth)<br>- [Sample App Integration](https://learn.hashicorp.com/tutorials/vault/application-integration) | **Lab 5.1**: Dự án tổng hợp.<br>**Mục tiêu**: Thiết lập Vault và tích hợp với ứng dụng web mẫu.<br>**Môi trường**: 1 Vault server, 1 ứng dụng web (Docker, ví dụ: Flask/Node.js).<br>**Các bước**:<br>1. **Cài đặt Vault**: Chạy Vault server với Raft storage, khởi tạo và unseal.<br>2. **Authentication**:<br>- Kích hoạt userpass: tạo 2 user với mật khẩu.<br>- Kích hoạt OIDC với GitHub/Google.<br>3. **Policies**: Viết 2 policies (read-only và read-write) cho path `secret/app/*`.<br>4. **Secret Engines**:<br>- Kích hoạt KV v2, lưu secret `secret/app/config`.<br>- Kích hoạt database engine, tạo credentials động cho MySQL.<br>- Kích hoạt transit engine, mã hóa một chuỗi dữ liệu.<br>5. **Integration**:<br>- Chạy ứng dụng web mẫu (Docker).<br>- Sử dụng Vault Agent để lấy secret từ KV v2 và inject vào ứng dụng.<br>6. **Best Practices**: Bật TLS, audit logging, và giới hạn truy cập mạng.<br>**Kiểm tra**:<br>- Đăng nhập bằng userpass và OIDC, truy xuất secret.<br>- Ứng dụng web hiển thị secret lấy từ Vault.<br>- Kiểm tra audit log ghi lại các hoạt động. |
| **MCQ** | Bài kiểm tra trắc nghiệm về các khái niệm và thao tác trong Vault. | 1 giờ | - [Vault Documentation](https://developer.hashicorp.com/vault/docs)<br>- [Vault Associate Exam Guide](https://developer.hashicorp.com/vault/docs/certifications) | **Lab 5.2**: Thi trắc nghiệm.<br>1. Chuẩn bị 25 câu hỏi trắc nghiệm, ví dụ:<br>- Vai trò của unseal keys trong Vault là gì?<br>- Cú pháp policy để cấp quyền đọc cho path `secret/data/*`?<br>- Lợi ích của database secrets engine?<br>2. Người học trả lời trong 1 giờ.<br>3. Đáp án tham khảo từ [HashiCorp Learn](https://learn.hashicorp.com/vault) hoặc tài liệu chính. |

**Tổng thời gian**: 5 giờ  
**Ghi chú**: Final Lab yêu cầu môi trường Docker để chạy ứng dụng web mẫu. MCQ cần được thiết kế trước hoặc dùng từ [HashiCorp Learn](https://learn.hashicorp.com/vault).

---

## Ghi Chú Bổ Sung
- **Tổng thời gian**: 31 giờ (6-7 giờ/ngày), bao gồm nghỉ giải lao và thảo luận.
- **Môi trường thực hành**:
  - **Local**: Cài đặt Vault, MySQL/PostgreSQL, và Docker qua Vagrant/VirtualBox.
  - **Trực tuyến**: Sử dụng [HashiCorp Learn](https://learn.hashicorp.com/vault) để thực hành miễn phí.
  - **Yêu cầu**: Quyền truy cập CLI/UI, tài khoản GitHub/Google cho OIDC, và (tùy chọn) AWS account.
- **Tài liệu bổ sung**:
  - [Vault CLI Reference](https://developer.hashicorp.com/vault/docs/commands)
  - [Vault API Reference](https://developer.hashicorp.com/vault/api-docs)
  - [Vault Tutorials](https://learn.hashicorp.com/vault)
  - [Vault Security Best Practices](https://developer.hashicorp.com/vault/docs/concepts/security)
- **Final Lab**: Dự án thực tế tích hợp toàn bộ kỹ năng, có thể tùy chỉnh độ khó dựa trên người học.
- **MCQ**: Có thể tham khảo mẫu câu hỏi từ [Vault Associate Certification](https://developer.hashicorp.com/vault/docs/certifications) hoặc tự tạo.

---

## Báo Cáo Chi Tiết (Đã Bổ Sung)

### Giới Thiệu
HashiCorp Vault là công cụ mã nguồn mở để quản lý secrets an toàn, hỗ trợ lưu trữ API keys, mật khẩu, chứng chỉ, và mã hóa dữ liệu. Lịch trình 5 ngày này cung cấp kiến thức từ cơ bản (cài đặt, lưu trữ secrets) đến nâng cao (HA, auditing, tích hợp CI/CD), phù hợp cho quản trị viên hệ thống và kỹ sư DevOps. Các bài thực hành được thiết kế chi tiết với các bước cụ thể, sử dụng CLI, UI, và API, giúp người học áp dụng ngay vào thực tế.

### Cấu Trúc Lịch Trình
- **Ngày 1**: Nắm vững khái niệm, kiến trúc, và thao tác cơ bản (lưu trữ secrets, unseal).
- **Ngày 2**: Thành thạo authentication (userpass, OIDC) và kiểm soát truy cập qua policies.
- **Ngày 3**: Làm việc với secret engines (KV v2, database, transit, AWS) để quản lý secrets tĩnh và động.
- **Ngày 4**: Tìm hiểu HA, auditing, best practices, và tích hợp CI/CD.
- **Ngày 5**: Áp dụng toàn bộ kiến thức vào Final Lab và đánh giá qua MCQ.

### Lợi Ích
- Thành thạo quản lý secrets với Vault qua CLI, UI, API.
- Biết cách triển khai Vault trong môi trường sản xuất với HA và bảo mật cao.
- Chuẩn bị cho [Vault Associate Certification](https://developer.hashicorp.com/vault/docs/certifications).
- Nâng cao kỹ năng DevOps và bảo mật.

### Hạn Chế
- Yêu cầu kiến thức cơ bản về Linux, Docker, và quản trị hệ thống.
- HA và auditing cần nhiều tài nguyên (có thể mô phỏng lý thuyết).
- OIDC và AWS cần tài khoản bên thứ ba để thực hành đầy đủ.

### Key Citations
- [What is HashiCorp Vault?](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault)
- [Vault Architecture](https://developer.hashicorp.com/vault/docs/concepts)
- [KV Secrets Engine v1/v2](https://developer.hashicorp.com/vault/docs/secrets/kv)
- [Initialize and Unseal](https://developer.hashicorp.com/vault/docs/concepts/seal)
- [Authentication Methods](https://developer.hashicorp.com/vault/docs/auth)
- [OIDC Authentication](https://developer.hashicorp.com/vault/docs/auth/jwt-oidc)
- [Policies](https://developer.hashicorp.com/vault/docs/concepts/policies)
- [Secret Engines](https://developer.hashicorp.com/vault/docs/secrets)
- [Database Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/databases)
- [Transit Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/transit)
- [AWS Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/aws)
- [High Availability with Raft](https://developer.hashicorp.com/vault/tutorials/raft/raft-storage)
- [Auditing](https://developer.hashicorp.com/vault/docs/audit)
- [Production Hardening](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [Vault Integrations](https://developer.hashicorp.com/vault/docs/integrations)
- [HashiCorp Learn](https://learn.hashicorp.com/vault)
- [Vault Associate Certification](https://developer.hashicorp.com/vault/docs/certifications)


---
Dưới đây là danh sách 25 câu hỏi trắc nghiệm (MCQ) được tạo thêm để đánh giá kiến thức về HashiCorp Vault, bao quát các chủ đề từ Ngày 1 đến Ngày 4 của lịch trình đào tạo. Các câu hỏi được thiết kế với độ khó từ cơ bản đến nâng cao, phù hợp để kiểm tra hiểu biết toàn diện và chuẩn bị cho [Vault Associate Certification](https://developer.hashicorp.com/vault/docs/certifications). Mỗi câu có 4 đáp án, kèm giải thích ngắn gọn.

---

## Bài Kiểm Tra Trắc Nghiệm (MCQ) về HashiCorp Vault

### Chủ đề 1: Giới thiệu và Kiến trúc Vault

1. **HashiCorp Vault chủ yếu được sử dụng để làm gì?**  
   a) Quản lý cơ sở hạ tầng mạng  
   b) Quản lý secrets và bảo vệ dữ liệu nhạy cảm  
   c) Tự động hóa triển khai ứng dụng  
   d) Giám sát hiệu suất hệ thống  
   **Đáp án**: b  
   **Giải thích**: Vault được thiết kế để quản lý secrets như API keys, mật khẩu, chứng chỉ, và mã hóa dữ liệu ([What is Vault?](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault)).

2. **Thành phần nào của Vault chịu trách nhiệm mã hóa dữ liệu trước khi lưu trữ?**  
   a) Storage Backend  
   b) Barrier  
   c) Audit Device  
   d) Secret Engine  
   **Đáp án**: b  
   **Giải thích**: Barrier mã hóa tất cả dữ liệu trước khi lưu vào storage backend ([Vault Architecture](https://developer.hashicorp.com/vault/docs/concepts)).

3. **Lệnh nào được sử dụng để khởi tạo một Vault server?**  
   a) `vault server start`  
   b) `vault operator init`  
   c) `vault secrets enable`  
   d) `vault auth enable`  
   **Đáp án**: b  
   **Giải thích**: `vault operator init` khởi tạo Vault và tạo unseal keys cùng root token ([Initialize and Unseal](https://developer.hashicorp.com/vault/docs/concepts/seal)).

4. **Trong chế độ dev, Vault có yêu cầu unseal không?**  
   a) Có, luôn yêu cầu  
   b) Không, tự động unseal  
   c) Chỉ khi cấu hình TLS  
   d) Chỉ khi dùng Raft storage  
   **Đáp án**: b  
   **Giải thích**: Chế độ dev tự động unseal để đơn giản hóa thử nghiệm ([Vault CLI Reference](https://developer.hashicorp.com/vault/docs/commands)).

5. **Lệnh nào dùng để lưu trữ secret trong KV secrets engine?**  
   a) `vault kv put`  
   b) `vault write secret`  
   c) `vault secrets store`  
   d) `vault kv save`  
   **Đáp án**: a  
   **Giải thích**: `vault kv put` lưu trữ secret trong KV engine ([KV Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/kv)).

---

### Chủ đề 2: Authentication và Access Control

6. **Phương thức xác thực nào dưới đây không được Vault hỗ trợ?**  
   a) Userpass  
   b) OIDC  
   c) Kerberos  
   d) SNMP  
   **Đáp án**: d  
   **Giải thích**: Vault hỗ trợ userpass, OIDC, Kerberos, nhưng không hỗ trợ SNMP ([Authentication Methods](https://developer.hashicorp.com/vault/docs/auth)).

7. **Cú pháp nào trong policy HCL cấp quyền đọc cho path `secret/data/my-secret`?**  
   a) `path "secret/data/my-secret" { capabilities = ["read"] }`  
   b) `path "secret/my-secret" { permissions = "read" }`  
   c) `path "secret/data/my-secret" { access = "read" }`  
   d) `path "secret/my-secret" { capabilities = ["get"] }`  
   **Đáp án**: a  
   **Giải thích**: Policy HCL sử dụng `capabilities` để cấp quyền, và path phải đúng cú pháp ([Policies](https://developer.hashicorp.com/vault/docs/concepts/policies)).

8. **Token trong Vault có thể được gán bao nhiêu policy?**  
   a) Chỉ một policy  
   b) Nhiều policy  
   c) Không gán policy nào  
   d) Chỉ policy mặc định  
   **Đáp án**: b  
   **Giải thích**: Token có thể được gán nhiều policy để kiểm soát truy cập ([Token Auth](https://developer.hashicorp.com/vault/docs/auth/token)).

9. **Lệnh nào kích hoạt userpass authentication?**  
   a) `vault auth enable userpass`  
   b) `vault userpass enable`  
   c) `vault secrets enable userpass`  
   d) `vault write auth/userpass`  
   **Đáp án**: a  
   **Giải thích**: `vault auth enable userpass` kích hoạt phương thức xác thực userpass ([Userpass Auth](https://developer.hashicorp.com/vault/docs/auth/userpass)).

10. **OIDC authentication thường được dùng cho trường hợp nào?**  
    a) Xác thực máy với máy  
    b) Xác thực người dùng qua nhà cung cấp danh tính  
    c) Quản lý cơ sở dữ liệu  
    d) Mã hóa dữ liệu  
    **Đáp án**: b  
    **Giải thích**: OIDC dùng để xác thực người dùng qua các nhà cung cấp như Google, GitHub ([OIDC Auth](https://developer.hashicorp.com/vault/docs/auth/jwt-oidc)).

---

### Chủ đề 3: Secret Engines

11. **KV v2 secrets engine hỗ trợ tính năng nào dưới đây?**  
    a) Mã hóa dữ liệu  
    b) Versioning của secrets  
    c) Tạo chứng chỉ SSL  
    d) Quản lý IAM roles  
    **Đáp án**: b  
    **Giải thích**: KV v2 hỗ trợ versioning và soft delete cho secrets ([KV v2](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2)).

12. **Database secrets engine tạo ra credentials với đặc điểm gì?**  
    a) Tĩnh, không thay đổi  
    b) Động, có thời hạn  
    c) Mã hóa end-to-end  
    d) Chỉ đọc, không ghi  
    **Đáp án**: b  
    **Giải thích**: Database engine tạo credentials động với TTL (time-to-live) ([Database Secrets](https://developer.hashicorp.com/vault/docs/secrets/databases)).

13. **Lệnh nào kích hoạt transit secrets engine?**  
    a) `vault secrets enable transit`  
    b) `vault transit enable`  
    c) `vault write transit/enable`  
    d) `vault secrets enable encryption`  
    **Đáp án**: a  
    **Giải thích**: `vault secrets enable transit` kích hoạt transit engine ([Transit Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/transit)).

14. **Transit secrets engine được sử dụng để làm gì?**  
    a) Lưu trữ secrets tĩnh  
    b) Mã hóa và giải mã dữ liệu  
    c) Tạo credentials động  
    d) Quản lý policies  
    **Đáp án**: b  
    **Giải thích**: Transit engine mã hóa/giải mã dữ liệu mà không lưu trữ ([Transit Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/transit)).

15. **AWS secrets engine có thể tạo gì?**  
    a) API keys tạm thời cho AWS  
    b) Chứng chỉ SSL cho AWS  
    c) Mật khẩu cho database  
    d) Token OIDC  
    **Đáp án**: a  
    **Giải thích**: AWS secrets engine tạo credentials IAM tạm thời ([AWS Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/aws)).

---

### Chủ đề 4: Chủ đề Nâng cao và Best Practices

16. **Raft storage backend được sử dụng trong Vault để làm gì?**  
    a) Mã hóa dữ liệu  
    b) Hỗ trợ high availability  
    c) Tạo credentials động  
    d) Ghi audit logs  
    **Đáp án**: b  
    **Giải thích**: Raft là storage backend hỗ trợ HA và replication ([HA with Raft](https://developer.hashicorp.com/vault/tutorials/raft/raft-storage)).

17. **Lệnh nào kiểm tra trạng thái cluster Raft?**  
    a) `vault operator raft status`  
    b) `vault raft list-peers`  
    c) `vault status`  
    d) `vault operator cluster`  
    **Đáp án**: b  
    **Giải thích**: `vault operator raft list-peers` hiển thị các node trong cluster Raft ([HA with Raft](https://developer.hashicorp.com/vault/tutorials/raft/raft-storage)).

18. **Audit device trong Vault làm gì?**  
    a) Mã hóa secrets  
    b) Ghi lại các hoạt động của Vault  
    c) Tạo credentials động  
    d) Quản lý policies  
    **Đáp án**: b  
    **Giải thích**: Audit device ghi lại mọi request/response trong Vault ([Auditing](https://developer.hashicorp.com/vault/docs/audit)).

19. **Thực hành tốt nhất (best practice) nào nên áp dụng khi triển khai Vault trong sản xuất?**  
    a) Vô hiệu hóa TLS  
    b) Sử dụng chế độ dev  
    c) Bật audit logging  
    d) Tắt unseal keys  
    **Đáp án**: c  
    **Giải thích**: Audit logging là bắt buộc để giám sát và bảo mật ([Production Hardening](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)).

20. **Vault Agent được sử dụng để làm gì trong CI/CD?**  
    a) Tạo pipeline CI/CD  
    b) Tự động lấy secrets và inject vào ứng dụng  
    c) Quản lý cluster Vault  
    d) Mã hóa dữ liệu pipeline  
    **Đáp án**: b  
    **Giải thích**: Vault Agent tự động hóa việc lấy secrets trong CI/CD ([Vault Agent](https://developer.hashicorp.com/vault/docs/agent)).

---

### Chủ đề 5: Tổng hợp và Ứng dụng

21. **Unseal keys được sử dụng khi nào?**  
    a) Khi lưu trữ secrets  
    b) Khi Vault ở trạng thái sealed  
    c) Khi tạo policy  
    d) Khi tích hợp CI/CD  
    **Đáp án**: b  
    **Giải thích**: Unseal keys mở Vault khi nó ở trạng thái sealed ([Initialize and Unseal](https://developer.hashicorp.com/vault/docs/concepts/seal)).

22. **Lệnh nào xóa một secret trong KV v2 mà không xóa vĩnh viễn?**  
    a) `vault kv delete`  
    b) `vault kv destroy`  
    c) `vault kv undelete`  
    d) `vault kv soft-delete`  
    **Đáp án**: a  
    **Giải thích**: `vault kv delete` thực hiện soft delete, có thể khôi phục ([KV v2](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2)).

23. **Trong Vault, policy mặc định (default policy) cho phép gì?**  
    a) Truy cập tất cả secrets  
    b) Chỉ đọc metadata của secrets  
    c) Không cho phép truy cập secrets  
    d) Chỉ tạo secrets mới  
    **Đáp án**: c  
    **Giải thích**: Default policy hạn chế truy cập secrets, chỉ cho phép một số thao tác quản lý ([Policies](https://developer.hashicorp.com/vault/docs/concepts/policies)).

24. **Khi tích hợp Vault với ứng dụng, phương pháp nào thường được sử dụng?**  
    a) Hardcode secrets trong code  
    b) Sử dụng Vault Agent hoặc SDK  
    c) Lưu secrets trong file config  
    d) Tắt xác thực  
    **Đáp án**: b  
    **Giải thích**: Vault Agent hoặc SDK được dùng để lấy secrets an toàn ([Vault Integrations](https://developer.hashicorp.com/vault/docs/integrations)).

25. **Tính năng nào của Vault giúp quản lý vòng đời chứng chỉ SSL?**  
    a) KV Secrets Engine  
    b) Transit Secrets Engine  
    c) PKI Secrets Engine  
    d) Database Secrets Engine  
    **Đáp án**: c  
    **Giải thích**: PKI engine tạo và quản lý chứng chỉ SSL ([PKI Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/pki)).

---

## Ghi Chú
- **Số lượng**: 25 câu hỏi, bao quát các chủ đề: kiến trúc, authentication, secret engines, HA, auditing, và best practices.
- **Độ khó**: 10 câu cơ bản, 10 câu trung bình, 5 câu nâng cao.
- **Cách sử dụng**: Người học trả lời trong 1 giờ (Ngày 5). Đáp án có thể được chấm tự động hoặc thủ công.
- **Tài liệu tham khảo**: Các câu hỏi dựa trên [HashiCorp Vault Documentation](https://developer.hashicorp.com/vault/docs) và [HashiCorp Learn](https://learn.hashicorp.com/vault).
- **Mục đích**: Đánh giá kiến thức toàn diện và chuẩn bị cho chứng chỉ Vault Associate.

Nếu bạn cần thêm câu hỏi, điều chỉnh độ khó, hoặc bổ sung dạng câu hỏi khác (ví dụ: câu hỏi mở), hãy cho tôi biết!