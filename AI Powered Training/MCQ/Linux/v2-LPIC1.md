// TOPIC 101: SYSTEM ARCHITECTURE
// question: 101.1.1  name: 101.1 Determine and configure hardware settings
$CATEGORY: $module$/top/TOPIC 101: SYSTEM ARCHITECTURE/101.1 Determine and configure hardware settings

::101.1 Determine and configure hardware settings::[html]<p>Trong các hệ thống Linux, các thiết bị NVMe (SSD kết nối với bus PCI Express) được đặt tiền tố đường dẫn nào cho các thiết bị khối?</p>{
	~[moodle]A. /dev/sdb.#<p>Đây là quy ước đặt tên truyền thống cho các thiết bị khối SATA/SCSI/IDE thứ cấp.</p>
	~[moodle]B. /dev/pci.#<p>Tiền tố này không phải là định dạng tiêu chuẩn cho tên thiết bị khối trong Linux.</p>
	=[moodle]C. /dev/nvme.
	~[moodle]D. /dev/mmcblk.#<p>Tiền tố mmcblk được sử dụng cho thẻ nhớ SD (SD cards).</p>
	####<p><strong>Giải thích</strong>: Các thiết bị NVMe nhận tiền tố là nvme, ví dụ như /dev/nvme0n1p1 và /dev/nvme0n1p2.</p>
}

// question: 101.1.2  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Nếu một hệ điều hành không thể khởi động sau khi thêm đĩa SATA thứ hai vào hệ thống (biết rằng tất cả các bộ phận đều không bị lỗi), nguyên nhân có thể xảy ra là gì?</p>{
	~[moodle]A. Hạt nhân (kernel) không hỗ trợ SATA.#<p>Nếu hệ điều hành đã từng hoạt động, vấn đề không phải là kernel không hỗ trợ SATA.</p>
	~[moodle]B. Cần phải cấu hình lại bootloader (bộ tải khởi động) trong MBR.#<p>Mặc dù đây có thể là một vấn đề, nguyên nhân trực tiếp hơn thường là do BIOS không biết chọn thiết bị nào để tìm kiếm bootstrap.</p>
	=[moodle]C. Thứ tự thiết bị khởi động (boot device order) chưa được cấu hình trong tiện ích thiết lập BIOS.
	~[moodle]D. Ổ đĩa mới không được format với hệ thống tập tin journaling.#<p>Việc thiếu hệ thống tập tin journaling sẽ không ngăn cản việc khởi động.</p>
	####<p><strong>Giải thích</strong>: Thứ tự thiết bị khởi động phải được cấu hình trong tiện ích thiết lập BIOS, nếu không BIOS có thể không thể chạy bootloader.</p>
}

// question: 101.1.3  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Cấu hình firmware nào có các tính năng tinh vi hơn BIOS, cung cấp các tính năng nhận dạng, kiểm tra, cấu hình và nâng cấp firmware tiên tiến?</p>{
	~[moodle]A. MBR.#<p>MBR là một kiểu bảng phân vùng, không phải firmware.</p>
	~[moodle]B. GPT.#<p>GPT là một kiểu bảng phân vùng.</p>
	~[moodle]C. NVRAM.#<p>NVRAM là bộ nhớ lưu trữ các định nghĩa khởi động của UEFI.</p>
	=[moodle]D. UEFI.
	####<p><strong>Giải thích</strong>: UEFI (Unified Extensible Firmware Interface) là triển khai mới hơn và tinh vi hơn, mặc dù người ta vẫn thường gọi tiện ích cấu hình là BIOS.</p>
}

// question: 101.1.4  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong Linux, để lấy thông tin chi tiết về các lỗi đã biết (bugs) của CPU, ta cần kiểm tra tệp nào và tìm dòng nào?</p>{
	~[moodle]A. Tệp /proc/devices, dòng cpu_meltdown.#<p>Đây là các tệp hoặc cú pháp không chính xác để tìm thông tin lỗi CPU theo tài liệu.</p>
	=[moodle]B. Tệp /proc/cpuinfo, dòng bugs: cpu_meltdown.
	~[moodle]C. Tệp /sys/devices/cpu/info, dòng bugs.#<p>Đây là các tệp hoặc cú pháp không chính xác để tìm thông tin lỗi CPU theo tài liệu.</p>
	~[moodle]D. Tệp /proc/meminfo, dòng bugs.#<p>Đây là các tệp hoặc cú pháp không chính xác để tìm thông tin lỗi CPU theo tài liệu.</p>
	####<p><strong>Giải thích</strong>: Tệp /proc/cpuinfo có một dòng hiển thị các lỗi đã biết cho CPU tương ứng, ví dụ: bugs: cpu_meltdown.</p>
}

// question: 101.1.5  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong các hệ thống cũ (legacy machines), làm thế nào để tránh vấn đề một số máy chủ x86 với firmware BIOS cũ không thể khởi động nếu không phát hiện thấy bàn phím?</p>{
	~[moodle]A. Cài đặt firmware UEFI thay vì BIOS.#<p>Đây là các giải pháp không chính xác hoặc không được đề cập là cách giải quyết trực tiếp cho vấn đề này trong ngữ cảnh hệ thống cũ.</p>
	~[moodle]B. Cấu hình lại bootloader để bỏ qua lỗi.#<p>Đây là các giải pháp không chính xác hoặc không được đề cập là cách giải quyết trực tiếp cho vấn đề này trong ngữ cảnh hệ thống cũ.</p>
	=[moodle]C. Thay đổi cài đặt trong tiện ích cấu hình BIOS/UEFI.
	~[moodle]D. Tải kernel Linux với tham số nokeyboard.#<p>Đây là các giải pháp không chính xác hoặc không được đề cập là cách giải quyết trực tiếp cho vấn đề này trong ngữ cảnh hệ thống cũ.</p>
	####<p><strong>Giải thích</strong>: Vấn đề này có thể được tránh bằng cách thay đổi cài đặt trong tiện ích cấu hình BIOS/UEFI (mặc dù câu trả lời đầy đủ không được cung cấp, ngữ cảnh của câu hỏi Khám phá và câu trả lời tương ứng chỉ ra rằng việc can thiệp vào cấu hình firmware là cần thiết).</p>
}

// question: 101.1.6  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Các đường dẫn nào được sử dụng để xác định phân vùng thứ nhất và thứ hai của thẻ nhớ SD (SD cards) được nhận dạng đầu tiên?</p>{
	~[moodle]A. /dev/sdc1, /dev/sdc2.#<p>Đây là quy ước đặt tên cho ổ đĩa SATA/SCSI/IDE thứ ba (hoặc thứ hai trong một số trường hợp).</p>
	~[moodle]B. /dev/nvme0n1p1, /dev/nvme0n1p2.#<p>Đây là quy ước đặt tên cho thiết bị NVMe.</p>
	=[moodle]C. /dev/mmcblk0p1, /dev/mmcblk0p2.
	~[moodle]D. /dev/mmcblk1p1, /dev/mmcblk1p2.#<p>Đây là thẻ SD thứ hai được nhận dạng.</p>
	####<p><strong>Giải thích</strong>: Đối với thẻ SD, các đường dẫn /dev/mmcblk0p1 và /dev/mmcblk0p2 được sử dụng cho phân vùng thứ nhất và thứ hai của thiết bị được nhận dạng đầu tiên.</p>
}

// question: 101.1.7  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Theo nguyên tắc chung về đặt tên thiết bị khối, sự khác biệt trong việc đặt tên xảy ra với loại thiết bị nào?</p>{
	~[moodle]A. Thiết bị SATA truyền thống (HDD/SSD).#<p>Các thiết bị này thường tuân theo quy tắc đặt tên truyền thống (/dev/sda, /dev/sdb, v.v.) (ngụ ý từ bối cảnh miêu tả các ngoại lệ).</p>
	~[moodle]B. Thiết bị PATA.#<p>Các thiết bị này thường tuân theo quy tắc đặt tên truyền thống (/dev/sda, /dev/sdb, v.v.) (ngụ ý từ bối cảnh miêu tả các ngoại lệ).</p>
	=[moodle]C. Thẻ nhớ SD và thiết bị NVMe.
	~[moodle]D. Thiết bị USB bên ngoài.#<p>Các thiết bị này thường tuân theo quy tắc đặt tên truyền thống (/dev/sda, /dev/sdb, v.v.) (ngụ ý từ bối cảnh miêu tả các ngoại lệ).</p>
	####<p><strong>Giải thích</strong>: Ngoại lệ đối với quy tắc đặt tên truyền thống xảy ra với thẻ nhớ SD (SD cards) và thiết bị NVMe (SSD kết nối với bus PCI Express).</p>
}

// question: 101.1.8  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong một máy tính, sau khi bật nguồn, phần mềm đầu tiên được thực thi là gì?</p>{
	~[moodle]A. Linux Kernel.#<p>Kernel được tải bởi Bootloader.</p>
	~[moodle]B. Bootloader.#<p>Bootloader được thực thi bởi firmware.</p>
	=[moodle]C. Firmware (BIOS/UEFI).
	~[moodle]D. Service Manager (Init System).#<p>Service Manager là chương trình đầu tiên được kernel khởi chạy.</p>
	####<p><strong>Giải thích</strong>: Firmware (BIOS hoặc UEFI) là chương trình đầu tiên chạy khi máy tính được bật nguồn, kích hoạt các thành phần cơ bản của hệ thống.</p>
}

// question: 101.1.9  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Các tiêu chuẩn công nghiệp về tập lệnh và giao tiếp thiết bị được thiết lập nhằm mục đích gì?</p>{
	~[moodle]A. Giúp các ứng dụng truy cập trực tiếp vào phần cứng.#<p>Hệ điều hành cung cấp một lớp trừu tượng cho ứng dụng.</p>
	~[moodle]B. Đảm bảo rằng chỉ một nhà sản xuất có thể tạo ra phần cứng tương thích.#<p>Đây không phải là mục đích chính được đề cập.</p>
	=[moodle]C. Giúp việc viết và bảo trì hệ điều hành không bị ràng buộc với một mô hình phần cứng cụ thể dễ dàng hơn.
	~[moodle]D. Tăng cường tốc độ truy cập bộ nhớ.#<p>Đây không phải là mục đích chính được đề cập.</p>
	####<p><strong>Giải thích</strong>: Các tiêu chuẩn giúp việc viết và bảo trì hệ điều hành dễ dàng hơn vì hệ điều hành không bị ràng buộc với một mô hình phần cứng cụ thể.</p>
}

// question: 101.1.10  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Khi đề cập đến các tiêu chuẩn trừu tượng, hệ điều hành cung cấp lớp trừu tượng tiêu chuẩn hóa (standardized abstraction layer) cho đối tượng nào?</p>{
	~[moodle]A. Kernel.#<p>Lớp trừu tượng này là giữa hệ điều hành và ứng dụng.</p>
	~[moodle]B. Firmware.#<p>Lớp trừu tượng này là giữa hệ điều hành và ứng dụng.</p>
	=[moodle]C. Ứng dụng (Application).
	~[moodle]D. Thiết bị I/O.#<p>Lớp trừu tượng này là giữa hệ điều hành và ứng dụng.</p>
	####<p><strong>Giải thích</strong>: Tương tự như các tiêu chuẩn phần cứng, hệ điều hành cung cấp lớp trừu tượng tiêu chuẩn hóa cho một ứng dụng.</p>
}

// question: 101.1.11  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong các hệ thống cũ sử dụng BIOS, nơi nào là nơi duy nhất để kiểm soát việc điều chỉnh tài nguyên phần cứng để đảm bảo hệ điều hành cài đặt và hoạt động chính xác?</p>{
	~[moodle]A. Trong các tệp cấu hình kernel.#<p>Mặc dù các thành phần này quan trọng, việc điều chỉnh tài nguyên cấp thấp nhất thường xảy ra trong firmware.</p>
	=[moodle]B. Trong tiện ích cấu hình BIOS.
	~[moodle]C. Trong tệp /proc/devices.#<p>Mặc dù các thành phần này quan trọng, việc điều chỉnh tài nguyên cấp thấp nhất thường xảy ra trong firmware.</p>
	~[moodle]D. Trong MBR.#<p>Mặc dù các thành phần này quan trọng, việc điều chỉnh tài nguyên cấp thấp nhất thường xảy ra trong firmware.</p>
	####<p><strong>Giải thích</strong>: Sự phức tạp của phần cứng tích hợp đôi khi đòi hỏi phải điều chỉnh cách tài nguyên được hiển thị cho hệ điều hành, điều này được thực hiện thông qua tiện ích cấu hình BIOS (hoặc UEFI).</p>
}

// question: 101.1.12  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong bối cảnh phân vùng, nếu ổ đĩa thứ hai được xác định là một thiết bị khối thông thường, các phân vùng thứ nhất và thứ hai của nó sẽ được xác định bằng đường dẫn nào?</p>{
	=[moodle]A. /dev/sdb1, /dev/sdb2.
	~[moodle]B. /dev/sda1, /dev/sda2.#<p>Đây là ổ đĩa đầu tiên.</p>
	~[moodle]C. /dev/mmcblk1p1, /dev/mmcblk1p2.#<p>Đây là quy ước đặt tên cho thẻ nhớ SD và thiết bị NVMe, không phải thiết bị khối thông thường.</p>
	~[moodle]D. /dev/nvme1n1p1, /dev/nvme1n1p2.#<p>Đây là quy ước đặt tên cho thẻ nhớ SD và thiết bị NVMe, không phải thiết bị khối thông thường.</p>
	####<p><strong>Giải thích</strong>: Nếu ổ đĩa được xác định là thứ hai (b), các phân vùng của nó sẽ là /dev/sdb1, /dev/sdb2, v.v..</p>
}

// question: 101.1.13  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Tiện ích cấu hình nào thường được gọi là BIOS, mặc dù đã được thay thế bằng một triển khai hiện đại hơn?</p>{
	~[moodle]A. NVRAM.#<p>Đây là các thành phần của hệ thống hoặc kiểu bảng phân vùng, không phải là tên gọi chung cho tiện ích cấu hình.</p>
	~[moodle]B. EFI.#<p>Đây là các thành phần của hệ thống hoặc kiểu bảng phân vùng, không phải là tên gọi chung cho tiện ích cấu hình.</p>
	=[moodle]C. UEFI.
	~[moodle]D. MBR.#<p>Đây là các thành phần của hệ thống hoặc kiểu bảng phân vùng, không phải là tên gọi chung cho tiện ích cấu hình.</p>
	####<p><strong>Giải thích</strong>: Dù đã thay đổi sang UEFI, không có gì lạ khi tiện ích cấu hình vẫn được gọi là BIOS, vì cả hai đều thực hiện cùng một mục đích cơ bản.</p>
}

// question: 101.1.14  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Khi một mô-đun hạt nhân (kernel module) đang được sử dụng bởi một quy trình đang chạy, điều gì ngăn cản việc gỡ bỏ mô-đun đó?</p>{
	~[moodle]A. Lỗi phần cứng.#<p>Các lựa chọn này không phản ánh lý do kỹ thuật được ngụ ý trong tài liệu về việc mô-đun không thể bị gỡ bỏ.</p>
	~[moodle]B. Thiếu quyền root.#<p>Các lựa chọn này không phản ánh lý do kỹ thuật được ngụ ý trong tài liệu về việc mô-đun không thể bị gỡ bỏ.</p>
	~[moodle]C. Mô-đun không tồn tại.#<p>Các lựa chọn này không phản ánh lý do kỹ thuật được ngụ ý trong tài liệu về việc mô-đun không thể bị gỡ bỏ.</p>
	=[moodle]D. Mô-đun đang được sử dụng bởi một quy trình đang chạy (running process).
	####<p><strong>Giải thích</strong>: Theo một câu trả lời ví dụ trong tài liệu, việc gỡ bỏ mô-đun sẽ bị lỗi nếu mô-đun đang được sử dụng bởi một quy trình đang chạy.</p>
}

// question: 101.1.15  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Điều gì không phổ biến khi các nhà sản xuất máy tính tích hợp nhiều bộ phận phần cứng khác nhau trong máy của họ?</p>{
	~[moodle]A. Không phổ biến kể từ những năm đầu của máy tính điện tử.#<p>Điều ngược lại là đúng.</p>
	=[moodle]B. Phổ biến ngay cả từ những năm đầu của máy tính điện tử.
	~[moodle]C. Chỉ phổ biến trong các máy chủ x86.#<p>Điều ngược lại là đúng.</p>
	~[moodle]D. Chỉ phổ biến trong các thiết bị di động.#<p>Điều ngược lại là đúng.</p>
	####<p><strong>Giải thích</strong>: Các nhà sản xuất máy tính đã tích hợp nhiều bộ phận phần cứng khác nhau kể từ những năm đầu của điện toán điện tử.</p>
}

// question: 101.1.16  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Nếu bạn muốn xác nhận xem card video bên ngoài được kết nối với bus PCI của máy tính để bàn có đúng như quảng cáo của nhà sản xuất hay không mà không mở vỏ máy (để tránh làm mất bảo hành), bạn có thể sử dụng lệnh nào350 để liệt kê chi tiết card video được hệ điều hành phát hiện?</p>{
	~[moodle]A. lsusb.#<p>lsusb chỉ hiển thị các thiết bị USB.</p>
	~[moodle]B. lscpu.#<p>lscpu hiển thị thông tin CPU.</p>
	=[moodle]C. Một lệnh liệt kê thiết bị PCI (ví dụ: lspci).
	~[moodle]D. dmidecode.#<p>dmidecode hiển thị thông tin DMI/BIOS.</p>
	####<p><strong>Giải thích</strong>: Câu hỏi 2 trong bài tập Hướng dẫn ngụ ý cần một lệnh để liệt kê chi tiết của card video (kết nối PCI) được hệ điều hành phát hiện. Các lệnh được thiết kế cho mục đích này là thích hợp (ví dụ: lspci).</p>
}

// question: 101.2.1  name: 101.2 Boot the system
$CATEGORY: $module$/top/TOPIC 101: SYSTEM ARCHITECTURE/101.2 Boot the system

::101.2 Boot the system::[html]<p>Trên một máy được trang bị firmware BIOS, binary bootstrap (bộ tải khởi động giai đoạn đầu) được đặt ở đâu?</p>{
	~[moodle]A. Trong phân vùng EFI System Partition (ESP).#<p>ESP là nơi chứa ứng dụng EFI cho hệ thống UEFI.</p>
	=[moodle]B. Trong MBR (Master Boot Record) của thiết bị lưu trữ đầu tiên.
	~[moodle]C. Trong /boot/grub/grub.cfg.#<p>Đây là tệp cấu hình của bootloader GRUB 2.</p>
	~[moodle]D. Trong NVRAM của firmware.#<p>NVRAM được sử dụng bởi UEFI.</p>
	####<p><strong>Giải thích</strong>: Trên máy được trang bị BIOS, binary bootstrap nằm trong MBR của thiết bị lưu trữ đầu tiên, như đã xác định trong tiện ích cấu hình BIOS.</p>
}

// question: 101.2.2  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong chuỗi khởi động UEFI, điều gì là cần thiết để thực thi ứng dụng EFI đã được định nghĩa trước (thường là bootloader)?</p>{
	~[moodle]A. Lệnh initramfs phải được thực thi.#<p>initramfs được kernel sử dụng.</p>
	=[moodle]B. Firmware phải đọc các định nghĩa được lưu trữ trong NVRAM.
	~[moodle]C. Kernel phải được giải nén trước.#<p>Việc giải nén kernel xảy ra sau đó.</p>
	~[moodle]D. BIOS phải kích hoạt các thành phần cơ bản.#<p>BIOS là cơ chế khởi động cũ, khác với UEFI.</p>
	####<p><strong>Giải thích</strong>: UEFI đọc các định nghĩa được lưu trữ trong NVRAM để thực thi ứng dụng EFI đã được định nghĩa trước.</p>
}

// question: 101.2.3  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Lệnh nào sau đây được sử dụng để đọc tất cả các thông báo khởi động của kernel (kernel ring buffer), thường là để kiểm tra sự kiện phần cứng và driver?</p>{
	~[moodle]A. journalctl.#<p>journalctl được sử dụng để truy vấn systemd journal.</p>
	=[moodle]B. dmesg.
	~[moodle]C. systemctl status.#<p>Đây là các lệnh quản lý dịch vụ hoặc mô-đun, không phải để đọc trực tiếp bộ đệm thông báo kernel.</p>
	~[moodle]D. lsmod.#<p>Đây là các lệnh quản lý dịch vụ hoặc mô-đun, không phải để đọc trực tiếp bộ đệm thông báo kernel.</p>
	####<p><strong>Giải thích</strong>: dmesg là một trong những lệnh được sử dụng để đọc các thông báo khởi động (boot messages).</p>
}

// question: 101.2.4  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Điều gì xảy ra khi hệ thống Linux hiển thị thông báo: ALERT! /dev/sda3 does not exist. Dropping to a shell!?</p>{
	~[moodle]A. Kernel đã tìm thấy hệ thống tập tin gốc nhưng bị lỗi đọc.#<p>Các lựa chọn này mô tả không chính xác nguyên nhân của thông báo lỗi cụ thể này.</p>
	=[moodle]B. Kernel không thể tìm thấy thiết bị /dev/sda3 đã được thông báo là hệ thống tập tin gốc.
	~[moodle]C. Thiết bị /dev/sda3 đã được gắn (mounted) thành công nhưng không có kernel.#<p>Các lựa chọn này mô tả không chính xác nguyên nhân của thông báo lỗi cụ thể này.</p>
	~[moodle]D. Bootloader không thể tải kernel.#<p>Các lựa chọn này mô tả không chính xác nguyên nhân của thông báo lỗi cụ thể này.</p>
	####<p><strong>Giải thích</strong>: Vấn đề là kernel không thể tìm thấy thiết bị /dev/sda3, thiết bị đã được thông báo là hệ thống tập tin gốc.</p>
}

// question: 101.2.5  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Để thông báo cho kernel biết hệ thống tập tin gốc (root filesystem) nằm tại /dev/sda3 thông qua tham số khởi động (kernel parameter), cú pháp chính xác là gì?</p>{
	~[moodle]A. kernel /dev/sda3.#<p>Các lựa chọn này không phải là cú pháp chuẩn để chỉ định root filesystem cho kernel.</p>
	=[moodle]B. root=/dev/sda3.
	~[moodle]C. init=/dev/sda3.#<p>Các lựa chọn này không phải là cú pháp chuẩn để chỉ định root filesystem cho kernel.</p>
	~[moodle]D. systemd.unit=multi-user.target /dev/sda3.#<p>Các lựa chọn này không phải là cú pháp chuẩn để chỉ định root filesystem cho kernel.</p>
	####<p><strong>Giải thích</strong>: Tham số kernel được sử dụng để chỉ định vị trí hệ thống tập tin gốc là root= theo sau là đường dẫn thiết bị, ví dụ: root=/dev/sda3.</p>
}

// question: 101.2.6  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Tại sao việc cài đặt hệ điều hành mới trên máy tính UEFI không có khả năng ghi đè lên MBR của đĩa cứng, làm cho hệ điều hành khác không thể truy cập được?</p>{
	=[moodle]A. UEFI không sử dụng MBR mà dựa trên ESP.
	~[moodle]B. UEFI chỉ cho phép một hệ điều hành được cài đặt.#<p>Các tuyên bố này là không chính xác về UEFI.</p>
	~[moodle]C. UEFI tự động sử dụng SysVinit.#<p>Các tuyên bố này là không chính xác về UEFI.</p>
	~[moodle]D. UEFI không yêu cầu bootloader.#<p>Các tuyên bố này là không chính xác về UEFI.</p>
	####<p><strong>Giải thích</strong>: Điều này sẽ không xảy ra trên máy được trang bị firmware UEFI vì UEFI không sử dụng MBR để lưu trữ bootloader mà thay vào đó sử dụng các ứng dụng EFI được lưu trữ trên ESP (EFI System Partition).</p>
}

// question: 101.2.7  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong chuỗi khởi động UEFI, ứng dụng EFI được xác định trước (pre-defined EFI application) được thực thi từ phân vùng nào?</p>{
	~[moodle]A. MBR.#<p>MBR được sử dụng trong hệ thống BIOS.</p>
	~[moodle]B. /boot.#<p>/boot không phải là phân vùng EFI.</p>
	=[moodle]C. ESP (EFI System Partition).
	~[moodle]D. NVRAM.#<p>NVRAM lưu trữ định nghĩa, không phải bản thân ứng dụng.</p>
	####<p><strong>Giải thích</strong>: Firmware UEFI đọc các định nghĩa trong NVRAM để thực thi ứng dụng EFI được lưu trữ trong hệ thống tập tin của phân vùng ESP (EFI System Partition).</p>
}

// question: 101.2.8  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Quá trình khởi động của máy Linux bắt đầu với việc kernel khởi chạy chương trình đầu tiên. Chương trình này là gì và nó luôn có PID bao nhiêu?</p>{
	~[moodle]A. Kernel, PID 0.#<p>Kernel có PID 0. Bootloader chạy trước kernel. Ứng dụng EFI chạy trước kernel.</p>
	~[moodle]B. Bootloader, PID 0.#<p>Kernel có PID 0. Bootloader chạy trước kernel. Ứng dụng EFI chạy trước kernel.</p>
	=[moodle]C. Service Manager (Trình quản lý dịch vụ), PID 1.
	~[moodle]D. Ứng dụng EFI, PID 1.#<p>Kernel có PID 0. Bootloader chạy trước kernel. Ứng dụng EFI chạy trước kernel.</p>
	####<p><strong>Giải thích</strong>: Trình quản lý dịch vụ (Service Manager) là chương trình đầu tiên được kernel khởi chạy trong quá trình khởi động, vì vậy PID (process identification number) của nó luôn là 1.</p>
}

// question: 101.2.9  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Giả sử một ổ đĩa cứng chứa toàn bộ hệ thống tập tin của một máy offline được gắn vào một máy đang hoạt động tại /mnt/hd. Lệnh journalctl nào được sử dụng để kiểm tra nội dung của các tệp journal nằm tại /mnt/hd/var/log/journal/?</p>{
	~[moodle]A. journalctl -F /mnt/hd/var/log/journal.#<p>Các tùy chọn -F, -B, -u không được sử dụng để chỉ định thư mục journal bên ngoài.</p>
	~[moodle]B. journalctl -B /mnt/hd/var/log/journal.#<p>Các tùy chọn -F, -B, -u không được sử dụng để chỉ định thư mục journal bên ngoài.</p>
	=[moodle]C. journalctl -D /mnt/hd/var/log/journal.
	~[moodle]D. journalctl -u /mnt/hd/var/log/journal.#<p>Các tùy chọn -F, -B, -u không được sử dụng để chỉ định thư mục journal bên ngoài.</p>
	####<p><strong>Giải thích</strong>: Lệnh chính xác là journalctl -D /mnt/hd/var/log/journal hoặc journalctl --directory=/mnt/hd/var/log/journal.</p>
}

// question: 101.2.10  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong hệ thống dựa trên SysVinit, các trạng thái hệ thống được xác định trước, có số từ 0 đến 6 và các tệp script dịch vụ tương ứng được thực thi, được gọi là gì?</p>{
	~[moodle]A. Boot Targets.#<p>Đây là các thuật ngữ được sử dụng bởi systemd.</p>
	=[moodle]B. Runlevels.
	~[moodle]C. Service Units.#<p>Đây là các thuật ngữ được sử dụng bởi systemd.</p>
	~[moodle]D. Initramfs.#<p>Initramfs là một hệ thống tập tin tạm thời được kernel sử dụng.</p>
	####<p><strong>Giải thích</strong>: Trình quản lý dịch vụ dựa trên tiêu chuẩn SysVinit cung cấp các bộ trạng thái hệ thống được xác định trước, được gọi là runlevels.</p>
}

// question: 101.2.11  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Để xem thông báo khởi động của kernel bằng lệnh dmesg với pager được bật theo mặc định, ta sử dụng tùy chọn nào?</p>{
	~[moodle]A. dmesg -F.#<p>Các tùy chọn này không được đề cập với mục đích bật pager.</p>
	~[moodle]B. dmesg -D.#<p>Các tùy chọn này không được đề cập với mục đích bật pager.</p>
	=[moodle]C. dmesg -H.
	~[moodle]D. dmesg -R.#<p>Các tùy chọn này không được đề cập với mục đích bật pager.</p>
	####<p><strong>Giải thích</strong>: Các lệnh dmesg -H hoặc dmesg --human sẽ bật pager theo mặc định.</p>
}

// question: 101.2.12  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong quá trình khởi động, bootloader đóng vai trò gì?</p>{
	~[moodle]A. Khởi tạo tất cả phần cứng.#<p>Các nhiệm vụ này được thực hiện bởi firmware, kernel và service manager.</p>
	=[moodle]B. Tải kernel của hệ điều hành và chuyển quyền kiểm soát cho nó.
	~[moodle]C. Cấu hình các dịch vụ mạng.#<p>Các nhiệm vụ này được thực hiện bởi firmware, kernel và service manager.</p>
	~[moodle]D. Quản lý các tiến trình đang chạy.#<p>Các nhiệm vụ này được thực hiện bởi firmware, kernel và service manager.</p>
	####<p><strong>Giải thích</strong>: Mục đích duy nhất của bootloader là tải kernel của hệ điều hành và chuyển quyền kiểm soát cho nó.</p>
}

// question: 101.2.13  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Tiện ích nào là trình quản lý dịch vụ hiện đại và phổ biến nhất được sử dụng trong hầu hết các bản phân phối Linux hiện nay?</p>{
	~[moodle]A. SysVinit.#<p>SysVinit là tiêu chuẩn cũ hơn.</p>
	~[moodle]B. Upstart.#<p>Upstart là một giải pháp quản lý dịch vụ khác nhưng thường được đề cập là nhận biết (awareness).</p>
	~[moodle]C. initramfs.#<p>Initramfs là một tệp lưu trữ.</p>
	=[moodle]D. systemd.
	####<p><strong>Giải thích</strong>: systemd là trình quản lý dịch vụ được sử dụng phổ biến nhất.</p>
}

// question: 101.2.14  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong bối cảnh UEFI, NVRAM được sử dụng để lưu trữ những thông tin nào?</p>{
	~[moodle]A. Kernel Linux.#<p>Các mục này không được lưu trữ trong NVRAM để khởi động UEFI.</p>
	~[moodle]B. Dữ liệu thời gian chạy của hệ điều hành.#<p>Các mục này không được lưu trữ trong NVRAM để khởi động UEFI.</p>
	=[moodle]C. Định nghĩa để thực thi ứng dụng EFI đã được định nghĩa trước.
	~[moodle]D. MBR của ổ đĩa.#<p>Các mục này không được lưu trữ trong NVRAM để khởi động UEFI.</p>
	####<p><strong>Giải thích</strong>: Firmware UEFI đọc các định nghĩa được lưu trữ trong NVRAM để thực thi ứng dụng EFI đã được định nghĩa trước.</p>
}

// question: 101.2.15  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong hệ thống SysVinit, những tiện ích nào là một phần của danh sách các tệp, thuật ngữ và tiện ích được sử dụng để quản lý runlevels/boot targets?</p>{
	~[moodle]A. systemctl, /etc/systemd/.#<p>Đây là các thành phần của systemd.</p>
	~[moodle]B. dmesg, journalctl.#<p>Đây là các lệnh để đọc thông báo khởi động.</p>
	=[moodle]C. init, telinit, /etc/inittab.
	~[moodle]D. grub-install, grub.cfg.#<p>Đây là các lệnh và tệp cấu hình bootloader.</p>
	####<p><strong>Giải thích</strong>: init, telinit, và /etc/inittab là các thành phần được liệt kê cho việc thay đổi runlevels trong các hệ thống dựa trên SysVinit.</p>
}

// question: 101.2.16  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Sự khác biệt chính giữa BIOS và UEFI, mà người dùng cần biết, là gì?</p>{
	~[moodle]A. Sự khác biệt trong việc quản lý bộ nhớ.#<p>Các lựa chọn này là các chủ đề liên quan nhưng không phải là trọng tâm chính của sự khác biệt giữa BIOS/UEFI trong bối cảnh khởi động.</p>
	~[moodle]B. Các giai đoạn khởi tạo hệ thống điển hình.#<p>Các lựa chọn này là các chủ đề liên quan nhưng không phải là trọng tâm chính của sự khác biệt giữa BIOS/UEFI trong bối cảnh khởi động.</p>
	=[moodle]C. Cách BIOS và UEFI khởi động khác nhau.
	~[moodle]D. Cách phục hồi thông báo khởi động.#<p>Các lựa chọn này là các chủ đề liên quan nhưng không phải là trọng tâm chính của sự khác biệt giữa BIOS/UEFI trong bối cảnh khởi động.</p>
	####<p><strong>Giải thích</strong>: Bài học 101.2 bao gồm cách BIOS và UEFI khởi động khác nhau.</p>
}

// question: 101.3.1  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
$CATEGORY: $module$/top/TOPIC 101: SYSTEM ARCHITECTURE/101.3 Change runlevels / boot targets and shutdown or reboot system

::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên SysVinit, runlevel nào được sử dụng để khởi động lại hệ thống (reboot)?</p>{
	~[moodle]A. Runlevel 0.#<p>Runlevel 0 thường là tắt nguồn (Halt/Power off) (Dựa trên kiến thức chung về runlevel 0-6).</p>
	~[moodle]B. Runlevel 1 (Single-user mode).#<p>Runlevel 1 là chế độ người dùng đơn (single user mode).</p>
	~[moodle]C. Runlevel 3 (Multi-user, non-graphical).#<p>Runlevel 3 là chế độ đa người dùng với mạng, không có GUI (ngụ ý).</p>
	=[moodle]D. Runlevel 6.
	####<p><strong>Giải thích</strong>: Lệnh telinit 6 sẽ chuyển sang runlevel 6, tức là khởi động lại hệ thống (reboot).</p>
}

// question: 101.3.2  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên SysVinit, điều gì xảy ra với các dịch vụ liên quan đến tệp /etc/rc1.d/K90network khi hệ thống chuyển sang runlevel 1?</p>{
	~[moodle]A. Các dịch vụ liên quan sẽ được khởi động (Start).#<p>Chữ cái S (Start) mới là để khởi động các dịch vụ.</p>
	=[moodle]B. Các dịch vụ liên quan sẽ bị dừng (Stop).
	~[moodle]C. Các dịch vụ sẽ được bỏ qua (Ignore).#<p>Sai chức năng của script SysVinit.</p>
	~[moodle]D. Hệ thống sẽ tự động khởi động lại.#<p>Sai chức năng của script SysVinit.</p>
	####<p><strong>Giải thích</strong>: Do chữ cái K (Kill) ở đầu tên tệp, các dịch vụ liên quan sẽ bị dừng khi hệ thống vào runlevel 1.</p>
}

// question: 101.3.3  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Lệnh nào được sử dụng trong hệ thống dựa trên systemd để kiểm tra xem đơn vị (unit) sshd.service có đang chạy hay không?</p>{
	~[moodle]A. systemctl restart sshd.service.#<p>Khởi động lại dịch vụ.</p>
	=[moodle]B. systemctl status sshd.service.
	~[moodle]C. systemctl enable sshd.service.#<p>Bật dịch vụ khởi động cùng hệ thống.</p>
	~[moodle]D. systemctl is-enabled sshd.service.#<p>Kiểm tra xem dịch vụ có được bật để khởi động cùng hệ thống hay không.</p>
	####<p><strong>Giải thích</strong>: Lệnh systemctl status sshd.service được sử dụng để người dùng xác minh xem unit dịch vụ có đang chạy hay không.</p>
}

// question: 101.3.4  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên systemd, lệnh nào phải được thực thi để bật (enable) kích hoạt đơn vị sshd.service trong quá trình khởi tạo hệ thống (system initialization)?</p>{
	~[moodle]A. systemctl start sshd.service.#<p>Khởi động dịch vụ ngay lập tức.</p>
	~[moodle]B. systemctl status sshd.service.#<p>Kiểm tra trạng thái.</p>
	=[moodle]C. systemctl enable sshd.service.
	~[moodle]D. systemctl reload sshd.service.#<p>Tải lại cấu hình dịch vụ.</p>
	####<p><strong>Giải thích</strong>: Lệnh systemctl enable sshd.service phải được thực thi để bật (enable) kích hoạt unit sshd.service trong quá trình khởi tạo hệ thống.</p>
}

// question: 101.3.5  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên systemd, làm thế nào để xác minh target hệ thống mặc định hiện tại? (Chọn câu trả lời chính xác nhất dựa trên tiện ích được liệt kê)</p>{
	~[moodle]A. Kiểm tra PID 1.#<p>PID 1 luôn là service manager.</p>
	=[moodle]B. Sử dụng lệnh systemctl get-default.
	~[moodle]C. Đọc tệp /etc/inittab.#<p>Tệp này dành cho SysVinit.</p>
	~[moodle]D. Kiểm tra /etc/systemd/default.runlevel.#<p>Tệp này không tồn tại trong tài liệu này (thay vào đó là symbolic link /etc/systemd/system/default.target).</p>
	####<p><strong>Giải thích</strong>: Lệnh systemctl get-default có thể được sử dụng để xác minh target hệ thống mặc định.</p>
}

// question: 101.3.6  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Để giới hạn người dùng có thể khởi động lại máy bằng cách nhấn tổ hợp phím Ctrl + Alt + Del trong triển khai SysVinit, người dùng đó phải có tên trong tệp nào?</p>{
	~[moodle]A. /etc/inittab.#<p>/etc/inittab là tệp cấu hình cho hành động Ctrl + Alt + Del, nhưng danh sách người dùng nằm trong tệp khác.</p>
	=[moodle]B. /etc/shutdown.allow.
	~[moodle]C. /etc/rc.d/boot.conf.#<p>Tệp này không liên quan đến giới hạn Ctrl + Alt + Del.</p>
	~[moodle]D. /etc/sysconfig/init.#<p>Tệp này không liên quan đến giới hạn Ctrl + Alt + Del.</p>
	####<p><strong>Giải thích</strong>: Bằng cách đặt tùy chọn -a cho lệnh shutdown trong tệp /etc/inittab, chỉ những người dùng có tên người dùng trong tệp /etc/shutdown.allow mới có thể khởi động lại hệ thống bằng tổ hợp phím Ctrl + Alt + Del.</p>
}

// question: 101.3.7  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Lệnh nào được sử dụng để hủy bỏ quá trình khởi động lại hệ thống đã được lên lịch bằng lệnh shutdown?</p>{
	~[moodle]A. shutdown -H now.#<p>Đây là các lệnh để tắt hoặc khởi động lại hệ thống ngay lập tức.</p>
	~[moodle]B. shutdown -r now.#<p>Đây là các lệnh để tắt hoặc khởi động lại hệ thống ngay lập tức.</p>
	=[moodle]C. shutdown -c.
	~[moodle]D. telinit Q.#<p>telinit Q không phải lệnh hủy shutdown.</p>
	####<p><strong>Giải thích</strong>: Lệnh shutdown -c nên được sử dụng để hủy bỏ quá trình khởi động lại đã được lên lịch.</p>
}

// question: 101.3.8  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong Upstart, lệnh nào được sử dụng để bắt đầu một terminal ảo thứ sáu (tty6)?</p>{
	~[moodle]A. init 6.#<p>init và telinit thường được sử dụng trong SysVinit.</p>
	~[moodle]B. systemctl start tty6.#<p>systemctl được sử dụng trong systemd.</p>
	=[moodle]C. start tty6.
	~[moodle]D. telinit 6.#<p>init và telinit thường được sử dụng trong SysVinit.</p>
	####<p><strong>Giải thích</strong>: Đối với Upstart, lệnh start có thể được sử dụng để khởi tạo một terminal ảo, ví dụ: start tty6.</p>
}

// question: 101.3.9  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Các quy trình (processes) trong các hệ thống dựa trên nguyên tắc thiết kế Unix để kiểm soát các chức năng riêng biệt của hệ thống (ví dụ: máy chủ HTTP, chia sẻ tệp) được gọi là gì?</p>{
	~[moodle]A. Service Managers.#<p>Service Manager là chương trình quản lý các daemons.</p>
	~[moodle]B. Libraries.#<p>Libraries không phải là quy trình chạy.</p>
	=[moodle]C. Daemons (hoặc services).
	~[moodle]D. Shell Scripts.#<p>Shell Scripts không phải là daemons.</p>
	####<p><strong>Giải thích</strong>: Các quy trình này, chịu trách nhiệm cho các chức năng và tính năng mở rộng của hệ điều hành, được gọi là daemons (hoặc, nói chung hơn, services).</p>
}

// question: 101.3.10  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên systemd, tệp liên kết tượng trưng nào sẽ trỏ đến tệp unit được xác định là target mặc định?</p>{
	~[moodle]A. /etc/inittab.#<p>Thuộc về SysVinit.</p>
	=[moodle]B. /etc/systemd/system/default.target.
	~[moodle]C. /usr/lib/systemd/default.target.#<p>Tệp không nằm ở vị trí chính xác để là symbolic link cho target mặc định.</p>
	~[moodle]D. /etc/systemd/default.target.#<p>Tệp không nằm ở vị trí chính xác để là symbolic link cho target mặc định.</p>
	####<p><strong>Giải thích</strong>: Liên kết tượng trưng /etc/systemd/system/default.target sẽ trỏ đến tệp unit được xác định là target mặc định.</p>
}

// question: 101.3.11  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Lệnh nào được sử dụng để gửi thông báo cảnh báo (warning text) đến tất cả các phiên terminal của người dùng đang đăng nhập?</p>{
	~[moodle]A. echo.#<p>echo chỉ in ra màn hình của phiên hiện tại.</p>
	~[moodle]B. mail.#<p>mail gửi email.</p>
	=[moodle]C. wall.
	~[moodle]D. logger.#<p>logger gửi thông báo đến hệ thống log.</p>
	####<p><strong>Giải thích</strong>: Tham số message của lệnh shutdown là văn bản cảnh báo được gửi đến tất cả các phiên terminal của người dùng đang đăng nhập thông qua tiện ích wall.</p>
}

// question: 101.3.12  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Lệnh nào trong Upstart được sử dụng để dừng (interruption) một dịch vụ?</p>{
	~[moodle]A. kill.#<p>kill gửi tín hiệu đến tiến trình, disable thường là cho systemd, halt là lệnh tắt máy.</p>
	=[moodle]B. stop.
	~[moodle]C. disable.#<p>kill gửi tín hiệu đến tiến trình, disable thường là cho systemd, halt là lệnh tắt máy.</p>
	~[moodle]D. halt.#<p>kill gửi tín hiệu đến tiến trình, disable thường là cho systemd, halt là lệnh tắt máy.</p>
	####<p><strong>Giải thích</strong>: Việc gián đoạn một dịch vụ trong Upstart được thực hiện bằng lệnh stop.</p>
}

// question: 101.3.13  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên systemd, tệp nào là một phần của "Partial list of the used files, terms and utilities" (Danh sách tệp, thuật ngữ và tiện ích được sử dụng một phần) cho Mục tiêu 101.3?</p>{
	~[moodle]A. /etc/init.d/.#<p>Tất cả đều là phần của danh sách.</p>
	~[moodle]B. /etc/inittab.#<p>Tất cả đều là phần của danh sách.</p>
	~[moodle]C. /usr/lib/systemd/.#<p>Tất cả đều là phần của danh sách.</p>
	=[moodle]D. Tất cả các mục trên.
	####<p><strong>Giải thích</strong>: Cả /etc/init.d/, /etc/inittab, và /usr/lib/systemd/ đều nằm trong danh sách các tệp và tiện ích liên quan đến Mục tiêu 101.3.</p>
}

// question: 101.3.14  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong một hệ thống dựa trên systemd, lệnh nào có thể được sử dụng để thay đổi giữa các target khởi động, bao gồm cả chế độ người dùng đơn (single user mode)?</p>{
	~[moodle]A. telinit.#<p>telinit và init thường liên quan đến SysVinit.</p>
	~[moodle]B. init.#<p>telinit và init thường liên quan đến SysVinit.</p>
	=[moodle]C. systemctl.
	~[moodle]D. reboot.#<p>reboot chỉ khởi động lại, không thay đổi target cụ thể.</p>
	####<p><strong>Giải thích</strong>: systemctl là tiện ích được sử dụng để quản lý các target khởi động trong hệ thống systemd.</p>
}

// question: 101.3.15  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trình quản lý dịch vụ nào không dựa trên SysVinit hoặc systemd, và thường sử dụng các lệnh độc lập như start, stop, và status?</p>{
	~[moodle]A. SysVinit.#<p>SysVinit là tiêu chuẩn cũ, ACPI là giao diện cấu hình nâng cao, và Kernel là lõi của hệ điều hành.</p>
	~[moodle]B. ACPI.#<p>SysVinit là tiêu chuẩn cũ, ACPI là giao diện cấu hình nâng cao, và Kernel là lõi của hệ điều hành.</p>
	=[moodle]C. Upstart.
	~[moodle]D. Kernel.#<p>SysVinit là tiêu chuẩn cũ, ACPI là giao diện cấu hình nâng cao, và Kernel là lõi của hệ điều hành.</p>
	####<p><strong>Giải thích</strong>: Upstart là một tiện ích quản lý dịch vụ khác, trong đó mỗi hành động Upstart có một lệnh độc lập riêng (ví dụ: start, stop, status).</p>
}

// question: 101.3.16  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Theo lệnh shutdown, định dạng thời gian +m có nghĩa là gì khi lên lịch một sự kiện?</p>{
	~[moodle]A. Ngày và giờ chính xác (giờ:phút).#<p>Định dạng hh:mm chỉ định giờ và phút.</p>
	~[moodle]B. Thực thi ngay lập tức.#<p>Định dạng now hoặc +0 chỉ định thực thi ngay lập tức.</p>
	=[moodle]C. Số phút chờ trước khi thực thi.
	~[moodle]D. Số giờ chờ trước khi thực thi.#<p>+m là phút, không phải giờ.</p>
	####<p><strong>Giải thích</strong>: Định dạng +m chỉ định số phút chờ trước khi thực thi lệnh.</p>
}