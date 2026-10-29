<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Mạch Điện Điều Khiển Dùng Mô Đun Cảm Biến

1. **Sơ đồ khối nguyên lý hoạt động:**
   $$\text{Môi trường biến đổi} \longrightarrow \text{Cảm biến} \longrightarrow \text{Mạch khuếch đại} \longrightarrow \text{Rơ-le (Relay)} \longrightarrow \text{Bật/Tắt Tải}$$
2. **Ứng dụng tiêu biểu trong đời sống thông minh (Smart Home):**
   - **Mô đun cảm biến ánh sáng:** Tự động bật đèn đường khi trời tối ($6\text{h tối}$) và tắt đèn khi trời sáng ($6\text{h sáng}$).
   - **Mô đun cảm biến nhiệt độ:** Tự động bật quạt thông gió khi nhiệt độ chuồng trại/phòng máy $> 35^\circ\text{C}$.
   - **Mô đun cảm biến độ ẩm đất:** Tự động kích hoạt máy bơm tưới hoa khi đất bị khô và tự ngắt bơm khi đất đã đủ ẩm.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 5 Bước Chuẩn SGK Lắp Ráp Mạch Điều Khiển
1. **Bước 1 - Tìm hiểu mô đun:** Xác định cực cấp nguồn ($VCC, GND$) và tiếp điểm đầu ra ($COM, NO$).
2. **Bước 2 - Lập sơ đồ nối dây:** Vẽ sơ đồ kết nối nguồn pin, mô đun cảm biến và bóng đèn/máy bơm.
3. **Bước 3 - Chuẩn bị dụng cụ:** Kìm tuốt dây, tua vít nhỏ, dây dẫn, băng dính cách điện.
4. **Bước 4 - Tiến hành đấu nối:** Đấu nối nguồn trước, đấu nối tải vào rơ-le theo đúng cực tính.
5. **Bước 5 - Vận hành và hiệu chỉnh:** Cấp nguồn, dùng tay che cảm biến (mô phỏng trời tối) và vặn chiết áp để đèn bật sáng chính xác.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 16

Sơ đồ khối điều khiển tự động:

![Hình 16.3 Sơ đồ khối](../assets/images/H16_3_so_do_khoi_mach_cam_bien.png)

> **Luyện tập:** Hãy trình bày cách đấu nối mô đun cảm biến độ ẩm để điều khiển một máy bơm mini $12\text{ V}$.
