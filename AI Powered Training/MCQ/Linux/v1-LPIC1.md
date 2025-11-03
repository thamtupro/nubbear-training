// TOPIC 101: SYSTEM ARCHITECTURE
// 101.1 Determine and configure hardware settings
$CATEGORY: $module$/top/101.1 Determine and configure hardware settings

// question: 1  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong kiến trúc hệ thống x86, chức năng cơ bản của BIOS và UEFI là gì, mặc dù UEFI cung cấp các tính năng phức tạp hơn?</p>{
	~[moodle]Cung cấp một hệ điều hành đầy đủ cho các thiết bị cũ.#<p>BIOS/UEFI chỉ là firmware khởi động, không phải là hệ điều hành đầy đủ.</p>
	~[moodle]Cung cấp các lệnh tải trình điều khiển mạng.#<p>Tải trình điều khiển mạng là nhiệm vụ của nhân hệ điều hành (kernel) sau khi hệ thống đã khởi động.</p>
	=[moodle]Đóng vai trò là tiện ích cấu hình cơ bản cho việc nhận dạng, kiểm tra, cấu hình phần cứng và nâng cấp firmware.
	~[moodle]Thiết lập các tham số hạt nhân (kernel parameters) ban đầu.#<p>Thiết lập tham số hạt nhân là chức năng của bootloader (ví dụ: GRUB).</p>
	####<p><strong>Explanation</strong>: Cả BIOS và UEFI đều đóng vai trò là tiện ích cấu hình cơ bản cho việc nhận dạng, kiểm tra, cấu hình phần cứng và nâng cấp firmware.</p>
}

// question: 2  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Sau khi thêm một ổ cứng SATA thứ hai vào hệ thống và hệ điều hành không thể khởi động, nguyên nhân có thể xảy ra là gì, biết rằng tất cả các bộ phận không bị lỗi?</p>{
	~[moodle]Không tìm thấy tập tin /etc/fstab cho ổ đĩa mới.#<p>/etc/fstab chỉ liên quan đến việc gắn kết các hệ thống tệp sau khi hệ thống đã khởi động kernel.</p>
	=[moodle]Thứ tự thiết bị khởi động (boot device order) chưa được cấu hình lại trong tiện ích cài đặt BIOS/UEFI.
	~[moodle]Nhân Linux (kernel) không hỗ trợ ổ cứng SATA thứ hai.#<p>Nhân Linux hiện đại hỗ trợ SATA rất tốt.</p>
	~[moodle]Xung đột giữa các mô-đun hạt nhân (kernel modules) của ổ đĩa cũ và mới.#<p>Xung đột mô-đun ít xảy ra và không phải là nguyên nhân trực tiếp phổ biến khiến hệ thống không khởi động được.</p>
	####<p><strong>Explanation</strong>: Thứ tự thiết bị khởi động phải được cấu hình trong tiện ích cài đặt BIOS, nếu không BIOS có thể không chạy được bootloader từ ổ đĩa chính.</p>
}

// question: 3  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong Linux, đường dẫn thiết bị khối (block device) tiêu chuẩn cho phân vùng thứ hai của ổ đĩa SATA thứ nhất là gì?</p>{
	~[moodle]/dev/sda.#<p>/dev/sda là tên của thiết bị khối (toàn bộ ổ đĩa).</p>
	=[moodle]/dev/sda2.
	~[moodle]/dev/sdb1.#<p>/dev/sdb1 là phân vùng thứ nhất của ổ đĩa SATA thứ hai.</p>
	~[moodle]/dev/mmcblk0p2.#<p>Đây là đường dẫn dành cho phân vùng SD card.</p>
	####<p><strong>Explanation</strong>: Theo mô hình đặt tên thiết bị khối truyền thống, /dev/sda là ổ đĩa SATA thứ nhất, và /dev/sda2 là phân vùng thứ hai của ổ đĩa đó.</p>
}

// question: 4  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Địa chỉ phân vùng của thiết bị lưu trữ NVMe (SSD kết nối qua PCI Express bus) sẽ bắt đầu bằng tiền tố nào?</p>{
	~[moodle]sd.#<p>sd dành cho các thiết bị SATA hoặc SCSI truyền thống.</p>
	~[moodle]mmcblk.#<p>mmcblk dành cho thẻ nhớ SD.</p>
	=[moodle]nvme.
	~[moodle]hd.#<p>hd là tiền tố legacy, thường không được sử dụng trong các hệ thống hiện đại.</p>
	####<p><strong>Explanation</strong>: Các thiết bị NVMe nhận tiền tố nvme, ví dụ: /dev/nvme0n1p1 và /dev/nvme0n1p2.</p>
}

// question: 5  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Lệnh nào có thể được sử dụng để liệt kê chi tiết các thành phần phần cứng được kết nối với bus PCI (ví dụ: card màn hình), như được hệ điều hành phát hiện?</p>{
	~[moodle]lsusb.#<p>lsusb liệt kê các thiết bị USB.</p>
	=[moodle]lspci.
	~[moodle]lsmod.#<p>lsmod liệt kê các mô-đun hạt nhân đang được tải.</p>
	~[moodle]dmesg.#<p>dmesg hiển thị thông báo bộ đệm vòng của hạt nhân (kernel ring buffer messages).</p>
	####<p><strong>Explanation</strong>: Lệnh lspci (List PCI devices) được sử dụng để liệt kê thông tin chi tiết về các thiết bị kết nối với bus PCI, bao gồm card màn hình.</p>
}

// question: 6  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Tập tin nào chứa thông tin về các lỗi đã biết (bugs) của CPU, chẳng hạn như cpu_meltdown?</p>{
	~[moodle]/var/log/dmesg.#<p>Chứa thông báo khởi động của kernel.</p>
	~[moodle]/proc/meminfo.#<p>Chứa thông tin về bộ nhớ hệ thống.</p>
	=[moodle]/proc/cpuinfo.
	~[moodle]/sys/class/cpu/.#<p>Là một thư mục ảo chứa thông tin về các thiết bị CPU.</p>
	####<p><strong>Explanation</strong>: Tập tin /proc/cpuinfo có một dòng hiển thị các lỗi đã biết (bugs:) cho CPU tương ứng.</p>
}

// question: 7  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Giả sử mô-đun bluetooth đang được sử dụng bởi một tiến trình đang chạy. Lệnh nào có khả năng thất bại nếu bạn cố gắng gỡ bỏ mô-đun này?</p>{
	~[moodle]lspci -k.#<p>Các lệnh này chỉ truy vấn thông tin, không thực hiện hành động gỡ bỏ.</p>
	~[moodle]modinfo bluetooth.#<p>Các lệnh này chỉ truy vấn thông tin, không thực hiện hành động gỡ bỏ.</p>
	~[moodle]lsmod | grep bluetooth.#<p>Các lệnh này chỉ truy vấn thông tin, không thực hiện hành động gỡ bỏ.</p>
	=[moodle]rmmod bluetooth.
	####<p><strong>Explanation</strong>: Lệnh rmmod dùng để gỡ bỏ một mô-đun hạt nhân. Nếu mô-đun đó đang được sử dụng bởi một tiến trình đang chạy, lệnh sẽ thất bại.</p>
}

// question: 8  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong các hệ thống cũ hơn sử dụng BIOS firmware, một vấn đề đặc biệt có thể ngăn hệ thống khởi động là gì nếu không có thiết bị này được phát hiện?</p>{
	~[moodle]Bộ xử lý mạng (Network processor).#<p>Các thiết bị này không phải là nguyên nhân phổ biến gây lỗi khởi động cho BIOS cũ.</p>
	~[moodle]Ổ đĩa quang (Optical drive).#<p>Các thiết bị này không phải là nguyên nhân phổ biến gây lỗi khởi động cho BIOS cũ.</p>
	=[moodle]Bàn phím (Keyboard).
	~[moodle]Chuột (Mouse).#<p>Các thiết bị này không phải là nguyên nhân phổ biến gây lỗi khởi động cho BIOS cũ.</p>
	####<p><strong>Explanation</strong>: Một số máy chủ x86 với firmware BIOS cũ hơn sẽ không khởi động nếu bàn phím không được phát hiện.</p>
}

// question: 9  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Lệnh nào được sử dụng để liệt kê các mô-đun hạt nhân (kernel modules) hiện đang được tải?</p>{
	~[moodle]lsusb.#<p>Liệt kê các thiết bị USB.</p>
	=[moodle]lsmod.
	~[moodle]lshw.#<p>Liệt kê thông tin tổng quát về phần cứng.</p>
	~[moodle]lspci.#<p>Liệt kê các thiết bị PCI.</p>
	####<p><strong>Explanation</strong>: Lệnh lsmod liệt kê trạng thái của các mô-đun hạt nhân trong Linux.</p>
}

// question: 10  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Theo mục tiêu 101.1, đâu là một trong những khu vực kiến thức chính mà một quản trị viên cần biết liên quan đến cấu hình phần cứng?</p>{
	~[moodle]Viết các driver cho phần cứng mới.#<p>Những điều này vượt quá phạm vi của mục tiêu quản trị hệ thống cơ bản 101.1.</p>
	=[moodle]Bật và tắt các thiết bị ngoại vi tích hợp.
	~[moodle]Thay đổi mã nguồn kernel.#<p>Những điều này vượt quá phạm vi của mục tiêu quản trị hệ thống cơ bản 101.1.</p>
	~[moodle]Tính toán dung lượng bộ nhớ cache L1/L2.#<p>Những điều này vượt quá phạm vi của mục tiêu quản trị hệ thống cơ bản 101.1.</p>
	####<p><strong>Explanation</strong>: Một trong những khu vực kiến thức chính là "Enable and disable integrated peripherals" (Bật và tắt các thiết bị ngoại vi tích hợp).</p>
}

// question: 11  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trên Linux, thẻ nhớ SD (SD cards) thường được xác định với đường dẫn thiết bị khối nào?</p>{
	~[moodle]/dev/sda.#<p>Dành cho SATA/SCSI.</p>
	~[moodle]/dev/hda.#<p>Dành cho thiết bị IDE legacy.</p>
	=[moodle]/dev/mmcblk0.
	~[moodle]/dev/nvme0.#<p>Dành cho thiết bị NVMe.</p>
	####<p><strong>Explanation</strong>: Thẻ nhớ SD (SD cards) sử dụng đường dẫn /dev/mmcblk0 cho thiết bị thứ nhất, và các phân vùng là /dev/mmcblk0p1, /dev/mmcblk0p2, v.v..</p>
}

// question: 12  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Trong mô hình đặt tên thiết bị Linux truyền thống, một thiết bị khối có tên là /dev/sdc đại diện cho điều gì?</p>{
	~[moodle]Phân vùng đầu tiên của ổ đĩa thứ ba.#<p>Sẽ là /dev/sdc1.</p>
	=[moodle]Toàn bộ ổ đĩa SATA/SCSI thứ ba.
	~[moodle]Ổ đĩa IDE đầu tiên.
	~[moodle]Thiết bị mạng đầu tiên.
	####<p><strong>Explanation</strong>: /dev/sdc đại diện cho toàn bộ ổ đĩa SATA/SCSI thứ ba được hệ thống phát hiện. Phân vùng của nó sẽ được đặt tên là /dev/sdc1, /dev/sdc2, v.v..</p>
}

// question: 13  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Mặc dù UEFI là một sự thay thế hiện đại, tại sao người ta vẫn thường gọi tiện ích cấu hình UEFI là BIOS?</p>{
	~[moodle]Vì UEFI chỉ là một biệt danh của BIOS.
	=[moodle]Vì cả hai triển khai đều đáp ứng cùng một mục đích cơ bản.
	~[moodle]Vì UEFI chỉ hỗ trợ các hệ thống x86, giống như BIOS.
	~[moodle]Vì các lệnh cấu hình trong UEFI hoàn toàn giống với BIOS.
	####<p><strong>Explanation</strong>: Mặc dù UEFI có các tính năng phức tạp hơn, việc vẫn gọi tiện ích cấu hình là BIOS là không hiếm, vì cả hai triển khai đều đáp ứng cùng một mục đích cơ bản.</p>
}

// question: 14  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Giá trị trọng số (Weight) của mục tiêu 101.1 "Determine and configure hardware settings" trong kỳ thi LPIC-1 là bao nhiêu?</p>{
	~[moodle]1.
	=[moodle]2.
	~[moodle]3.
	~[moodle]4.
	####<p><strong>Explanation</strong>: Trọng số (Weight) của mục tiêu 101.1 là 2.</p>
}

// question: 15  name: 101.1 Determine and configure hardware settings
::101.1 Determine and configure hardware settings::[html]<p>Chức năng nào sau đây là một trong những cải tiến mà UEFI mang lại so với BIOS truyền thống?</p>{
	~[moodle]Chỉ hỗ trợ hệ thống tệp MBR.
	=[moodle]Khả năng nhận dạng, kiểm tra và cấu hình tinh vi hơn.
	~[moodle]Chỉ sử dụng bootloader nằm trong MBR.
	~[moodle]Bỏ qua việc kiểm tra phần cứng khởi động.
	####<p><strong>Explanation</strong>: UEFI có các tính năng tinh vi hơn cho việc nhận dạng, kiểm tra, cấu hình và nâng cấp firmware so với BIOS truyền thống.</p>
}

// 101.2 Boot the system
$CATEGORY: $module$/top/101.2 Boot the system

// question: 1  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong một máy tính được trang bị firmware BIOS, tập tin nhị phân bootstrap (bootstrap binary) đầu tiên được tải nằm ở đâu?</p>{
	~[moodle]Trong phân vùng ESP (EFI System Partition).#<p>ESP liên quan đến khởi động UEFI.</p>
	~[moodle]Trong thư mục /boot của hệ thống tệp root.
	=[moodle]Trong Bản ghi khởi động chính (Master Boot Record - MBR) của thiết bị lưu trữ đầu tiên.
	~[moodle]Trong bộ nhớ NVRAM của firmware.#<p>NVRAM được sử dụng trong khởi động UEFI để lưu trữ định nghĩa về ứng dụng EFI.</p>
	####<p><strong>Explanation</strong>: Trên một máy tính có firmware BIOS, tập tin nhị phân bootstrap nằm trong MBR của thiết bị lưu trữ đầu tiên, theo định nghĩa trong tiện ích cấu hình BIOS.</p>
}

// question: 2  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Theo trình tự khởi động UEFI, ứng dụng EFI đã được xác định trước (thường là bootloader) được lưu trữ ở đâu?</p>{
	~[moodle]Trong thư mục /etc/.
	=[moodle]Trong phân vùng ESP (EFI System Partition) của hệ thống tệp.
	~[moodle]Trong MBR của ổ đĩa.#<p>MBR được sử dụng trong khởi động BIOS.</p>
	~[moodle]Trong /proc/.
	####<p><strong>Explanation</strong>: Firmware UEFI đọc các định nghĩa được lưu trữ trong NVRAM để thực thi ứng dụng EFI được xác định trước, ứng dụng này được lưu trữ trong hệ thống tệp của phân vùng ESP.</p>
}

// question: 3  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Giả sử hệ thống không thể khởi động do vị trí hệ thống tệp root bị sai. Tham số kernel nào cần được cung cấp để chỉ định vị trí hệ thống tệp root chính xác là /dev/sda3?</p>{
	~[moodle]init=/dev/sda3.#<p>init= dùng để chỉ định chương trình init/PID 1.</p>
	~[moodle]boot=/dev/sda3.
	=[moodle]root=/dev/sda3.
	~[moodle]mount=/dev/sda3.
	####<p><strong>Explanation</strong>: Tham số kernel được sử dụng để chỉ định vị trí hệ thống tệp root là root=, ví dụ: root=/dev/sda3.</p>
}

// question: 4  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Sau khi kernel được tải và khởi tạo, quá trình nào chịu trách nhiệm cho các giai đoạn khởi tạo hệ thống tiếp theo (System initialization stages)?</p>{
	~[moodle]UEFI firmware.
	~[moodle]Bootloader.#<p>Bootloader chịu trách nhiệm tải kernel và initramfs.</p>
	=[moodle]Chương trình Init (SysVinit, systemd, hoặc Upstart).
	~[moodle]Chương trình dmesg.
	####<p><strong>Explanation</strong>: Nhân (kernel) sau khi tải sẽ chuyển quyền điều khiển cho chương trình Init (PID 1), chương trình này (như SysVinit hoặc systemd) sẽ chịu trách nhiệm cho các giai đoạn khởi tạo hệ thống tiếp theo.</p>
}

// question: 5  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Lệnh nào được sử dụng để xem lại các thông báo khởi động của kernel (boot messages) trong các hệ thống sử dụng systemd?</p>{
	~[moodle]tail /var/log/syslog.#<p>Chỉ hiển thị các dòng cuối cùng của log file truyền thống.</p>
	=[moodle]journalctl -b.
	~[moodle]cat /proc/kmsg.
	~[moodle]dmesg -c.#<p>dmesg cũng hiển thị thông báo khởi động, nhưng journalctl là công cụ hiện đại hơn.</p>
	####<p><strong>Explanation</strong>: journalctl là lệnh được sử dụng để truy vấn nhật ký hệ thống (systemd journal). Tùy chọn -b (hoặc --boot) được sử dụng để hiển thị các thông báo từ lần khởi động hiện tại hoặc lần khởi động trước đó.</p>
}

// question: 6  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong trình tự khởi động UEFI, các định nghĩa cần thiết để thực thi ứng dụng EFI được lưu trữ ở đâu?</p>{
	~[moodle]MBR.
	~[moodle]RAM.
	=[moodle]NVRAM.
	~[moodle]Hệ thống tệp /tmp.
	####<p><strong>Explanation</strong>: Trong trình tự khởi động UEFI, firmware đọc các định nghĩa được lưu trữ trong NVRAM (Non-Volatile RAM) để thực thi ứng dụng EFI được xác định trước.</p>
}

// question: 7  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Công cụ nào cung cấp khả năng hiển thị các thông báo khởi động của kernel bằng cách truy cập bộ đệm vòng (ring buffer) của kernel?</p>{
	~[moodle]journalctl.
	=[moodle]dmesg.
	~[moodle]init.
	~[moodle]systemctl.
	####<p><strong>Explanation</strong>: dmesg là lệnh được sử dụng để hiển thị các thông báo từ bộ đệm vòng của kernel.</p>
}

// question: 8  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Khái niệm nào được bootloader tải vào bộ nhớ trước khi chuyển quyền điều khiển cho nhân (kernel) để giúp kernel truy cập các hệ thống tệp cần thiết (ví dụ: ổ đĩa root)?</p>{
	~[moodle]MBR.
	~[moodle]SysVinit.
	=[moodle]initramfs.
	~[moodle]UEFI.
	####<p><strong>Explanation</strong>: initramfs (initial RAM filesystem) là một hệ thống tệp nhỏ được tải vào bộ nhớ bởi bootloader, nó chứa các driver và tiện ích cần thiết để kernel có thể mount hệ thống tệp root thực sự.</p>
}

// question: 9  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Thuật ngữ nào mô tả một hệ thống init mà bạn cần phải có nhận thức (Awareness) về nó theo mục tiêu 101.2, bên cạnh SysVinit và systemd?</p>{
	~[moodle]cron.
	=[moodle]Upstart.
	~[moodle]runlevel.
	~[moodle]acpid.
	####<p><strong>Explanation</strong>: Các hệ thống init được đề cập là SysVinit, systemd, và nhận thức về Upstart.</p>
}

// question: 10  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Tham số nào được truyền cho kernel tại thời điểm khởi động để đặt chương trình init thay thế thay vì /sbin/init mặc định?</p>{
	=[moodle]init=.
	~[moodle]boot=.
	~[moodle]runlevel=.
	~[moodle]systemd=.
	####<p><strong>Explanation</strong>: Tham số init= cho phép người dùng chỉ định một chương trình sẽ chạy thay thế cho chương trình init mặc định (PID 1).</p>
}

// question: 11  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Giá trị trọng số (Weight) của mục tiêu 101.2 "Boot the system" trong kỳ thi LPIC-1 là bao nhiêu?</p>{
	~[moodle]1.
	~[moodle]2.
	=[moodle]3.
	~[moodle]4.
	####<p><strong>Explanation</strong>: Trọng số (Weight) của mục tiêu 101.2 là 3.</p>
}

// question: 12  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Trong trình tự khởi động, bootloader chịu trách nhiệm cho hành động nào ngay sau khi được kích hoạt bởi firmware (BIOS/UEFI)?</p>{
	~[moodle]Khởi tạo tất cả các thiết bị ngoại vi USB.
	=[moodle]Tải nhân hệ điều hành (kernel).
	~[moodle]Thiết lập cấu hình mạng.
	~[moodle]Chuyển sang chế độ đa người dùng.
	####<p><strong>Explanation</strong>: Mục đích duy nhất của bootloader là tải nhân hệ điều hành (kernel) và chuyển quyền kiểm soát cho nó.</p>
}

// question: 13  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Cấu trúc cơ bản nào trong hệ thống tệp kernel ảo được sử dụng để lưu trữ các thông báo nhật ký khởi động?</p>{
	~[moodle]/sys/.
	~[moodle]/proc/meminfo.
	=[moodle]Kernel ring buffer (được truy cập bằng dmesg).
	~[moodle]/var/log/messages.
	####<p><strong>Explanation</strong>: Các lệnh như dmesg phục hồi các thông báo khởi động của kernel bằng cách đọc bộ đệm vòng của kernel (kernel ring buffer).</p>
}

// question: 14  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Thuật ngữ nào trong systemd tương đương với khái niệm "runlevel" trong SysVinit?</p>{
	~[moodle]Service.
	~[moodle]Unit.
	=[moodle]Boot Target.
	~[moodle]Daemon.
	####<p><strong>Explanation</strong>: Trong systemd, các trạng thái hoạt động của hệ thống được gọi là Boot Targets (Mục tiêu Khởi động), thay thế cho Runlevels trong SysVinit.</p>
}

// question: 15  name: 101.2 Boot the system
::101.2 Boot the system::[html]<p>Sau khi kernel được tải, nó thực hiện hành động nào tiếp theo?</p>{
	~[moodle]Chuyển quyền điều khiển trở lại cho firmware.
	~[moodle]Khởi động lại hệ thống.
	=[moodle]Tải và giải nén initramfs trước khi chạy chương trình Init.
	~[moodle]Ngay lập tức hiển thị giao diện đồ họa.
	####<p><strong>Explanation</strong>: Sau khi bootloader tải kernel, kernel sẽ tải và giải nén initramfs (nếu có), sau đó chạy chương trình Init (PID 1) để bắt đầu quá trình khởi tạo hệ thống.</p>
}

// 101.3 Change runlevels / boot targets and shutdown or reboot system
$CATEGORY: $module$/top/101.3 Change runlevels / boot targets and shutdown or reboot system

// question: 1  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Lệnh telinit nên được sử dụng với số nào để thực hiện việc khởi động lại hệ thống (reboot) trong hệ thống dựa trên SysVinit?</p>{
	~[moodle]0.#<p>Runlevel 0 là tắt máy (shutdown).</p>
	~[moodle]1.#<p>Runlevel 1 là chế độ người dùng đơn (single user mode).</p>
	~[moodle]5.
	=[moodle]6.
	####<p><strong>Explanation</strong>: Lệnh telinit 6 sẽ chuyển sang runlevel 6, tức là khởi động lại hệ thống.</p>
}

// question: 2  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên SysVinit, điều gì sẽ xảy ra với các dịch vụ liên quan đến tập tin /etc/rc1.d/K90network khi hệ thống chuyển sang runlevel 1?</p>{
	~[moodle]Dịch vụ sẽ được khởi động do số 90.
	=[moodle]Dịch vụ sẽ được dừng lại (stopped) do ký tự 'K' đứng đầu tên tệp.
	~[moodle]Dịch vụ sẽ được khởi động do số 1 trong tên thư mục.
	~[moodle]Dịch vụ sẽ được khởi động lại.
	####<p><strong>Explanation</strong>: Do chữ cái K (Kill) ở đầu tên tệp, các dịch vụ liên quan sẽ bị dừng lại khi hệ thống đi vào runlevel 1.</p>
}

// question: 3  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên systemd, lệnh nào được sử dụng để kiểm tra xem đơn vị (unit) sshd.service có đang chạy hay không?</p>{
	=[moodle]systemctl status sshd.service.
	~[moodle]init status sshd.service.
	~[moodle]telinit sshd.service.
	~[moodle]wall sshd.service.#<p>wall dùng để gửi tin nhắn đến tất cả người dùng.</p>
	####<p><strong>Explanation</strong>: Lệnh systemctl status <unit> được sử dụng để xác minh trạng thái hoạt động của một đơn vị systemd, bao gồm cả dịch vụ.</p>
}

// question: 4  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Để đảm bảo dịch vụ sshd.service được kích hoạt (enabled) trong quá trình khởi tạo hệ thống (system initialization) trên hệ thống dựa trên systemd, lệnh nào phải được thực thi?</p>{
	~[moodle]systemctl start sshd.service.#<p>Chỉ khởi động dịch vụ trong phiên hiện tại.</p>
	~[moodle]systemctl disable sshd.service.
	=[moodle]systemctl enable sshd.service.
	~[moodle]telinit 5.
	####<p><strong>Explanation</strong>: Lệnh systemctl enable <unit> được sử dụng để kích hoạt một đơn vị, đảm bảo nó sẽ chạy khi hệ thống khởi động.</p>
}

// question: 5  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên systemd, lệnh nào có thể được sử dụng để xác định mục tiêu khởi động mặc định (default target) của hệ thống?</p>{
	~[moodle]cat /etc/inittab.
	=[moodle]systemctl get-default.
	~[moodle]systemctl set-default.
	~[moodle]init 5.
	####<p><strong>Explanation</strong>: Lệnh systemctl get-default sẽ hiển thị mục tiêu mặc định. Ngoài ra, có thể kiểm tra xem symbolic link /etc/systemd/system/default.target trỏ đến đâu.</p>
}

// question: 6  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Lệnh nào được sử dụng để hủy bỏ một lần khởi động lại hệ thống đã được lên lịch bằng lệnh shutdown?</p>{
	~[moodle]shutdown -k.
	=[moodle]shutdown -c.
	~[moodle]shutdown -r.
	~[moodle]init 0.
	####<p><strong>Explanation</strong>: Lệnh shutdown -c (cancel) được sử dụng để hủy bỏ một lần khởi động lại hoặc tắt máy đã được lên lịch.</p>
}

// question: 7  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Chế độ người dùng đơn (single user mode) trong SysVinit tương ứng với runlevel nào?</p>{
	~[moodle]0.
	=[moodle]1.
	~[moodle]3.
	~[moodle]5.
	####<p><strong>Explanation</strong>: Runlevel 1 (hoặc single hoặc s) là chế độ người dùng đơn.</p>
}

// question: 8  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Lệnh nào thường được sử dụng để gửi một tin nhắn cảnh báo đến tất cả người dùng đang đăng nhập trên hệ thống trước khi thực hiện hành động tắt máy hoặc khởi động lại?</p>{
	~[moodle]mail.
	~[moodle]echo.
	=[moodle]wall.
	~[moodle]logger.
	####<p><strong>Explanation</strong>: Lệnh wall (write all) được sử dụng để cảnh báo người dùng trước khi chuyển đổi runlevel/boot target hoặc các sự kiện hệ thống lớn khác.</p>
}

// question: 9  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong các hệ thống dựa trên SysVinit, tệp nào xác định runlevel mặc định mà hệ thống sẽ khởi động vào?</p>{
	~[moodle]/etc/init.d/.
	~[moodle]/etc/systemd/.
	=[moodle]/etc/inittab.
	~[moodle]/usr/lib/systemd/.
	####<p><strong>Explanation</strong>: Tệp /etc/inittab được sử dụng trong hệ thống SysVinit để xác định runlevel mặc định và các hành động liên quan đến runlevel.</p>
}

// question: 10  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Nếu lệnh shutdown +5 "Hệ thống sẽ tắt máy" được thực thi, điều gì sẽ xảy ra?</p>{
	~[moodle]Hệ thống tắt máy ngay lập tức.
	=[moodle]Hệ thống tắt máy sau 5 phút.
	~[moodle]Hệ thống khởi động lại sau 5 phút.
	~[moodle]Lệnh bị hủy ngay lập tức.
	####<p><strong>Explanation</strong>: Khi sử dụng cú pháp shutdown +m, hệ thống sẽ lên lịch tắt máy sau m phút, và tin nhắn sẽ được gửi đến tất cả người dùng.</p>
}

// question: 11  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong hệ thống dựa trên systemd, tệp /sbin/init là một liên kết tượng trưng (symbolic link) trỏ đến tệp thực thi nào?</p>{
	~[moodle]/etc/inittab.
	~[moodle]/bin/bash.
	=[moodle>Tệp thực thi chính của systemd (ví dụ: /lib/systemd/systemd).
	~[moodle]/etc/systemd/system/default.target.
	####<p><strong>Explanation</strong>: Trong các hệ thống dựa trên systemd, tệp /sbin/init là một liên kết tượng trưng trỏ đến tệp thực thi systemd chính.</p>
}

// question: 12  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Runlevel nào trong SysVinit thường được sử dụng cho việc tắt máy (halt)?</p>{
	=[moodle]0.
	~[moodle]1.
	~[moodle]5.
	~[moodle]6.
	####<p><strong>Explanation</strong>: Runlevel 0 thường được xác định là trạng thái dừng máy (halt/poweroff).</p>
}

// question: 13  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Trong cấu trúc thư mục SysVinit (/etc/rcX.d/), tên dịch vụ được đặt tiền tố là 'S' (Start) có ý nghĩa gì đối với dịch vụ đó khi hệ thống vào runlevel X?</p>{
	~[moodle]Dịch vụ sẽ bị bỏ qua.
	~[moodle]Dịch vụ sẽ bị dừng.
	=[moodle]Dịch vụ sẽ được khởi động.
	~[moodle]Dịch vụ sẽ bị xóa.
	####<p><strong>Explanation</strong>: Dịch vụ được đặt tiền tố 'S' (Start) trong thư mục runlevel có nghĩa là nó sẽ được khởi động khi hệ thống vào runlevel đó.</p>
}

// question: 14  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Lệnh nào sau đây là cách nhanh nhất để khởi động lại hệ thống ngay lập tức từ dòng lệnh mà không cần sử dụng shutdown hay telinit?</p>{
	=[moodle]reboot.
	~[moodle]init 5.
	~[moodle]wall.
	~[moodle]systemctl enable reboot.target.
	####<p><strong>Explanation</strong>: Lệnh reboot (hoặc systemctl reboot trong systemd) là cách phổ biến nhất để khởi động lại hệ thống ngay lập tức.</p>
}

// question: 15  name: 101.3 Change runlevels / boot targets and shutdown or reboot system
::101.3 Change runlevels / boot targets and shutdown or reboot system::[html]<p>Thư mục nào chứa các tệp đơn vị (unit files) mặc định được hệ thống systemd sử dụng?</p>{
	~[moodle]/etc/systemd/.
	~[moodle]/run/systemd/.
	=[moodle]/usr/lib/systemd/.
	~[moodle]/var/log/systemd/.
	####<p><strong>Explanation</strong>: Các tệp đơn vị (unit files) mặc định thường được lưu trữ trong /usr/lib/systemd/. Thư mục /etc/systemd/ thường chứa các tùy chỉnh cục bộ.</p>
}

// TOPIC 102: LINUX INSTALLATION AND PACKAGE MANAGEMENT
// 102.1 Design hard disk layout
$CATEGORY: $module$/top/102.1 Design hard disk layout

// question: 1  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Trong các hệ thống sử dụng BIOS legacy, để đảm bảo máy tính luôn có thể tải kernel, phân vùng /boot phải kết thúc trước cylinder nào?</p>{
	~[moodle]Cylinder 512.
	=[moodle]Cylinder 1024.
	~[moodle]Cylinder 2048.
	~[moodle]Không có giới hạn cylinder nào cho /boot.
	####<p><strong>Explanation</strong>: Để đảm bảo một PC luôn có thể tải kernel trong các hệ thống BIOS cũ, phân vùng khởi động phải kết thúc trước cylinder 1024.</p>
}

// question: 2  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Theo quy ước trong Linux, khi gắn kết (mounting) thủ công một hệ thống tệp không phải hệ thống tệp gốc hoặc /home, nó thường nên được gắn dưới thư mục nào?</p>{
	~[moodle]/var.
	~[moodle]/usr.
	=[moodle]/mnt.
	~[moodle]/etc.
	####<p><strong>Explanation</strong>: Khi gắn kết thủ công một hệ thống tệp, nó thường nên được gắn dưới /mnt. Lưu ý rằng điều này không bắt buộc.</p>
}

// question: 3  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Trong các hệ thống sử dụng UEFI, phân vùng EFI System Partition (ESP) thường được gắn ở đâu?</p>{
	~[moodle]/.
	~[moodle]/home.
	~[moodle]/boot.
	=[moodle]/boot/efi.
	####<p><strong>Explanation</strong>: Phân vùng EFI System Partition (ESP) thường được gắn dưới /boot/efi.</p>
}

// question: 4  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Trong LVM (Logical Volume Management), đơn vị nhỏ nhất nằm bên trong một Volume Group (VG) được gọi là gì?</p>{
	~[moodle]Logical Volume (LV).
	~[moodle]Physical Volume (PV).
	=[moodle]Extents (Physical Extents - PE).
	~[moodle]Partition Table.
	####<p><strong>Explanation</strong>: Volume Groups được chia thành các extent (hay Physical Extents), đây là đơn vị nhỏ nhất được sử dụng để định nghĩa kích thước của Logical Volume.</p>
}

// question: 5  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Trên một ổ đĩa được định dạng bằng lược đồ phân vùng MBR, ID được gán cho phân vùng EFI System Partition là gì?</p>{
	~[moodle]0x83 (Linux).
	~[moodle]0x07 (NTFS).
	=[moodle]0xEF.
	~[moodle]0x82 (Swap).
	####<p><strong>Explanation</strong>: Trên đĩa được định dạng với lược đồ phân vùng MBR, ID của EFI System Partition là 0xEF.</p>
}

// question: 6  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Tập tin cấu hình nào chứa thông tin về các điểm gắn kết (mount points) của hệ thống tệp để được gắn tự động khi khởi động?</p>{
	=[moodle]/etc/fstab.
	~[moodle]/etc/mtab.
	~[moodle]/boot/grub/grub.cfg.
	~[moodle]/dev/disk/by-uuid.
	####<p><strong>Explanation</strong>: /etc/fstab là tệp tiêu chuẩn quy định việc gắn kết tự động các hệ thống tệp khi khởi động.</p>
}

// question: 7  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Điều nào sau đây là ưu điểm chính của việc sử dụng LVM (Logical Volume Management)?</p>{
	~[moodle]Tăng tốc độ truy cập dữ liệu (I/O) cơ bản.
	=[moodle]Cung cấp khả năng tăng hoặc giảm kích thước Logical Volume một cách linh hoạt bằng cách thêm hoặc bớt extents.
	~[moodle]Loại bỏ hoàn toàn nhu cầu về phân vùng đĩa.
	~[moodle]Chỉ hỗ trợ các hệ thống tệp VFAT.
	####<p><strong>Explanation</strong>: LVM cho phép quản trị viên thêm hoặc bớt extents từ Volume Group có sẵn để tăng hoặc giảm kích thước Logical Volume.</p>
}

// question: 8  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Nếu một Logical Volume (LV) được tạo trên LVM, hệ điều hành sẽ coi nó là loại thiết bị nào?</p>{
	~[moodle]Một thư mục thông thường.
	~[moodle]Một tệp hoán đổi (swap file).
	=[moodle]Một thiết bị khối (block device) thông thường.
	~[moodle]Một cổng mạng ảo.
	####<p><strong>Explanation</strong>: Sau khi Logical Volume được tạo, hệ điều hành coi nó là một thiết bị khối thông thường, với đường dẫn theo định dạng /dev/VGNAME/LVNAME.</p>
}

// question: 9  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Loại không gian nào có thể được sử dụng để tăng không gian hoán đổi (swap space) trên Linux ngoài việc sử dụng phân vùng hoán đổi chuyên dụng?</p>{
	~[moodle]Ổ đĩa quang.
	~[moodle]Phân vùng EFI.
	=[moodle]Tệp hoán đổi (Swap files).
	~[moodle]Phân vùng /home.
	####<p><strong>Explanation</strong>: Ngoài các phân vùng swap, có thể sử dụng swap files (các tệp hoán đổi) để nhanh chóng tăng không gian hoán đổi trên hệ thống Linux.</p>
}

// question: 10  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Mục tiêu 102.1 nhấn mạnh việc phân bổ hệ thống tệp /home vào một phân vùng riêng biệt. Mục đích chính của việc này là gì?</p>{
	~[moodle]Tăng tốc độ khởi động hệ thống.
	=[moodle>Cách ly dữ liệu người dùng khỏi hệ điều hành, giúp việc sao lưu và nâng cấp hệ điều hành dễ dàng hơn.
	~[moodle]Giảm dung lượng đĩa cần thiết.
	~[moodle]Chỉ áp dụng cho hệ thống tệp ext4.
	####<p><strong>Explanation</strong>: Việc tách /home ra thành một phân vùng riêng (cùng với /var và /) là một phương pháp thiết kế để cách ly dữ liệu người dùng, cho phép quản trị viên dễ dàng quản lý, sao lưu hoặc cài đặt lại hệ điều hành mà không ảnh hưởng đến dữ liệu người dùng.</p>
}

// question: 11  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>LVM liên quan đến khái niệm "Physical Volume" (PV). PV được tạo từ đâu?</p>{
	~[moodle]Từ một tệp ẩn trong /dev/.
	=[moodle]Từ toàn bộ ổ đĩa hoặc một phân vùng đĩa.
	~[moodle]Từ một nhóm các Logical Volume.
	~[moodle]Từ các extents.
	####<p><strong>Explanation</strong>: Physical Volumes là các khối lưu trữ cơ bản mà LVM sử dụng, thường là toàn bộ một đĩa hoặc một phân vùng đĩa. PV sau đó được thêm vào Volume Groups.</p>
}

// question: 12  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Tập tin nào chứa các tập tin cần thiết cho bootloader GRUB trong quá trình khởi động?</p>{
	~[moodle]/etc/grub/.
	~[moodle]/var/log/grub/.
	=[moodle]/boot/grub/.
	~[moodle]/usr/bin/grub/.
	####<p><strong>Explanation</strong>: Các tệp cho bootloader GRUB được lưu trữ dưới /boot/grub.</p>
}

// question: 13  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Trong một Volume Group LVM có 100 extents vật lý, mỗi extent có kích thước 4MB. Một Logical Volume được tạo bằng 50 extents. Kích thước của Logical Volume đó là bao nhiêu?</p>{
	~[moodle]4MB.
	~[moodle]50MB.
	=[moodle]200MB.
	~[moodle]400MB.
	####<p><strong>Explanation</strong>: Kích thước của Logical Volume được định nghĩa bằng kích thước của extents vật lý nhân với số lượng extents trong volume. (50 * 4MB = 200MB).</p>
}

// question: 14  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Theo mục tiêu, các quản trị viên Linux cần có kiến thức cơ bản về tính năng nào của LVM?</p>{
	~[moodle]XFS.
	~[moodle]Partitions.
	=[moodle]Basic features of LVM.
	~[moodle]Mount points.
	####<p><strong>Explanation</strong>: Mục tiêu 102.1 yêu cầu "Knowledge of basic features of LVM" (Kiến thức về các tính năng cơ bản của LVM).</p>
}

// question: 15  name: 102.1 Design hard disk layout
::102.1 Design hard disk layout::[html]<p>Địa chỉ thiết bị nào sẽ được tạo trong /dev cho một Logical Volume có tên là data_lv thuộc Volume Group có tên là vg_archive?</p>{
	~[moodle]/dev/vg_archive_data_lv.
	~[moodle]/dev/data_lv/vg_archive.
	=[moodle]/dev/vg_archive/data_lv.
	~[moodle]/dev/lv_data_archive_vg.
	####<p><strong>Explanation</strong>: Thiết bị sẽ được tạo trong /dev với tên theo định dạng /dev/VGNAME/LVNAME, tức là /dev/vg_archive/data_lv.</p>
}

// 102.2 Install a boot manager
$CATEGORY: $module$/top/102.2 Install a boot manager

// question: 1  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Tệp cấu hình mặc định cho GRUB 2, tệp được tạo tự động và không khuyến nghị chỉnh sửa thủ công, nằm ở vị trí nào?</p>{
	~[moodle]/etc/default/grub.#<p>Đây là tệp được dùng để thay đổi cấu hình GRUB 2.</p>
	=[moodle]/boot/grub/grub.cfg.
	~[moodle]/etc/grub.d/40_custom.
	~[moodle]/boot/grub/menu.lst.
	####<p><strong>Explanation</strong>: Tệp cấu hình mặc định cho GRUB 2 là /boot/grub/grub.cfg. Tệp này được tạo tự động và không khuyến nghị chỉnh sửa thủ công.</p>
}

// question: 2  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Để thay đổi các cài đặt cấu hình cho GRUB 2, hai bước chính nào là cần thiết?</p>{
	~[moodle]Chỉnh sửa /boot/grub/grub.cfg và chạy grub-install.
	=[moodle]Chỉnh sửa /etc/default/grub và chạy update-grub.
	~[moodle]Chạy grub-mkconfig và sau đó khởi động lại hệ thống.
	~[moodle]Chỉnh sửa /boot/grub/menu.lst và chạy grub-install.
	####<p><strong>Explanation</strong>: Cần thực hiện thay đổi trong tệp /etc/default/grub, sau đó chạy tiện ích update-grub (hoặc grub-mkconfig) để tạo ra tệp cấu hình tuân thủ.</p>
}

// question: 3  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Trong GRUB 2, tệp nào được sử dụng để thêm các mục nhập menu tùy chỉnh (custom menu entries)?</p>{
	~[moodle]/etc/default/grub.
	=[moodle]/etc/grub.d/40_custom.
	~[moodle]/boot/grub/grub.cfg.
	~[moodle]/etc/grub.d/10_linux.
	####<p><strong>Explanation</strong>: Các mục nhập menu tùy chỉnh cho GRUB 2 nên được thêm vào tệp /etc/grub.d/40_custom.</p>
}

// question: 4  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Để vào GRUB Shell từ menu GRUB 2 hoặc GRUB Legacy, bạn cần nhấn phím nào?</p>{
	~[moodle]e.
	=[moodle]c.
	~[moodle]Enter.
	~[moodle]Tab.
	####<p><strong>Explanation</strong>: Để vào GRUB Shell từ màn hình menu, bạn nhấn phím c.</p>
}

// question: 5  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Trong GRUB Legacy, các mục nhập menu khởi động được lưu trữ ở đâu?</p>{
	~[moodle]/boot/grub/grub.cfg.
	~[moodle]/etc/grub.d/.
	=[moodle]/boot/grub/menu.lst.
	~[moodle]/etc/default/grub.
	####<p><strong>Explanation</strong>: Các mục nhập menu cho GRUB Legacy được lưu trữ trong /boot/grub/menu.lst.</p>
}

// question: 6  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Lệnh nào được sử dụng để cài đặt GRUB vào MBR của ổ đĩa, ví dụ: ổ đĩa /dev/sda?</p>{
	~[moodle]update-grub.
	~[moodle]grub-mkconfig.
	=[moodle]grub-install /dev/sda.
	~[moodle]setup (hd0).
	####<p><strong>Explanation</strong>: Lệnh grub-install được sử dụng để cài đặt GRUB vào Master Boot Record (MBR).</p>
}

// question: 7  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Giả sử bạn đang ở GRUB Legacy shell. Hai lệnh nào cần thiết để đặt thiết bị gốc (root device) là phân vùng đầu tiên của ổ đĩa thứ hai và cài đặt GRUB vào MBR của ổ đĩa đó?</p>{
	~[moodle]root (hd0,1) và setup (hd0).
	=[moodle]root (hd1,0) và setup (hd1).
	~[moodle]root /dev/sdb1 và setup /dev/sdb.
	~[moodle]set root=(hd1,0) và install (hd1).
	####<p><strong>Explanation</strong>: Trong cú pháp GRUB Legacy, ổ đĩa thứ hai là hd1, phân vùng đầu tiên là (hd1,0). Lệnh để đặt thiết bị gốc là root (hd1,0) và lệnh để cài đặt là setup (hd1).</p>
}

// question: 8  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Để đặt GRUB 2 đợi 10 giây trước khi khởi động mục menu mặc định, tham số nào nên được thêm vào tệp /etc/default/grub?</p>{
	~[moodle]GRUB_TIMEOUT_STYLE=10.
	~[moodle]GRUB_DEFAULT=10.
	=[moodle]GRUB_TIMEOUT=10.
	~[moodle]GRUB_WAIT=10.
	####<p><strong>Explanation</strong>: Tham số GRUB_TIMEOUT=10 được thêm vào /etc/default/grub sẽ đặt thời gian chờ là 10 giây trước khi khởi động mục mặc định.</p>
}

// question: 9  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Trong cấu hình menuentry của GRUB 2, tham số linux làm gì?</p>{
	~[moodle]Chỉ định thiết bị hoặc phân vùng để khởi động.
	=[moodle]Chỉ định đường dẫn đầy đủ đến ảnh kernel sẽ được tải.
	~[moodle]Đặt tiêu đề cho hệ điều hành trên màn hình menu.
	~[moodle]Chỉ định đường dẫn đến initramfs.
	####<p><strong>Explanation</strong>: Tham số linux (hoặc kernel trong GRUB Legacy) chỉ định đường dẫn đầy đủ đến ảnh kernel (vmlinuz) cần được tải khi mục nhập tương ứng được chọn.</p>
}

// question: 10  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Lệnh nào được sử dụng để tạo tệp cấu hình GRUB 2 (grub.cfg) sau khi thay đổi /etc/default/grub?</p>{
	~[moodle]grub-install.
	=[moodle]grub-mkconfig.
	~[moodle]menu.lst.
	~[moodle]grub-update.
	####<p><strong>Explanation</strong>: grub-mkconfig (thường được gọi thông qua update-grub trên Debian/Ubuntu) được sử dụng để tạo tệp cấu hình GRUB 2.</p>
}

// question: 11  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Một menu entry trong GRUB Legacy có ít nhất bao nhiêu lệnh cơ bản?</p>{
	~[moodle]Một (title).
	~[moodle]Hai (title, kernel).
	=[moodle]Ba (title, root, kernel).
	~[moodle]Bốn (title, root, kernel, initrd).
	####<p><strong>Explanation</strong>: Một mục nhập menu GRUB Legacy có ít nhất ba lệnh: title, root, và kernel.</p>
}

// question: 12  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Trong GRUB Legacy, tham số root có vai trò gì?</p>{
	~[moodle]Khởi động lại hệ thống.
	=[moodle]Cho GRUB biết thiết bị hoặc phân vùng để khởi động.
	~[moodle]Chỉ định đường dẫn tương đối của kernel.
	~[moodle]Hiển thị thông tin phiên bản GRUB.
	####<p><strong>Explanation</strong>: Lệnh root cho GRUB Legacy biết thiết bị hoặc phân vùng để khởi động.</p>
}

// question: 13  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Trong một mục nhập menu GRUB 2, tham số initrd chỉ định đường dẫn đến tệp nào?</p>{
	~[moodle]Nhân Linux (kernel).
	=[moodle]Tệp hệ thống tệp RAM ban đầu (initial RAM filesystem).
	~[moodle]Tệp cấu hình đĩa cứng.
	~[moodle]Tệp hệ thống tệp root.
	####<p><strong>Explanation</strong>: initrd (hoặc initramfs) chỉ định đường dẫn đến hệ thống tệp RAM ban đầu, cần thiết để kernel có thể mount hệ thống tệp root thực sự.</p>
}

// question: 14  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Khi một máy tính được bật nguồn, phần mềm nào chạy đầu tiên sau firmware (BIOS/UEFI)?</p>{
	~[moodle]Nhân hệ điều hành (Kernel).
	~[moodle]Shell dòng lệnh.
	=[moodle]Bootloader.
	~[moodle]Trình quản lý cửa sổ (Window Manager).
	####<p><strong>Explanation</strong>: Khi máy tính được bật nguồn, phần mềm đầu tiên chạy là bootloader.</p>
}

// question: 15  name: 102.2 Install a boot manager
::102.2 Install a boot manager::[html]<p>Điều gì xảy ra nếu bạn cố gắng chỉnh sửa trực tiếp tệp /boot/grub/grub.cfg trong GRUB 2?</p>{
	~[moodle]Các thay đổi sẽ có hiệu lực ngay lập tức.
	=[moodle]Các thay đổi sẽ bị ghi đè khi chạy update-grub hoặc khi cập nhật hệ thống.
	~[moodle]Hệ thống sẽ khởi động lại với cấu hình lỗi.
	~[moodle]Không thể chỉnh sửa tệp này vì nó bị khóa.
	####<p><strong>Explanation</strong>: Việc chỉnh sửa thủ công /boot/grub/grub.cfg không được khuyến nghị vì nó là tệp được tạo tự động và các thay đổi có thể bị mất khi chạy update-grub.</p>
}

// 102.3 Manage shared libraries
$CATEGORY: $module$/top/102.3 Manage shared libraries

// question: 1  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Lệnh nào được sử dụng để liệt kê các thư viện chia sẻ (shared libraries) mà một chương trình nhị phân (executable) yêu cầu?</p>{
	~[moodle]ldconfig.
	~[moodle]readelf.
	=[moodle]ldd.
	~[moodle]objdump.
	####<p><strong>Explanation</strong>: Lệnh ldd (list dynamic dependencies) in ra các đối tượng chia sẻ (shared objects) mà một chương trình phụ thuộc vào.</p>
}

// question: 2  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Sau khi thêm một thư mục chứa thư viện chia sẻ mới vào cấu hình hệ thống (ví dụ: tạo tệp .conf mới), lệnh nào cần chạy để cập nhật bộ nhớ cache của linker runtime?</p>{
	~[moodle]ldd -u.
	=[moodle]ldconfig.
	~[moodle]update-linker-cache.
	~[moodle]ld.so.conf -R.
	####<p><strong>Explanation</strong>: Lệnh ldconfig được sử dụng để tạo các liên kết cần thiết và cập nhật bộ nhớ cache được sử dụng bởi dynamic linker runtime.</p>
}

// question: 3  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Tên thư viện chia sẻ Linux tiêu chuẩn được cấu tạo từ những phần chính nào?</p>{
	~[moodle]Tên tệp đầy đủ, Loại mã hóa, Kích thước.
	=[moodle>Tên thư viện, Hậu tố .so, Số phiên bản.
	~[moodle]Đường dẫn tuyệt đối, Tên tiến trình, ID người dùng.
	~[moodle]Tên nhà phát triển, Mã băm (checksum), Thời gian tạo.
	####<p><strong>Explanation</strong>: Tên thư viện chia sẻ bao gồm: Tên thư viện (ví dụ: libprocps), hậu tố .so, và Số phiên bản (ví dụ: 6).</p>
}

// question: 4  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Biến môi trường nào được sử dụng để tạm thời thêm các đường dẫn thư viện không chuẩn vào danh sách tìm kiếm của dynamic linker?</p>{
	~[moodle]PATH.
	~[moodle]LD_PATH.
	=[moodle]LD_LIBRARY_PATH.
	~[moodle]MANPATH.
	####<p><strong>Explanation</strong>: Biến môi trường LD_LIBRARY_PATH được sử dụng để xác định các thư mục để dynamic linker tìm kiếm các thư viện chia sẻ tại thời điểm chạy.</p>
}

// question: 5  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Tập tin cấu hình chính, nơi lưu trữ danh sách các thư mục chứa thư viện chia sẻ mặc định của hệ thống, là gì?</p>{
	~[moodle]/etc/ld.so.cache.
	=[moodle]/etc/ld.so.conf.
	~[moodle]/etc/rc.local.
	~[moodle]/usr/lib/libdir.
	####<p><strong>Explanation</strong>: Tập tin /etc/ld.so.conf chứa các thư mục mà ldconfig sẽ quét để tìm các thư viện chia sẻ.</p>
}

// question: 6  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Công cụ nào có thể được sử dụng để in thông tin từ các tệp đối tượng (object files), bao gồm thông tin về các thư viện chia sẻ?</p>{
	~[moodle]ldd.
	~[moodle]ldconfig.
	=[moodle]objdump.
	~[moodle]objcopy.
	####<p><strong>Explanation</strong>: objdump là tiện ích dòng lệnh hiển thị thông tin từ các tệp đối tượng.</p>
}

// question: 7  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>ELF là viết tắt của gì trong ngữ cảnh các tệp nhị phân và thư viện chia sẻ của Linux?</p>{
	~[moodle]Executable Linux Framework.
	~[moodle]Embedded Library Format.
	=[moodle]Executable and Linkable Format.
	~[moodle]Extended Local File.
	####<p><strong>Explanation</strong>: ELF là viết tắt của Executable and Linkable Format, là định dạng tệp tiêu chuẩn cho các tệp nhị phân, thư viện chia sẻ, và tệp đối tượng trên Linux.</p>
}

// question: 8  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Lệnh nào bạn sẽ sử dụng để liệt kê các thư viện chia sẻ mà lệnh kill yêu cầu?</p>{
	~[moodle]ldconfig /bin/kill.
	=[moodle]ldd /bin/kill.
	~[moodle]objdump /bin/kill.
	~[moodle]kill -ldd.
	####<p><strong>Explanation</strong>: Để liệt kê các thư viện chia sẻ yêu cầu bởi một lệnh, bạn sử dụng ldd theo sau là đường dẫn tuyệt đối của lệnh đó, ví dụ: ldd /bin/kill.</p>
}

// question: 9  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Tệp /etc/ld.so.cache được tạo ra bằng lệnh nào và mục đích của nó là gì?</p>{
	~[moodle]Được tạo bằng ldd để lưu trữ đường dẫn thư viện tạm thời.
	=[moodle]Được tạo bằng ldconfig để tăng tốc độ tìm kiếm thư viện cho dynamic linker.
	~[moodle]Được tạo thủ công để định nghĩa các thư mục tìm kiếm.
	~[moodle]Được tạo khi kernel khởi động để lưu trữ driver.
	####<p><strong>Explanation</strong>: Tệp /etc/ld.so.cache là bộ nhớ cache được xây dựng bởi ldconfig để lưu trữ các đường dẫn thư viện được xác định, giúp dynamic linker nhanh chóng tìm thấy các thư viện cần thiết.</p>
}

// question: 10  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Giả sử bạn có thư viện libsample.so.1.2.3. Phần nào đại diện cho số phiên bản (Version number)?</p>{
	~[moodle]libsample.
	=[moodle]1.2.3.
	~[moodle].so.
	~[moodle]sample.
	####<p><strong>Explanation</strong>: Trong cấu trúc tên thư viện chia sẻ (ví dụ: libsample.so.1.2.3), 1.2.3 là số phiên bản.</p>
}

// question: 11  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Nếu bạn tạo một tệp cấu hình thư viện tùy chỉnh mới tên là mylib.conf và đặt đường dẫn tuyệt đối /opt/lib/mylib vào đó, tệp này nên được đặt trong thư mục nào để được ldconfig nhận diện?</p>{
	~[moodle]/etc/.
	~[moodle]/var/lib/.
	=[moodle]/etc/ld.so.conf.d/.
	~[moodle]/usr/local/lib/.
	####<p><strong>Explanation</strong>: Tốt nhất là nên đặt tệp cấu hình thư viện tùy chỉnh trong thư mục /etc/ld.so.conf.d/ để nó được tệp /etc/ld.so.conf bao gồm và được ldconfig xử lý.</p>
}

// question: 12  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Lệnh readelf được sử dụng để hiển thị thông tin về loại tệp nào?</p>{
	~[moodle]Tệp văn bản thuần túy.
	~[moodle]Tệp hình ảnh.
	=[moodle]Tệp ELF (Executable and Linkable Format).
	~[moodle]Tệp log.
	####<p><strong>Explanation</strong>: readelf hiển thị thông tin về các tệp ELF, là định dạng tiêu chuẩn cho các tệp nhị phân và thư viện trên Linux.</p>
}

// question: 13  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Mục tiêu của việc quản lý thư viện chia sẻ là gì?</p>{
	~[moodle]Đảm bảo tất cả các chương trình đều sử dụng các thư viện tĩnh.
	=[moodle]Đảm bảo các chương trình có thể tìm và tải các thư viện cần thiết tại thời điểm chạy.
	~[moodle]Tăng kích thước tệp nhị phân.
	~[moodle]Chỉ sử dụng thư viện hệ thống mặc định.
	####<p><strong>Explanation</strong>: Thư viện chia sẻ giúp giảm kích thước nhị phân và tiết kiệm bộ nhớ, nhưng mục tiêu quản lý là đảm bảo các chương trình có thể tìm và tải các thư viện này (Dynamic Linking).</p>
}

// question: 14  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Thư viện ld-linux-x86-64.so.2 có vai trò gì trong hệ thống Linux?</p>{
	~[moodle]Đây là thư viện toán học cơ bản.
	=[moodle]Đây là dynamic linker/loader (trình liên kết/tải động).
	~[moodle]Đây là thư viện hệ thốngd chính.
	~[moodle]Đây là một trình điều khiển ảo.
	####<p><strong>Explanation</strong>: Trong các hệ thống Linux, các tệp như ld-linux-x86-64.so.2 thực chất là dynamic linker/loader, chịu trách nhiệm tải các thư viện chia sẻ cần thiết cho chương trình khi nó chạy.</p>
}

// question: 15  name: 102.3 Manage shared libraries
::102.3 Manage shared libraries::[html]<p>Trọng số (Weight) của mục tiêu 102.3 "Manage shared libraries" trong kỳ thi LPIC-1 là bao nhiêu?</p>{
	=[moodle]1.
	~[moodle]2.
	~[moodle]3.
	~[moodle]4.
	####<p><strong>Explanation</strong>: Trọng số (Weight) của mục tiêu 102.3 là 1.</p>
}

// 102.4 Use Debian package management
$CATEGORY: $module$/top/102.4 Use Debian package management

// question: 1  name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Lệnh nào nên được sử dụng trước khi cài đặt hoặc cập nhật gói bằng apt hoặc apt-get để đảm bảo chỉ mục gói (package index) là mới nhất?</p>{
	~[moodle]apt install.
	~[moodle]apt upgrade.
	=[moodle]apt update.
	~[moodle]dpkg -i.
	####<p><strong>Explanation</strong>: Lệnh apt update (hoặc apt-get update) phải được sử dụng để đảm bảo chỉ mục gói là mới nhất, đồng bộ hóa danh sách gói từ các kho lưu trữ.</p>
}

// question: 2  name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Lệnh nào được sử dụng để hiển thị thông tin chi tiết (như mô tả, phiên bản, phụ thuộc) của một gói có sẵn trong cache (ví dụ: gói gimp)?</p>{
	~[moodle]dpkg -i gimp.
	~[moodle]apt-cache search gimp.
	=[moodle]apt-cache show gimp.
	~[moodle]apt install gimp.
	####<p><strong>Explanation</strong>: Lệnh apt-cache show <package> được sử dụng để hiển thị thông tin chi tiết về gói từ cache của APT.</p>
}

// question: 3  name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Trong hệ thống Debian, tệp nào chứa danh sách các kho lưu trữ (repositories) mà APT sử dụng để tìm kiếm và tải xuống gói?</p>{
	~[moodle]/etc/dpkg.conf.
	=[moodle]/etc/apt/sources.list.
	~[moodle]/etc/package.list.
	~[moodle]/var/cache/apt/.
	####<p><strong>Explanation</strong>: Các kho lưu trữ được định nghĩa trong tệp /etc/apt/sources.list.</p>
}

// question: 4  name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Giả sử gói file-roller phụ thuộc vào gói unzip. Nếu bạn cố gắng loại bỏ unzip bằng lệnh dpkg -r unzip, điều gì sẽ xảy ra?</p>{
	~[moodle]Gói unzip sẽ bị gỡ bỏ thành công và file-roller tiếp tục hoạt động.
	=[moodle]Lệnh sẽ thất bại do phụ thuộc chưa được đáp ứng.
	~[moodle]file-roller cũng sẽ bị xóa tự động.
	~[moodle]Hệ thống sẽ buộc bạn phải cài đặt một gói thay thế cho unzip.
	####<p><strong>Explanation</strong>: dpkg -r chỉ loại bỏ gói được chỉ định và không giải quyết các phụ thuộc ngược (reverse dependencies). Lệnh sẽ thất bại vì file-roller vẫn phụ thuộc vào unzip.</p>
}

// question: 5  name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Lệnh nào được sử dụng để tìm kiếm gói nào chứa một tệp cụ thể (ví dụ: /usr/bin/unrar) mà chưa được cài đặt trên hệ thống (yêu cầu tiện ích apt-file)?</p>{
	~[moodle]dpkg -S /usr/bin/unrar.
	~[moodle]apt-cache search /usr/bin/unrar.
	=[moodle]apt-file search /usr/bin/unrar.
	~[moodle]apt which /usr/bin/unrar.
	####<p><strong>Explanation</strong>: Lệnh apt-file search <file_path> được sử dụng để tìm kiếm gói nào chứa tệp đó, kể cả khi gói đó chưa được cài đặt.</p>
}

// question: 6  name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Lệnh nào sau đây sẽ gỡ bỏ gói (package) và cả các tệp cấu hình của nó?</p>{
	~[moodle]dpkg -r <package>.
	~[moodle]dpkg --remove <package>.
	=[moodle]apt-get purge <package>.
	~[moodle]apt-get clean <package>.
	####<p><strong>Explanation</strong>: apt-get purge (hoặc apt purge) loại bỏ gói và cả các tệp cấu hình liên quan. dpkg -r chỉ loại bỏ tệp nhị phân và giữ lại tệp cấu hình.</p>
	
// question: 7 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Lệnh nào được sử dụng để cài đặt một gói nhị phân Debian (.deb) đã tải xuống (ví dụ: google-chrome.deb) ở cấp độ thấp, không tự động giải quyết phụ thuộc?</p>{
	~[moodle]apt install google-chrome.deb
	=[moodle]dpkg -i google-chrome.deb
	~[moodle]apt-get install google-chrome.deb
	~[moodle]dpkg --configure google-chrome.deb
	####<p><strong>Giải thích</strong>: dpkg -i (install) được sử dụng để cài đặt các gói nhị phân Debian cục bộ.</p>
}

// question: 8 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Lệnh nào có thể được sử dụng để liệt kê các tệp đã được cài đặt thuộc về một gói đã cài đặt (transmission-gtk)?</p>{
	=[moodle]dpkg -L transmission-gtk
	~[moodle]apt-file show transmission-gtk
	~[moodle]apt-cache depends transmission-gtk
	~[moodle]dpkg --get-files transmission-gtk
	####<p><strong>Giải thích</strong>: dpkg -L <package> liệt kê nội dung (các tệp) của gói đã được cài đặt.</p>
}

// question: 9 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Tiện ích nào được sử dụng để cấu hình lại (reconfigure) một gói đã cài đặt (ví dụ: nếu bạn cần thay đổi cài đặt ban đầu)?</p>{
	~[moodle]apt-cache configure
	=[moodle]dpkg-reconfigure
	~[moodle]apt-get config
	~[moodle]dpkg -C
	####<p><strong>Giải thích</strong>: dpkg-reconfigure chạy lại tập lệnh cấu hình của gói, cho phép người dùng thay đổi các tùy chọn đã được thiết lập ban đầu.</p>
}

// question: 10 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Theo danh sách Phụ thuộc (Dependencies) của gói openshot-qt (trong ví dụ), điều gì được chỉ định là vấn đề chính ngăn cản việc cài đặt thành công nếu các gói phụ thuộc không được cài đặt?</p>{
	~[moodle]Gói cần quyền root để cài đặt.
	=[moodle]Các gói phụ thuộc không được cài đặt.
	~[moodle]Phiên bản kernel không tương thích.
	~[moodle]Thiếu dung lượng đĩa.
	####<p><strong>Giải thích</strong>: Ví dụ lỗi cho thấy openshot-qt depends on python3-openshot; however: Package python3-openshot is not installed, chỉ ra vấn đề về các gói phụ thuộc chưa được cài đặt.</p>
}

// question: 11 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Lệnh nào trong APT/dpkg được sử dụng để kiểm tra tính toàn vẹn (integrity) của gói?</p>{
	~[moodle]apt check
	=[moodle]dpkg -V <package>
	~[moodle]dpkg -s <package>
	~[moodle]apt-file check
	####<p><strong>Giải thích</strong>: dpkg -V (verify) kiểm tra tính toàn vẹn của các tệp đã cài đặt thuộc về một gói.</p>
}

// question: 12 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Giá trị trọng số (Weight) của mục tiêu 102.4 "Use Debian package management" trong kỳ thi LPIC-1 là bao nhiêu?</p>{
	~[moodle]1
	~[moodle]2
	=[moodle]3
	~[moodle]4
	####<p><strong>Giải thích</strong>: Trọng số (Weight) của mục tiêu 102.4 là 3.</p>
}

// question: 13 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Lệnh nào sau đây sẽ liệt kê tất cả các gói đã được cài đặt trên hệ thống?</p>{
	~[moodle]apt list
	~[moodle]dpkg --get-selections
	~[moodle]apt-cache showall
	=[moodle]dpkg-query -l
	####<p><strong>Giải thích</strong>: dpkg -l (list) hoặc dpkg-query -l liệt kê tất cả các gói đã được cài đặt.</p>
}

// question: 14 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Sau khi chạy apt update, nếu bạn muốn nâng cấp tất cả các gói đã cài đặt lên phiên bản mới nhất, nhưng KHÔNG muốn loại bỏ các gói hoặc cài đặt các gói phụ thuộc mới (ngoài các gói cần thiết để giải quyết các phụ thuộc hiện có), bạn sẽ sử dụng lệnh nào?</p>{
	=[moodle]apt upgrade
	~[moodle]apt dist-upgrade
	~[moodle]apt full-upgrade
	~[moodle]apt remove --autoremove
	####<p><strong>Giải thích</strong>: apt upgrade thực hiện nâng cấp mà không gỡ bỏ các gói đã cài đặt hoặc cài đặt các gói phụ thuộc mới (ngoài những gói cần thiết để giải quyết các phụ thuộc hiện có). dist-upgrade (hoặc full-upgrade) là cho phép gỡ bỏ/cài đặt các gói mới để giải quyết thay đổi phụ thuộc lớn hơn.</p>
}

// question: 15 name: 102.4 Use Debian package management
::102.4 Use Debian package management::[html]<p>Công cụ nào của Debian được thiết kế để dễ dàng hơn cho người dùng cuối trong việc quản lý gói, hoạt động như một lớp trừu tượng phía trên dpkg và apt-get?</p>{
	~[moodle]dpkg-reconfigure
	=[moodle]apt
	~[moodle]apt-cache
	~[moodle]apt-file
	####<p><strong>Giải thích</strong>: apt (hoặc apt-get) là các tiện ích cấp cao được xây dựng để xử lý các tác vụ quản lý gói phức tạp, bao gồm cả giải quyết phụ thuộc, so với dpkg cấp thấp.</p>
}

// 102.5 Use RPM and YUM package management
// question: 1 name: Switch category to $module$/top/102.5 Use RPM and YUM package management
$CATEGORY: $module$/top/102.5 Use RPM and YUM package management

// question: 1 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Trong RPM, tham số nào được sử dụng để cài đặt một gói (.rpm) và hiển thị thanh tiến trình (progress bar)?</p>{
	~[moodle]-i
	~[moodle]-h
	=[moodle]-ih
	~[moodle]-Uvh
	####<p><strong>Giải thích</strong>: Tham số -i dùng để cài đặt gói, và tùy chọn -h (hash marks) cho phép hiển thị thanh tiến trình trong quá trình cài đặt.</p>
}

// question: 2 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Lệnh nào được sử dụng với yum để kiểm tra các bản cập nhật có sẵn cho tất cả các gói đã cài đặt trên hệ thống?</p>{
	~[moodle]yum update
	~[moodle]yum list updates
	=[moodle]yum check-update
	~[moodle]yum upgrade
	####<p><strong>Giải thích</strong>: yum check-update được sử dụng để kiểm tra các bản cập nhật cho tất cả các gói trong hệ thống.</p>
}

// question: 3 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Để tìm gói nào cung cấp một tệp cụ thể (ví dụ: /bin/wget) bằng cách sử dụng yum, lệnh nào là chính xác?</p>{
	~[moodle]yum provides /bin/wget
	~[moodle]yum search /bin/wget
	=[moodle]yum whatprovides /bin/wget
	~[moodle]rpm -qf /bin/wget.#<p>rpm -qf chỉ hoạt động nếu tệp đó đã được cài đặt.</p>
	####<p><strong>Giải thích</strong>: Lệnh yum whatprovides <file_path> được sử dụng để tìm kiếm gói nào cung cấp tệp đó.</p>
}

// question: 4 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Lệnh nào trong zypper được sử dụng để tìm kiếm các gói đã được cài đặt (unzip)?</p>{
	~[moodle]zypper info unzip
	~[moodle]zypper search unzip
	=[moodle]zypper se -i unzip
	~[moodle]zypper list unzip
	####<p><strong>Giải thích</strong>: Lệnh zypper se -i <package> (search installed) được sử dụng để tìm kiếm gói đã được cài đặt.</p>
}

// question: 5 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Nếu bạn có một tệp .repo mô tả một kho lưu trữ mới cho DNF/YUM, tệp này nên được đặt ở đâu để DNF/YUM nhận ra nó?</p>{
	~[moodle]/etc/dnf.conf
	~[moodle]/etc/yum.conf
	=[moodle]/etc/yum.repos.d/
	~[moodle]/usr/local/repo/
	####<p><strong>Giải thích</strong>: Các tệp .repo mô tả kho lưu trữ nên được đặt trong thư mục /etc/yum.repos.d/ để được DNF/YUM nhận diện.</p>
}

// question: 6 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Lệnh nào của RPM được sử dụng để truy vấn (query) tệp nào thuộc về gói đã được cài đặt?</p>{
	=[moodle]rpm -ql <package>
	~[moodle]rpm -qi <package>
	~[moodle]rpm -qf <file_path>
	~[moodle]rpm -qa
	####<p><strong>Giải thích</strong>: rpm -ql <package> được sử dụng để liệt kê tất cả các tệp thuộc về gói đã được cài đặt.</p>
}

// question: 7 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Giả sử bạn muốn gỡ bỏ (remove) một kho lưu trữ có tên là packman bằng zypper. Lệnh nào là chính xác?</p>{
	~[moodle]zypper remove packman
	=[moodle]zypper removerepo packman
	~[moodle]zypper disable packman
	~[moodle]zypper clean packman
	####<p><strong>Giải thích</strong>: Lệnh zypper removerepo <repo_name> được sử dụng để xóa một kho lưu trữ.</p>
}

// question: 8 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Công cụ quản lý gói mới hơn nào đang được sử dụng thay thế cho YUM trên các bản phân phối dựa trên Red Hat (như Fedora, RHEL mới hơn)?</p>{
	~[moodle]apt
	~[moodle]zypper
	=[moodle]dnf
	~[moodle]rpm
	####<p><strong>Giải thích</strong>: DNF (Dandified YUM) là trình quản lý gói thế hệ tiếp theo, đang dần thay thế YUM.</p>
}

// question: 9 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Lệnh RPM nào được sử dụng để xác định gói nào đã cài đặt chứa tệp /etc/redhat-release?</p>{
	=[moodle]rpm -qf /etc/redhat-release
	~[moodle]rpm -qi /etc/redhat-release
	~[moodle]yum whatprovides /etc/redhat-release
	~[moodle]zypper se -i /etc/redhat-release
	####<p><strong>Giải thích</strong>: Lệnh rpm -qf <file_path> được sử dụng để truy vấn gói nào sở hữu tệp được chỉ định (-q query, -f file).</p>
}

// question: 10 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Tệp nào chứa các tùy chọn cấu hình toàn cục cho YUM?</p>{
	~[moodle]/etc/dnf.conf
	~[moodle]/etc/yum.repos.d/
	=[moodle]/etc/yum.conf
	~[moodle]/var/log/yum.log
	####<p><strong>Giải thích</strong>: /etc/yum.conf là tệp cấu hình chính cho YUM.</p>
}

// question: 11 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Nếu bạn muốn nâng cấp một gói (ví dụ: new_app.rpm) bằng RPM, tùy chọn cơ bản nào là thích hợp nhất?</p>{
	~[moodle]rpm -i new_app.rpm
	~[moodle]rpm -h new_app.rpm
	=[moodle]rpm -U new_app.rpm
	~[moodle]rpm -e new_app.rpm
	####<p><strong>Giải thích</strong>: rpm -U (upgrade) là tùy chọn tiêu chuẩn để nâng cấp gói.</p>
}

// question: 12 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Mục tiêu 102.5 yêu cầu kiến thức về các tác vụ nào liên quan đến gói RPM?</p>{
	~[moodle]Chỉ cài đặt và xóa.
	=[moodle]Cài đặt, cài đặt lại, nâng cấp và xóa.
	~[moodle]Chỉ cài đặt và nâng cấp.
	~[moodle]Chỉ kiểm tra tính toàn vẹn và chữ ký.
	####<p><strong>Giải thích</strong>: Các tác vụ chính là "Install, re-install, upgrade and remove packages using RPM, YUM and Zypper".</p>
}

// question: 13 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Lệnh yum history có mục đích gì?</p>{
	~[moodle]Hiển thị lịch sử các lệnh được gõ trong terminal.
	=[moodle]Hiển thị thông tin về các giao dịch gói đã được thực hiện bằng YUM/DNF (ví dụ: cài đặt, xóa).
	~[moodle]Hiển thị lịch sử các phiên bản RPM đã được phát hành.
	~[moodle]Hiển thị lịch sử sử dụng ổ đĩa.
	####<p><strong>Giải thích</strong>: yum history (hoặc dnf history) hiển thị các giao dịch quản lý gói đã được thực hiện trước đó.</p>
}

// question: 14 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Lệnh nào của RPM được sử dụng để hiển thị thông tin về nhà cung cấp (Vendor) và ngày xây dựng (Build Date) của một gói?</p>{
	~[moodle]rpm -ql <package>
	~[moodle]rpm -qa
	=[moodle]rpm -qi <package>
	~[moodle]rpm -V <package>
	####<p><strong>Giải thích</strong>: rpm -qi <package> (query information) hiển thị thông tin chi tiết của gói, bao gồm Vendor, Build Date và mô tả.</p>
}

// question: 15 name: 102.5 Use RPM and YUM package management
::102.5 Use RPM and YUM package management::[html]<p>Công cụ nào của SUSE/OpenSUSE tương đương với YUM/DNF trên Red Hat Enterprise Linux?</p>{
	~[moodle]dpkg
	=[moodle]zypper
	~[moodle]rpm
	~[moodle]apt-get
	####<p><strong>Giải thích</strong>: zypper là công cụ quản lý gói chính được sử dụng trong các bản phân phối dựa trên SUSE.</p>
}

// 102.6 Linux as a virtualization guest
// question: 1 name: Switch category to $module$/top/102.6 Linux as a virtualization guest
$CATEGORY: $module$/top/102.6 Linux as a virtualization guest

// question: 1 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Các tiện ích mở rộng CPU nào là cần thiết trên nền tảng phần cứng x86 để chạy các máy ảo khách được ảo hóa hoàn toàn (fully virtualized guests)?</p>{
	~[moodle]Hyper-Threading và Multicore.
	~[moodle]cgroups và Namespaces.
	=[moodle]Intel VT-x hoặc AMD-V.
	~[moodle]SSE4 và AVX.
	####<p><strong>Giải thích</strong>: Để ảo hóa hoàn toàn (fully virtualized) diễn ra trên phần cứng x86, các tiện ích mở rộng CPU Intel VT-x hoặc AMD-V phải được bật trong firmware (BIOS/UEFI).</p>
}

// question: 2 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Loại máy ảo khách nào (guest) có khả năng cung cấp hiệu suất tốt hơn so với ảo hóa hoàn toàn, do sử dụng nhân đã được sửa đổi và trình điều khiển đặc biệt?</p>{
	~[moodle]Fully Virtualized Guest (FVM).
	~[moodle]Hyper-V Guest.
	=[moodle]Paravirtualized Guest (PVM).
	~[moodle]Application Container.
	####<p><strong>Giải thích</strong>: Máy ảo khách được ảo hóa bán phần (Paravirtualized Guest - PVM) sử dụng nhân đã được sửa đổi và trình điều khiển đặc biệt (guest drivers) để tận dụng tài nguyên phần mềm và phần cứng của hypervisor, thường mang lại hiệu suất tốt hơn.</p>
}

// question: 3 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Khi một hệ thống Linux được nhân bản (cloned) hoặc được sử dụng làm mẫu (template), thuộc tính nào sau đây cần được thay đổi để tránh hành vi bất thường, đặc biệt là liên quan đến D-Bus?</p>{
	~[moodle]Địa chỉ MAC.
	=[moodle]D-Bus Machine ID.
	~[moodle]Cấu hình DNS.
	~[moodle]Tên người dùng root.
	####<p><strong>Giải thích</strong>: Khi một hệ thống được nhân bản từ một template, các thuộc tính duy nhất như SSH host keys và D-Bus Machine ID cần được thay đổi để tránh sự cố.</p>
}

// question: 4 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Lệnh nào được sử dụng để xác định và xem D-Bus ID của hệ thống hiện tại?</p>{
	~[moodle]ssh-keygen -l
	=[moodle]dbus-uuidgen --get
	~[moodle]grep D-Bus /etc/
	~[moodle]systemctl status dbus
	####<p><strong>Giải thích</strong>: Lệnh dbus-uuidgen --get được sử dụng để xác minh và xem D-Bus ID của hệ thống.</p>
}

// question: 5 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Công cụ nào được thiết kế để hỗ trợ việc cấu hình và triển khai máy ảo và container lên môi trường đám mây?</p>{
	~[moodle]ssh-keygen
	~[moodle]dbus-uuidgen
	=[moodle]cloud-init
	~[moodle]systemd
	####<p><strong>Giải thích</strong>: cloud-init là một công cụ giúp cấu hình và triển khai máy ảo và container lên môi trường đám mây.</p>
}

// question: 6 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Trong kiến trúc máy ảo, các trình điều khiển đặc biệt được sử dụng bởi máy ảo khách được ảo hóa bán phần (PVM) được gọi là gì?</p>{
	~[moodle]Kernelspace processes.
	~[moodle]Application containers.
	=[moodle]Guest drivers.
	~[moodle]Hypervisor extensions.
	####<p><strong>Giải thích</strong>: Máy ảo khách PVM sử dụng các trình điều khiển đặc biệt, được gọi là guest drivers, để giao tiếp với hypervisor.</p>
}

// question: 7 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Công nghệ nào được đề cập nhưng không cần thiết phải có kiến thức chuyên sâu để vượt qua kỳ thi LPIC-1, mặc dù nó được sử dụng để phân đoạn ứng dụng vì mục đích sử dụng tài nguyên hệ thống?</p>{
	=[moodle]cgroups (Control Groups)
	~[moodle]Containers
	~[moodle]Virtual machines
	~[moodle]SSH
	####<p><strong>Giải thích</strong>: Mặc dù khái niệm về cgroups (Control Groups) được đề cập để cung cấp kiến thức nền tảng về cách ứng dụng được phân đoạn để quản lý tài nguyên, kiến thức về nó hiện không cần thiết để vượt qua kỳ thi LPIC-1.</p>
}

// question: 8 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Lệnh nào có thể được sử dụng để kiểm tra xem CPU của bạn có bật các tiện ích mở rộng ảo hóa (vmx cho Intel hoặc svm cho AMD) hay không?</p>{
	~[moodle]lspci -v
	~[moodle]lsmod | grep hypervisor
	=[moodle]grep -E "vmx|svm" /proc/cpuinfo
	~[moodle]dmesg | grep virtualization
	####<p><strong>Giải thích</strong>: grep -E "vmx|svm" /proc/cpuinfo sẽ tìm kiếm các cờ (flag) CPU cho biết hỗ trợ ảo hóa (vmx cho Intel VT-x và svm cho AMD-V).</p>
}

// question: 9 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Loại container nào cung cấp sự ảo hóa cấp hệ điều hành (OS-level virtualization) bằng cách chia sẻ kernel host nhưng cung cấp môi trường người dùng (user space) riêng biệt?</p>{
	~[moodle]Application Container
	=[moodle]Linux Container (LXC)
	~[moodle]Virtual Machine
	~[moodle]Docker Swarm
	####<p><strong>Giải thích</strong>: Linux Containers (LXC) cung cấp ảo hóa cấp hệ điều hành, cho phép nhiều phiên bản Linux độc lập chạy trên một kernel host.</p>
}

// question: 10 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>IaaS (Infrastructure as a Service) trong điện toán đám mây bao gồm những thành phần cơ bản nào liên quan đến máy ảo?</p>{
	~[moodle]Mạng, Ứng dụng, Cơ sở dữ liệu.
	=[moodle]Phiên bản điện toán (Computing instances), Lưu trữ khối (Block storage), và Mạng (Networking).
	~[moodle]SaaS, PaaS, và FaaS.
	~[moodle]SSH host keys, D-Bus machine id.
	####<p><strong>Giải thích</strong>: Các yếu tố phổ biến của máy ảo trong IaaS cloud bao gồm các phiên bản điện toán, lưu trữ khối và mạng.</p>
}

// question: 11 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Khi cloning một hệ thống từ template, ngoài D-Bus machine ID, thuộc tính nào khác cần được thay đổi để đảm bảo xác thực an toàn khi truy cập từ xa?</p>{
	~[moodle]Tên người dùng.
	=[moodle]SSH host keys.
	~[moodle]Địa chỉ IP.
	~[moodle]Tên miền.
	####<p><strong>Giải thích</strong>: SSH host keys là một trong những thuộc tính duy nhất của hệ thống Linux cần được thay đổi khi nhân bản.</p>
}

// question: 12 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Lệnh nào được sử dụng để tạo một cặp khóa SSH công khai và riêng tư cho việc truy cập hệ thống từ xa?</p>{
	~[moodle]dbus-uuidgen
	~[moodle]ssh-copy-id
	=[moodle]ssh-keygen
	~[moodle]cloud-init
	####<p><strong>Giải thích</strong>: Lệnh ssh-keygen được sử dụng để tạo một cặp khóa SSH công khai và riêng tư.</p>
}

// question: 13 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Trọng số (Weight) của mục tiêu 102.6 "Linux as a virtualization guest" trong kỳ thi LPIC-1 là bao nhiêu?</p>{
	=[moodle]1
	~[moodle]2
	~[moodle]3
	~[moodle]4
	####<p><strong>Giải thích</strong>: Trọng số (Weight) của mục tiêu 102.6 là 1.</p>
}

// question: 14 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Hệ thống quản lý máy ảo (hypervisor) trên phần cứng x86 cần các tiện ích mở rộng CPU (VT-x hoặc AMD-V) được bật ở đâu?</p>{
	~[moodle]Trong cấu hình kernel Linux.
	~[moodle]Trong cấu hình bộ nhớ cache.
	=[moodle]Từ menu cấu hình firmware BIOS hoặc UEFI.
	~[moodle]Trong tệp /proc/cpuinfo.
	####<p><strong>Giải thích</strong>: Để chạy khách được ảo hóa hoàn toàn, các tiện ích mở rộng CPU phải được bật từ menu cấu hình firmware BIOS hoặc UEFI.</p>
}

// question: 15 name: 102.6 Linux as a virtualization guest
::102.6 Linux as a virtualization guest::[html]<p>Nếu một máy ảo khách không biết rằng nó đang chạy trong môi trường ảo hóa, nó được gọi là loại ảo hóa nào?</p>{
	~[moodle]Paravirtualized.
	=[moodle]Fully Virtualized (hoặc FVM).
	~[moodle]Application Container.
	~[moodle]Kernel Virtualization.
	####<p><strong>Giải thích</strong>: Máy ảo khách được ảo hóa hoàn toàn (Fully Virtualized Guest) là loại mà hệ điều hành khách không cần biết rằng nó đang chạy trong môi trường ảo hóa (Ngược lại với Paravirtualized Guest).</p>
}