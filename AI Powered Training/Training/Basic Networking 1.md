# Lịch Trình Đào Tạo Networking Cơ Bản cho DevOps Newbie Trong 5 Ngày (Phase 1)

## Ngày 1: Khái Niệm Networking và Giao Thức Cơ Bản

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Giới thiệu Networking trong DevOps** | - Networking là gì? Vai trò trong DevOps.<br>- Mô hình TCP/IP và các tầng cơ bản (Application, Transport, Network, Link).<br>- Các thiết bị mạng DevOps thường gặp (router, firewall, load balancer). | 2 giờ | - [Networking for DevOps](https://www.redhat.com/en/topics/devops/what-is-devops-networking)<br>- [TCP/IP Model](https://www.guru99.com/tcp-ip-model.html)<br>- [DevOps Networking Basics](https://linuxjourney.com/lesson/networking-basics) | 1. Vẽ sơ đồ mô hình TCP/IP và giải thích chức năng mỗi tầng.<br>2. Sử dụng `ip addr` trên Linux để kiểm tra cấu hình mạng máy local.<br>3. Mô tả vai trò của networking trong pipeline CI/CD với ví dụ thực tế. |
| **Giao Thức Cơ Bản (TCP/IP, UDP)** | - TCP vs. UDP: Đặc điểm và ứng dụng.<br>- Port và socket trong networking.<br>- Các lệnh kiểm tra giao thức (`netstat`, `ss`). | 2 giờ | - [TCP vs UDP](https://www.geeksforgeeks.org/differences-between-tcp-and-udp/)<br>- [Networking Ports](https://www.tutorialspoint.com/what-is-ports-in-networking) | 1. Sử dụng `netstat -tulpn` để liệt kê các port đang mở trên máy local.<br>2. Kiểm tra kết nối TCP đến `google.com:80` bằng `telnet` hoặc `nc`.<br>3. So sánh tốc độ truyền dữ liệu UDP và TCP bằng công cụ như `iperf`. |
| **Giao Thức Ứng Dụng (SSH, HTTP/HTTPS, SMTP)** | - SSH: Quản lý server từ xa.<br>- HTTP/HTTPS: Web communication.<br>- SMTP: Email delivery. | 2 giờ | - [SSH Basics](https://www.ssh.com/academy/ssh)<br>- [HTTP/HTTPS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)<br>- [SMTP Protocol](https://www.tutorialspoint.com/smtp/smtp_quick_guide.htm) | 1. Kết nối đến máy local qua SSH bằng `ssh localhost`.<br>2. Gửi yêu cầu HTTP đến `example.com` bằng `curl` và kiểm tra response.<br>3. Gửi email thử nghiệm qua SMTP bằng lệnh `mail` hoặc công cụ như `swaks`. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Tầng nào trong mô hình TCP/IP xử lý giao thức HTTP?  
   a) Application  
   b) Transport  
   c) Network  
   d) Link  
   **Đáp án**: a
2. Giao thức nào đảm bảo truyền dữ liệu đáng tin cậy?  
   a) UDP  
   b) TCP  
   c) SMTP  
   d) ICMP  
   **Đáp án**: b
3. Port mặc định của SSH là gì?  
   a) 80  
   b) 22  
   c) 443  
   d) 25  
   **Đáp án**: b
4. Lệnh nào liệt kê các port đang mở trên Linux?  
   a) netstat -tulpn  
   b) ping  
   c) ip addr  
   d) traceroute  
   **Đáp án**: a
5. SMTP được sử dụng để làm gì?  
   a) Truy cập web  
   b) Gửi email  
   c) Quản lý server  
   d) Tải file  
   **Đáp án**: b
6. Sự khác biệt giữa HTTP và HTTPS là gì?  
   a) HTTPS dùng SSL/TLS  
   b) HTTP nhanh hơn HTTPS  
   c) HTTPS không dùng port  
   d) HTTP mã hóa dữ liệu  
   **Đáp án**: a
7. Lệnh nào kiểm tra kết nối TCP?  
   a) curl  
   b) telnet  
   c) ping  
   d) ss  
   **Đáp án**: b
8. UDP phù hợp cho ứng dụng nào?  
   a) Truyền video streaming  
   b) Truy cập web  
   c) Gửi email  
   d) Quản lý server  
   **Đáp án**: a
9. Lệnh `ss -t` hiển thị gì?  
   a) Kết nối TCP  
   b) Kết nối UDP  
   c) Địa chỉ IP  
   d) Bảng định tuyến  
   **Đáp án**: a
10. Port 443 dùng cho giao thức nào?  
    a) HTTP  
    b) HTTPS  
    c) SSH  
    d) SMTP  
    **Đáp án**: b

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao networking quan trọng trong DevOps?
2. Giải thích sự khác biệt giữa TCP và UDP với ví dụ thực tế.
3. SSH được sử dụng như thế nào trong quản lý server DevOps?
4. Làm thế nào để kiểm tra một port có đang mở trên server?
5. HTTP và HTTPS khác nhau như thế nào về bảo mật?

## Ngày 2: Firewall và Bảo Mật Mạng Cơ Bản

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Firewall trong DevOps** | - Firewall là gì? Vai trò trong bảo mật.<br>- iptables và ufw trên Linux.<br>- Cấu hình firewall rules. | 3 giờ | - [iptables Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-iptables-on-ubuntu)<br>- [UFW Guide](https://www.linode.com/docs/guides/configure-firewall-with-ufw/) | 1. Cấu hình iptables để chỉ cho phép traffic SSH (port 22) trên máy local.<br>2. Sử dụng ufw để cho phép HTTP (port 80) và chặn tất cả traffic khác.<br>3. Kiểm tra firewall rules bằng `iptables -L` và thử truy cập port bị chặn. |
| **Bảo Mật Mạng Cơ Bản** | - Giới thiệu IP filtering và port security.<br>- Kiểm tra traffic bằng lệnh Linux.<br>- Best practices cho firewall trong DevOps. | 3 giờ | - [Network Security Basics](https://www.geeksforgeeks.org/network-security-basics/)<br>- [Linux Security Commands](https://www.tecmint.com/linux-server-security-tips/) | 1. Chặn một dải IP cụ thể (ví dụ: 192.168.1.100) bằng iptables.<br>2. Kiểm tra traffic đến port 80 bằng `tcpdump -i eth0 port 80`.<br>3. Viết firewall rule để chỉ cho phép traffic từ một IP cụ thể đến port 443. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Firewall dùng để làm gì?  
   a) Tăng tốc mạng  
   b) Kiểm soát traffic  
   c) Tạo IP mới  
   d) Giám sát server  
   **Đáp án**: b
2. Lệnh nào hiển thị firewall rules trong iptables?  
   a) iptables -L  
   b) ufw status  
   c) netstat -f  
   d) ss -r  
   **Đáp án**: a
3. UFW là gì?  
   a) Firewall configuration tool  
   b) Network monitoring tool  
   c) Proxy server  
   d) Load balancer  
   **Đáp án**: a
4. Lệnh nào chặn traffic đến port 80 trong iptables?  
   a) iptables -A INPUT -p tcp --dport 80 -j DROP  
   b) iptables -A OUTPUT -p tcp --sport 80 -j ACCEPT  
   c) iptables -L INPUT -p tcp --dport 80  
   d) iptables -A INPUT -p udp --dport 80 -j DROP  
   **Đáp án**: a
5. Best practice nào quan trọng khi cấu hình firewall?  
   a) Chặn tất cả traffic trước khi mở port  
   b) Mở tất cả port  
   c) Không dùng logging  
   d) Chỉ dùng UDP  
   **Đáp án**: a
6. Lệnh nào kiểm tra traffic mạng trên Linux?  
   a) tcpdump  
   b) ping  
   c) curl  
   d) telnet  
   **Đáp án**: a
7. Port security là gì?  
   a) Giới hạn truy cập dựa trên port  
   b) Tăng tốc port  
   c) Tạo port mới  
   d) Giám sát port  
   **Đáp án**: a
8. Lệnh nào cho phép traffic SSH trong ufw?  
   a) ufw allow 22  
   b) ufw deny 22  
   c) ufw status 22  
   d) ufw open 22  
   **Đáp án**: a
9. IP filtering dựa trên yếu tố nào?  
   a) Địa chỉ IP nguồn/đích  
   b) Tên miền  
   c) Giao thức ứng dụng  
   d) Tốc độ mạng  
   **Đáp án**: a
10. Tại sao cần logging trong firewall?  
    a) Theo dõi traffic bị chặn  
    b) Tăng tốc mạng  
    c) Tạo port mới  
    d) Giám sát CPU  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Tại sao firewall quan trọng trong môi trường DevOps?
2. Mô tả cách cấu hình firewall rule để bảo vệ server web.
3. Sự khác biệt giữa iptables và ufw là gì?
4. Làm thế nào để kiểm tra traffic mạng bị chặn bởi firewall?
5. Best practice nào giúp firewall hiệu quả trong DevOps?

## Ngày 3: Proxy và Reverse Proxy

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Proxy trong DevOps** | - Proxy là gì? Forward proxy vs. Reverse proxy.<br>- Ứng dụng của proxy trong DevOps.<br>- Cấu hình proxy với Nginx. | 3 giờ | - [Proxy vs Reverse Proxy](https://www.nginx.com/resources/glossary/reverse-proxy-vs-load-balancer/)<br>- [Nginx Proxy Guide](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) | 1. Cấu hình Nginx làm forward proxy để truy cập `example.com` từ máy local.<br>2. Kiểm tra proxy log trong Nginx bằng `tail -f /var/log/nginx/access.log`.<br>3. Thiết lập proxy để chặn truy cập đến một website cụ thể (ví dụ: `example.org`). |
| **Reverse Proxy** | - Reverse proxy là gì? Lợi ích (bảo mật, caching).<br>- Cấu hình reverse proxy với Nginx.<br>- Tích hợp reverse proxy với ứng dụng web. | 3 giờ | - [Reverse Proxy Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-reverse-proxy-with-nginx)<br>- [Nginx Reverse Proxy](https://www.nginx.com/resources/library/what-is-a-reverse-proxy/) | 1. Cấu hình Nginx làm reverse proxy cho ứng dụng web chạy trên `localhost:3000`.<br>2. Kích hoạt caching trong reverse proxy để cải thiện hiệu suất.<br>3. Kiểm tra truy cập ứng dụng web qua reverse proxy bằng `curl` hoặc trình duyệt. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Proxy server hoạt động như thế nào?  
   a) Trung gian giữa client và server  
   b) Tạo IP mới  
   c) Tăng tốc mạng  
   d) Giám sát server  
   **Đáp án**: a
2. Reverse proxy khác forward proxy như thế nào?  
   a) Reverse proxy phục vụ server, forward proxy phục vụ client  
   b) Reverse proxy nhanh hơn  
   c) Forward proxy bảo mật hơn  
   d) Không có khác biệt  
   **Đáp án**: a
3. Lợi ích của reverse proxy là gì?  
   a) Load balancing  
   b) Caching  
   c) Cả hai  
   d) Không có lợi ích  
   **Đáp án**: c
4. Lệnh nào kiểm tra log Nginx?  
   a) tail -f /var/log/nginx/access.log  
   b) cat /var/log/nginx/error.log  
   c) nginx -l  
   d) nginx -t  
   **Đáp án**: a
5. Reverse proxy thường được dùng trong trường hợp nào?  
   a) Bảo vệ server backend  
   b) Tăng tốc client  
   c) Tạo IP mới  
   d) Giám sát mạng  
   **Đáp án**: a
6. Nginx có thể làm gì?  
   a) Reverse proxy  
   b) Load balancer  
   c) Cả hai  
   d) Không làm được gì  
   **Đáp án**: c
7. Caching trong reverse proxy giúp gì?  
   a) Giảm tải server backend  
   b) Tăng độ trễ  
   c) Chặn traffic  
   d) Tạo port mới  
   **Đáp án**: a
8. Lệnh nào kiểm tra cấu hình Nginx?  
   a) nginx -t  
   b) nginx -c  
   c) nginx -v  
   d) nginx -l  
   **Đáp án**: a
9. Forward proxy thường được dùng để làm gì?  
   a) Ẩn danh client  
   b) Bảo vệ server  
   c) Load balancing  
   d) Tăng tốc mạng  
   **Đáp án**: a
10. Reverse proxy có thể tích hợp với ứng dụng nào?  
    a) Web server  
    b) Database  
    c) Firewall  
    d) Router  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Proxy và reverse proxy khác nhau như thế nào trong DevOps?
2. Làm thế nào để cấu hình reverse proxy với Nginx?
3. Lợi ích của caching trong reverse proxy là gì?
4. Forward proxy phù hợp trong trường hợp nào?
5. Làm thế nào để kiểm tra reverse proxy hoạt động đúng?

## Ngày 4: Load Balancer và Quản Lý Traffic

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Load Balancer trong DevOps** | - Load balancer là gì? Lợi ích (HA, scalability).<br>- Layer 4 vs. Layer 7 load balancing.<br>- Cấu hình load balancer với HAProxy. | 3 giờ | - [Load Balancing Basics](https://www.nginx.com/resources/glossary/load-balancing/)<br>- [HAProxy Guide](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/) | 1. Cấu hình HAProxy để phân phối traffic đến 2 server web (Docker container chạy Nginx).<br>2. Kiểm tra load balancer bằng `curl` để xác nhận traffic được phân phối.<br>3. Thêm health check trong HAProxy để phát hiện server backend down. |
| **Quản Lý Traffic** | - Sticky sessions và session persistence.<br>- Rate limiting và throttling.<br>- Best practices cho load balancing. | 3 giờ | - [HAProxy Sticky Sessions](https://www.haproxy.com/blog/introduction-to-haproxy-stick-tables/)<br>- [Rate Limiting with Nginx](https://www.nginx.com/blog/rate-limiting-nginx/) | 1. Cấu hình sticky sessions trong HAProxy để giữ session người dùng.<br>2. Thiết lập rate limiting trong Nginx để giới hạn số request từ một IP.<br>3. Kiểm tra traffic log trong HAProxy để phân tích phân phối load. |

**Tổng thời gian**: 6 giờ

**MCQ (10 câu)**:
1. Load balancer dùng để làm gì?  
   a) Phân phối traffic  
   b) Tạo IP mới  
   c) Tăng tốc mạng  
   d) Giám sát server  
   **Đáp án**: a
2. Layer 7 load balancing dựa trên gì?  
   a) IP và port  
   b) HTTP headers  
   c) MAC address  
   d) VLAN ID  
   **Đáp án**: b
3. HAProxy hoạt động ở tầng nào?  
   a) Layer 4 và Layer 7  
   b) Layer 2  
   c) Layer 3  
   d) Layer 1  
   **Đáp án**: a
4. Sticky sessions dùng để làm gì?  
   a) Giữ session người dùng  
   b) Tăng tốc mạng  
   c) Chặn traffic  
   d) Tạo port mới  
   **Đáp án**: a
5. Lệnh nào kiểm tra cấu hình HAProxy?  
   a) haproxy -c -f /etc/haproxy/haproxy.cfg  
   b) haproxy -t  
   c) haproxy -v  
   d) haproxy -l  
   **Đáp án**: a
6. Rate limiting giúp gì trong DevOps?  
   a) Ngăn DDoS  
   b) Tăng tốc mạng  
   c) Tạo IP mới  
   d) Giám sát server  
   **Đáp án**: a
7. Health check trong load balancer là gì?  
   a) Kiểm tra trạng thái server backend  
   b) Tăng tốc traffic  
   c) Chặn traffic  
   d) Tạo port mới  
   **Đáp án**: a
8. Lệnh nào kiểm tra log HAProxy?  
   a) tail -f /var/log/haproxy.log  
   b) cat /var/log/haproxy/error.log  
   c) haproxy -l  
   d) haproxy -t  
   **Đáp án**: a
9. Layer 4 load balancing dựa trên gì?  
   a) IP và port  
   b) HTTP headers  
   c) Application data  
   d) Session ID  
   **Đáp án**: a
10. Best practice nào quan trọng cho load balancer?  
    a) Sử dụng health check  
    b) Tắt logging  
    c) Chỉ dùng Layer 4  
    d) Không dùng rate limiting  
    **Đáp án**: a

**Câu hỏi vấn đáp (5 câu)**:
1. Load balancer giúp cải thiện hiệu suất ứng dụng như thế nào?
2. Mô tả sự khác biệt giữa Layer 4 và Layer 7 load balancing.
3. Sticky sessions có vai trò gì trong ứng dụng web?
4. Làm thế nào để thiết lập rate limiting trong DevOps?
5. Best practice nào đảm bảo load balancer hoạt động hiệu quả?

## Ngày 5: Giám Sát Mạng Cơ Bản và Final Lab

| **Chủ đề** | **Bài học** | **Thời lượng** | **Tài liệu tham khảo** | **Bài tập thực hành** |
|------------|-------------|----------------|------------------------|-----------------------|
| **Giám Sát Mạng Cơ Bản** | - Công cụ giám sát mạng (ping, tcpdump, netstat).<br>- Phân tích traffic và xử lý lỗi cơ bản.<br>- Logging trong DevOps networking. | 2.5 giờ | - [tcpdump Tutorial](https://www.tutorialspoint.com/tcpdump/tcpdump_introduction.htm)<br>- [Netstat Guide](https://www.geeksforgeeks.org/netstat-command-linux/)<br>- [Network Troubleshooting](https://www.redhat.com/sysadmin/network-troubleshooting-commands) | 1. Sử dụng `tcpdump -i eth0 port 80` để capture traffic HTTP.<br>2. Kiểm tra kết nối mạng bằng `ping` và phân tích độ trễ.<br>3. Kiểm tra các kết nối đang mở bằng `netstat -tulpn` và xác định ứng dụng. |
| **Final Lab** | Triển khai ứng dụng web với firewall, reverse proxy, và load balancer, sử dụng Nginx, HAProxy, và iptables. | 3.5 giờ | - [Nginx Documentation](https://docs.nginx.com/)<br>- [HAProxy Documentation](https://www.haproxy.com/documentation/)<br>- [iptables Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-iptables-on-ubuntu) | **Mô tả**: Triển khai ứng dụng web đơn giản (Nginx) với firewall, reverse proxy, và load balancer trên máy local Linux.<br>**Yêu cầu**:<br>- **Môi trường**: Máy local Ubuntu với Docker Desktop, Nginx, HAProxy, iptables.<br>- **Đề mục**:<br>  1. **Thiết lập ứng dụng**: Chạy 2 container Nginx làm web server (port 8081, 8082).<br>  2. **Firewall**: Cấu hình iptables để chỉ cho phép traffic SSH (22), HTTP (80), và port load balancer (8080).<br>  3. **Reverse proxy**: Sử dụng Nginx làm reverse proxy để chuyển traffic từ `localhost:80` đến 2 web server.<br>  4. **Load balancer**: Cấu hình HAProxy để phân phối traffic đến 2 web server, thêm health check.<br>  5. **Giám sát**: Sử dụng `tcpdump` và `netstat` để kiểm tra traffic và log HAProxy/Nginx.<br>  6. **Tài liệu**: Cung cấp README.md với hướng dẫn tái tạo, sơ đồ mạng, và cấu hình.<br>**Guideline**:<br>- Sử dụng container Nginx chính thức từ Docker Hub.<br>- Đảm bảo ứng dụng web truy cập được qua `http://localhost`.<br>- Kiểm tra firewall chặn traffic không hợp lệ (ví dụ: port 443).<br>- Kiểm tra load balancer phân phối traffic đều bằng log HAProxy.<br>- Tài liệu hóa cấu hình (IP, port, firewall rules, proxy/load balancer).<br>- Đảm bảo giải pháp tái tạo được trên máy khác. |

**Tổng thời gian**: 6 giờ

**MCQ (20 câu)**:
1. Tầng nào của TCP/IP xử lý giao thức SSH?  
   a) Application  
   b) Transport  
   c) Network  
   d) Link  
   **Đáp án**: a
2. Port mặc định của HTTP là gì?  
   a) 22  
   b) 80  
   c) 443  
   d) 25  
   **Đáp án**: b
3. Lệnh nào chặn traffic đến port 443 trong iptables?  
   a) iptables -A INPUT -p tcp --dport 443 -j DROP  
   b) iptables -A OUTPUT -p tcp --sport 443 -j ACCEPT  
   c) iptables -L INPUT -p tcp --dport 443  
   d) iptables -A INPUT -p udp --dport 443 -j DROP  
   **Đáp án**: a
4. Reverse proxy giúp gì trong DevOps?  
   a) Bảo vệ server backend  
   b) Tăng tốc client  
   c) Tạo IP mới  
   d) Giám sát mạng  
   **Đáp án**: a
5. Load balancer Layer 7 dựa trên gì?  
   a) HTTP headers  
   b) IP và port  
   c) MAC address  
   d) VLAN ID  
   **Đáp án**: a
6. Lệnh nào kiểm tra kết nối TCP trên Linux?  
   a) telnet  
   b) ping  
   c) curl  
   d) tcpdump  
   **Đáp án**: a
7. SMTP dùng port nào?  
   a) 25  
   b) 80  
   c) 22  
   d) 443  
   **Đáp án**: a
8. Lệnh nào kiểm tra log Nginx?  
   a) tail -f /var/log/nginx/access.log  
   b) cat /var/log/nginx/error.log  
   c) nginx -l  
   d) nginx -t  
   **Đáp án**: a
9. Health check trong HAProxy làm gì?  
   a) Kiểm tra trạng thái server backend  
   b) Tăng tốc traffic  
   c) Chặn traffic  
   d) Tạo port mới  
   **Đáp án**: a
10. UDP phù hợp cho ứng dụng nào?  
    a) Video streaming  
    b) Web browsing  
    c) Email delivery  
    d) Server management  
    **Đáp án**: a
*(10 câu tiếp theo tương tự, bao quát firewall, proxy, load balancer, giao thức, và giám sát mạng)*

**Câu hỏi vấn đáp (5 câu)**:
1. Mô tả các bước triển khai ứng dụng web với firewall, reverse proxy, và load balancer.
2. Làm thế nào để giám sát traffic mạng trong DevOps?
3. Tại sao cần reverse proxy và load balancer trong ứng dụng web?
4. Giải thích cách khắc phục lỗi traffic bị chặn bởi firewall.
5. Lợi ích của việc sử dụng giao thức HTTPS trong DevOps là gì?

## Ghi Chú
- **Tổng thời gian**: 30 giờ (6 giờ/ngày).
- **Môi trường thực hành**: Máy local Ubuntu với Docker Desktop, Nginx, HAProxy, iptables, hoặc lab trực tuyến như [KodeKloud](https://kodekloud.com/free-labs/).
- **Tài liệu chính**: Nginx, HAProxy, iptables documentation, và Linux networking guides.
- **Final Lab**: Dự án thực tế, đơn giản, tập trung vào firewall, reverse proxy, và load balancer, phù hợp với DevOps newbie.
- **Đánh giá**: MCQ và câu hỏi vấn đáp củng cố kiến thức; Final Lab kiểm tra khả năng áp dụng thực tế.