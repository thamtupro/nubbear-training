# Lịch Trình Đào Tạo HashiCorp Vagrant Trong 5 Ngày (Điều Chỉnh)

## Ngày 1: Giới Thiệu về Vagrant

| Chủ đề | Bài học | Thời lượng | Tài liệu tham khảo | Bài tập thực hành |
|--------|---------|------------|--------------------|-------------------|
| **What is Vagrant?** | Tổng quan về Vagrant, mục đích, và lợi ích trong phát triển phần mềm. | 1.5 giờ | [What is Vagrant?](https://developer.hashicorp.com/vagrant/docs/introduction) | 1. Cài đặt Vagrant và VirtualBox, kiểm tra phiên bản bằng `vagrant --version`.<br>2. Khám phá danh sách box công khai trên Vagrant Cloud.<br>3. Tạo một thư mục dự án và khởi tạo Vagrantfile mẫu bằng `vagrant init`. |
| **Getting Started with Vagrant** | Cài đặt Vagrant, hiểu về Vagrantfile, và các lệnh cơ bản (`vagrant up`, `vagrant ssh`). | 2 giờ | [Getting Started](https://developer.hashicorp.com/vagrant/docs/getting-started) | 1. Tạo Vagrantfile sử dụng box `hashicorp/bionic64`, chạy `vagrant up` để khởi động VM.<br>2. Đăng nhập vào VM bằng `vagrant ssh` và kiểm tra hệ điều hành.<br>3. Tạo một VM khác với box `centos/7` và kiểm tra trạng thái bằng `vagrant status`. |
| **Managing Virtual Machines** | Sử dụng các lệnh Vagrant để khởi động, tắt, tạm dừng, và hủy VM (`vagrant halt`, `vagrant suspend`, `vagrant destroy`). | 2 giờ | [Vagrant Commands](https://developer.hashicorp.com/vagrant/docs/cli) | 1. Tạm dừng VM bằng `vagrant suspend` và khôi phục bằng `vagrant resume`.<br>2. Hủy VM bằng `vagrant destroy` và khởi động lại để kiểm tra.<br>3. Tạo snapshot của VM bằng `vagrant snapshot save` và khôi phục bằng `vagrant snapshot restore`. |

**Tổng thời gian**: 5.5 giờ

**MCQ (10 câu)**:
1. Vagrant là công cụ dùng để làm gì?  
   a) Quản lý secrets  
   b) Quản lý môi trường máy ảo  
   c) Tự động hóa CI/CD  
   d) Giám sát hệ thống  
   **Đáp án**: b
2. Lệnh nào khởi động một VM trong Vagrant?  
   a) vagrant start  
   b) vagrant up  
   c) vagrant run  
   d) vagrant init  
   **Đáp án**: b
3. File nào định nghĩa cấu hình Vagrant?  
   a) Vagrantfile  
   b) Configfile  
   c) Boxfile  
   d) VMfile  
   **Đáp án**: a
4. Lệnh nào dùng để đăng nhập vào VM?  
   a) vagrant login  
   b) vagrant ssh  
   c) vagrant connect  
   d) vagrant access  
   **Đáp án**: b
5. Box trong Vagrant là gì?  
   a) Một file cấu hình  
   b) Một máy ảo được đóng gói  
   c) Một plugin  
   d) Một lệnh CLI  
   **Đáp án**: b
6. Lệnh nào hủy một VM?  
   a) vagrant halt  
   b) vagrant destroy  
   c) vagrant stop  
   d) vagrant delete  
   **Đáp án**: b
7. Provider mặc định của Vagrant là gì?  
   a) Docker  
   b) VirtualBox  
   c) AWS  
   d) Hyper-V  
   **Đáp án**: b
8. Lệnh nào kiểm tra trạng thái VM?  
   a) vagrant status  
   b) vagrant check  
   c) vagrant info  
   d) vagrant list  
   **Đáp án**: a
9. Lệnh nào tạo snapshot của VM?  
   a) vagrant snapshot save  
   b) vagrant backup  
   c) vagrant save  
   d) vagrant snapshot create  
   **Đáp án**: a
10. Vagrant Cloud được dùng để làm gì?  
    a) Lưu trữ secrets  
    b) Chia sẻ và tải box  
    c) Tích hợp CI/CD  
    d) Quản lý plugins  
    **Đáp án**: b

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao Vagrant được sử dụng trong phát triển phần mềm? Lợi ích chính là gì?
2. Mô tả quy trình khởi động một VM bằng Vagrant.
3. Sự khác biệt giữa `vagrant halt` và `vagrant suspend` là gì?
4. Làm thế nào để chọn một box phù hợp từ Vagrant Cloud?
5. Tại sao cần sử dụng snapshot trong quản lý VM?

## Ngày 2: Cấu Hình Môi Trường Vagrant

| Chủ đề | Bài học | Thời lượng | Tài liệu tham khảo | Bài tập thực hành |
|--------|---------|------------|--------------------|-------------------|
| **Vagrantfile Basics** | Hiểu về cấu trúc và cú pháp của Vagrantfile (box, provider, cấu hình VM). | 2 giờ | [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile) | 1. Tạo Vagrantfile với box `ubuntu/focal64`, cấu hình 2GB RAM và 2 CPU.<br>2. Thêm comment vào Vagrantfile để giải thích các cấu hình.<br>3. Thử thay đổi provider từ VirtualBox sang Docker (nếu hỗ trợ). |
| **Provisioning with Vagrant** | Giới thiệu provisioning với shell scripts, Ansible, Chef, hoặc Puppet. | 2.5 giờ | [Provisioning](https://developer.hashicorp.com/vagrant/docs/provisioning) | 1. Viết shell script provisioner cài đặt Nginx và tạo trang web tĩnh.<br>2. Sử dụng Ansible provisioner để cài đặt Apache trên VM.<br>3. Tạo một file provisioner để cập nhật hệ thống và cài đặt `git`. |
| **Networking in Vagrant** | Tùy chọn networking: port forwarding, private networks, public networks. | 2 giờ | [Networking](https://developer.hashicorp.com/vagrant/docs/networking) | 1. Thiết lập port forwarding để truy cập Nginx trên VM qua `localhost:8080`.<br>2. Cấu hình private network với IP tĩnh cho VM.<br>3. Thử cấu hình public network và kiểm tra truy cập từ máy khác. |

**Tổng thời gian**: 6.5 giờ

**MCQ (10 câu)**:
1. Vagrantfile sử dụng ngôn ngữ nào?  
   a) Python  
   b) Ruby  
   c) YAML  
   d) JSON  
   **Đáp án**: b
2. Lệnh nào kiểm tra cú pháp Vagrantfile?  
   a) vagrant validate  
   b) vagrant check  
   c) vagrant syntax  
   d) vagrant test  
   **Đáp án**: a
3. Provisioning trong Vagrant dùng để làm gì?  
   a) Cấu hình networking  
   b) Tự động hóa cài đặt phần mềm  
   c) Quản lý snapshot  
   d) Chia sẻ box  
   **Đáp án**: b
4. Loại networking nào cho phép VM giao tiếp với host?  
   a) Private network  
   b) Public network  
   c) Port forwarding  
   d) NAT  
   **Đáp án**: c
5. Lệnh nào chạy provisioner mà không khởi động lại VM?  
   a) vagrant provision  
   b) vagrant reload  
   c) v ressource  
   d) vagrant up --provision  
   **Đáp án**: a
6. Cú pháp nào cấu hình RAM trong Vagrantfile?  
   a) vb.memory = "2048"  
   b) vm.ram = 2048  
   c) memory = 2048  
   d) vb.ram = "2048"  
   **Đáp án**: a
7. Shell provisioner thường được lưu ở đâu?  
   a) Inline trong Vagrantfile  
   b) File riêng  
   c) Cả hai  
   d) Trong box  
   **Đáp án**: c
8. Private network sử dụng loại IP nào?  
   a) Public IP  
   b) DHCP  
   c) Static IP  
   d) Cả b và c  
   **Đáp án**: d
9. Lệnh nào reload VM với provisioning?  
   a) vagrant reload  
   b) vagrant reload --provision  
   c) vagrant up --reload  
   d) vagrant restart  
   **Đáp án**: b
10. Networking nào phù hợp cho môi trường production?  
    a) Port forwarding  
    b) Private network  
    c) Public network  
    d) NAT  
    **Đáp án**: c

**Câu hỏi vấn đáp (5 câu)**:
1. Mô tả cấu trúc cơ bản của một Vagrantfile.
2. Tại sao cần provisioning trong Vagrant? So sánh shell và Ansible provisioner.
3. Làm thế nào để cấu hình private network trong Vagrant?
4. Khi nào nên sử dụng port forwarding thay vì private network?
5. Làm thế nào để đảm bảo Vagrantfile có thể tái sử dụng trên nhiều hệ thống?

## Ngày 3: Các Tính Năng Nâng Cao Của Vagrant

| Chủ đề | Bài học | Thời lượng | Tài liệu tham khảo | Bài tập thực hành |
|--------|---------|------------|--------------------|-------------------|
| **Multi-Machine Setups** | Cấu hình nhiều VM trong một Vagrantfile để mô phỏng môi trường phức tạp. | 2.5 giờ | [Multi-Machine](https://developer.hashicorp.com/vagrant/docs/multi-machine) | 1. Tạo Vagrantfile với hai VM (web và db), cấu hình private network.<br>2. Thiết lập giao tiếp giữa hai VM bằng `ping`.<br>3. Sử dụng Ansible để cấu hình Nginx trên VM web và MySQL trên VM db. |
| **Vagrant Cloud** | Hiểu về Vagrant Cloud, boxes, và cách chia sẻ hoặc sử dụng boxes công khai. | 2 giờ | [Vagrant Cloud](https://www.vagrantup.com/vagrant-cloud) | 1. Tải box `ubuntu/jammy64` từ Vagrant Cloud và sử dụng trong Vagrantfile.<br>2. Tạo một box tùy chỉnh từ VM hiện có bằng `vagrant package`.<br>3. Chia sẻ box tùy chỉnh lên Vagrant Cloud (hoặc mô phỏng). |
| **Vagrant Plugins** | Mở rộng chức năng của Vagrant với plugins (caching, disk management). | 2 giờ | [Plugins](https://developer.hashicorp.com/vagrant/docs/plugins) | 1. Cài đặt plugin `vagrant-vbguest` để tự động cập nhật VirtualBox Guest Additions.<br>2. Sử dụng plugin `vagrant-cachier` để tăng tốc provisioning.<br>3. Cài đặt plugin `vagrant-disksize` để tăng kích thước ổ đĩa VM. |

**Tổng thời gian**: 6.5 giờ

**MCQ (10 câu)**:
1. Multi-machine trong Vagrant dùng để làm gì?  
   a) Chạy nhiều box trong một VM  
   b) Cấu hình nhiều VM trong một Vagrantfile  
   c) Tăng tốc provisioning  
   d) Quản lý snapshot  
   **Đáp án**: b
2. Lệnh nào liệt kê các VM trong multi-machine setup?  
   a) vagrant status  
   b) vagrant list  
   c) vagrant machines  
   d) vagrant show  
   **Đáp án**: a
3. Vagrant Cloud cung cấp tính năng gì?  
   a) Quản lý plugins  
   b) Lưu trữ và chia sẻ box  
   c) Tích hợp CI/CD  
   d) Debug Vagrantfile  
   **Đáp án**: b
4. Lệnh nào gói một VM thành box?  
   a) vagrant package  
   b) vagrant box create  
   c) vagrant export  
   d) vagrant save  
   **Đáp án**: a
5. Plugin `vagrant-vbguest` dùng để làm gì?  
   a) Tăng tốc provisioning  
   b) Cập nhật Guest Additions  
   c) Quản lý disk  
   d) Tích hợp CI/CD  
   **Đáp án**: b
6. Lệnh nào cài đặt plugin?  
   a) vagrant plugin install  
   b) vagrant install plugin  
   c) vagrant add plugin  
   d) vagrant plugin add  
   **Đáp án**: a
7. Box từ Vagrant Cloud được thêm bằng lệnh nào?  
   a) vagrant box add  
   b) vagrant box install  
   c) vagrant box download  
   d) vagrant box import  
   **Đáp án**: a
8. Plugin nào tăng tốc provisioning bằng cách cache package?  
   a) vagrant-cachier  
   b) vagrant-vbguest  
   c) vagrant-disksize  
   d) vagrant-share  
   **Đáp án**: a
9. Lệnh nào kiểm tra danh sách plugin đã cài?  
   a) vagrant plugin list  
   b) vagrant plugins  
   c) vagrant list plugins  
   d) vagrant show plugins  
   **Đáp án**: a
10. Multi-machine setup thường dùng cho môi trường nào?  
    a) Đơn lẻ  
    b) Phức tạp, nhiều server  
    c) CI/CD pipeline  
    d) Snapshot management  
    **Đáp án**: b

**Câu hỏi vấn đáp (5 câu)**:
1. Lợi ích của multi-machine setup so với single VM là gì?
2. Làm thế nào để chia sẻ một box tùy chỉnh qua Vagrant Cloud?
3. Mô tả cách sử dụng plugin để cải thiện hiệu suất Vagrant.
4. Khi nào nên sử dụng multi-machine setup trong dự án thực tế?
5. Làm thế nào để kiểm tra giao tiếp giữa các VM trong multi-machine setup?

## Ngày 4: Best Practices và Troubleshooting

| Chủ đề | Bài học | Thời lượng | Tài liệu tham khảo | Bài tập thực hành |
|--------|---------|------------|--------------------|-------------------|
| **Best Practices for Vagrant** | Mẹo viết Vagrantfile hiệu quả, quản lý phiên bản với Git, hợp tác nhóm. | 2 giờ | [Best Practices](https://developer.hashicorp.com/vagrant/docs/best-practices) | 1. Refactor Vagrantfile để thêm comment và tổ chức cấu trúc rõ ràng.<br>2. Lưu Vagrantfile vào Git repository và đẩy lên GitHub.<br>3. Tạo Vagrantfile với biến môi trường để tái sử dụng trên nhiều hệ thống. |
| **Troubleshooting Vagrant** | Các vấn đề thường gặp (lỗi box, networking, provisioning) và cách debug. | 2 giờ | [Troubleshooting](https://developer.hashicorp.com/vagrant/docs/troubleshooting) | 1. Cố tình gây lỗi box không tồn tại và khắc phục bằng cách kiểm tra log.<br>2. Debug lỗi networking (port conflict) và sửa trong Vagrantfile.<br>3. Kiểm tra lỗi provisioning và sửa bằng cách chạy `vagrant provision --debug`. |
| **Integrating Vagrant with CI/CD** | Sử dụng Vagrant trong pipeline CI/CD để kiểm tra môi trường phát triển. | 2.5 giờ | [CI/CD Integration](https://developer.hashicorp.com/vagrant/docs/integration) | 1. Tạo pipeline GitHub Actions để chạy `vagrant up` và test môi trường.<br>2. Tích hợp Vagrant với Jenkins để kiểm tra provisioning.<br>3. Viết script kiểm tra trạng thái VM trong CI/CD pipeline. |

**Tổng thời gian**: 6.5 giờ

**MCQ (10 câu)**:
1. Best practice nào quan trọng khi viết Vagrantfile?  
   a) Thêm comment  
   b) Sử dụng inline scripts  
   c) Không dùng version control  
   d) Sử dụng public network  
   **Đáp án**: a
2. Lệnh nào chạy Vagrant với debug mode?  
   a) vagrant up --debug  
   b) vagrant debug  
   c) vagrant run --debug  
   d) vagrant provision --debug  
   **Đáp án**: a
3. Lỗi box không tồn tại được khắc phục bằng lệnh nào?  
   a) vagrant box add  
   b) vagrant box install  
   c) vagrant box download  
   d) vagrant box update  
   **Đáp án**: a
4. Vagrant tích hợp với CI/CD thường sử dụng công cụ nào?  
   a) Jenkins  
   b) GitHub Actions  
   c) Cả hai  
   d) Ansible  
   **Đáp án**: c
5. Lệnh nào kiểm tra lỗi provisioning?  
   a) vagrant provision --debug  
   b) vagrant debug provision  
   c) vagrant check provision  
   d) vagrant provision --test  
   **Đáp án**: a
6. Tại sao nên dùng Git cho Vagrantfile?  
   a) Tăng tốc provisioning  
   b) Quản lý phiên bản  
   c) Debug networking  
   d) Tích hợp CI/CD  
   **Đáp án**: b
7. Lỗi port conflict thuộc về vấn đề nào?  
   a) Provisioning  
   b) Networking  
   c) Box  
   d) Plugin  
   **Đáp án**: b
8. Lệnh nào cập nhật box?  
   a) vagrant box update  
   b) vagrant box refresh  
   c) vagrant box upgrade  
   d) vagrant box install  
   **Đáp án**: a
9. CI/CD pipeline thường kiểm tra gì với Vagrant?  
   a) Môi trường phát triển  
   b) Secrets management  
   c) Snapshot  
   d) Plugin installation  
   **Đáp án**: a
10. Log Vagrant được tìm thấy ở đâu?  
    a) vagrant.log  
    b) debug.log  
    c) Cả hai  
    d) Không có log  
    **Đáp án**: c

**Câu hỏi vấn đáp (5 câu)**:
1. Làm thế nào để tổ chức Vagrantfile theo best practices?
2. Mô tả cách debug một lỗi networking trong Vagrant.
3. Tại sao nên tích hợp Vagrant vào pipeline CI/CD?
4. Làm thế nào để xử lý lỗi box không tương thích với provider?
5. Lợi ích của việc sử dụng version control cho Vagrantfile?

## Ngày 5: Final Lab và Đánh Giá

| Chủ đề | Bài học | Thời lượng | Tài liệu tham khảo | Bài tập thực hành |
|--------|---------|------------|--------------------|-------------------|
| **Final Lab** | Thiết lập môi trường phát triển hoàn chỉnh với web server, database server, và load balancer, sử dụng Vagrant, Ansible, và networking. | 4.5 giờ | [Vagrant Documentation](https://developer.hashicorp.com/vagrant/docs) | **Mô tả**: Thiết lập môi trường phát triển với:<br>- Ba VM: web server (Nginx), database server (MySQL), và load balancer (HAProxy).<br>- Sử dụng Ansible để provisioning phần mềm.<br>- Thiết lập private network và port forwarding để truy cập dịch vụ.<br>- Lưu Vagrantfile và scripts vào Git repository.<br>**Yêu cầu**:<br>- **Môi trường**: Máy local với VirtualBox, 3 VM, box `ubuntu/jammy64`.<br>- **Đề mục**:<br>  1. **Vagrantfile Setup**: Tạo Vagrantfile với 3 VM, cấu hình RAM, CPU, và private network.<br>  2. **Provisioning**: Sử dụng Ansible để cài đặt Nginx, MySQL, HAProxy, và cấu hình dịch vụ.<br>  3. **Networking**: Thiết lập private network để giao tiếp giữa các VM, port forwarding để truy cập web server qua `localhost:8080`.<br>  4. **Version Control**: Đẩy Vagrantfile và Ansible playbooks lên Git repository.<br>  5. **Testing**: Kiểm tra trạng thái VM, dịch vụ, và truy cập web qua load balancer.<br>**Guideline**:<br>- Sử dụng box chính thức từ Vagrant Cloud.<br>- Đảm bảo Vagrantfile tuân thủ best practices (comment, cấu trúc rõ ràng).<br>- Kiểm tra kết nối SSH giữa VM và host.<br>- Sử dụng Ansible roles để tổ chức provisioning.<br>- Đảm bảo dịch vụ Nginx, MySQL, HAProxy hoạt động và giao tiếp được.<br>- Trang web phải truy cập được qua `http://localhost:8080`.<br>- Lưu trữ mã nguồn trên GitHub để tái sử dụng. |
| **MCQ** | Bài kiểm tra trắc nghiệm về các khái niệm và thao tác trong Vagrant. | 1.5 giờ | [Vagrant Documentation](https://developer.hashicorp.com/vagrant/docs) | Tạo và trả lời 20-30 câu hỏi trắc nghiệm về Vagrantfile, provisioning, networking, multi-machine, Vagrant Cloud, plugins, best practices, và CI/CD. Sample MCQs:<br>1. Lệnh nào khởi động tất cả VM trong multi-machine setup? (a) vagrant up **(Đáp án: a)**<br>2. Provisioner nào phù hợp cho quản lý cấu hình phức tạp? (a) Shell (b) Ansible **(Đáp án: b)**<br>3. Networking nào cho phép truy cập từ mạng bên ngoài? (a) Private (b) Public **(Đáp án: b)**<br>4. Plugin `vagrant-cachier` dùng để? (a) Cache package **(Đáp án: a)**<br>5. Lệnh nào kiểm tra cú pháp Vagrantfile? (a) vagrant validate **(Đáp án: a)** |

**Tổng thời gian**: 6 giờ

## Ghi Chú
- **Tổng thời gian**: 33 giờ (6-7 giờ/ngày).
- **Môi trường thực hành**: Máy local với VirtualBox hoặc [HashiCorp Learn](https://learn.hashicorp.com/vagrant), [KodeKloud](https://kodekloud.com/free-labs/vagrant).
- **Tài liệu chính**: [HashiCorp Vagrant Documentation](https://developer.hashicorp.com/vagrant/docs).
- **Final Lab**: Yêu cầu tích hợp kiến thức từ ngày 1-4, tập trung vào CLI, Ansible, và networking.
- **Đánh giá**: MCQ và câu hỏi vấn đáp giúp củng cố kiến thức; Final Lab đánh giá khả năng áp dụng thực tế.