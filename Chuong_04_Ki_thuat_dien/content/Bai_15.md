<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Cảm Biến Và Mô Đun Cảm Biến

> **Cảm biến (Sensor)** là linh kiện điện tử cảm nhận và biến đổi đại lượng vật lý/môi trường (ánh sáng, nhiệt độ, độ ẩm) thành tín hiệu điện.

1. **Các loại cảm biến thông dụng:**
   - **Cảm biến ánh sáng (Quang điện trở LDR):** Khi trời sáng &rarr; điện trở giảm; Khi trời tối &rarr; điện trở tăng vọt.
   - **Cảm biến nhiệt độ (Nhiệt điện trở NTC):** Cảm nhận nhiệt độ môi trường tăng hoặc giảm.
   - **Cảm biến độ ẩm (Độ ẩm đất/không khí):** Đầu dò hai chân cắm vào đất đo hàm lượng nước có trong đất.

2. **Mô đun cảm biến (Sensor Module):**
   - Là một mạch điện hoàn chỉnh tích hợp: Cảm biến + Mạch khuếch đại so sánh điện áp + Rơ-le (Relay) đóng cắt tải công suất lớn.
   - Cổng vào: Nối nguồn cấp ($5\text{ V}$ hoặc $12\text{ V}$).
   - Cổng ra: Tiếp điểm rơ-le (NO - Thường mở, NC - Thường đóng, COM - Chân chung) để điều khiển bật/tắt đèn, quạt, bơm.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: Nhận Diện Các Khối Trên Mô Đun Cảm Biến Thực Tế
- **Khối 1 (Đầu vào tín hiệu):** Hai chân cắm linh kiện cảm biến (quang trở hoặc que đo ẩm).
- **Khối 2 (Chiết áp tinh chỉnh):** Biến trở xoay hình vuông có ốc vặn nhỏ màu xanh để chỉnh ngưỡng nhạy sáng hoặc độ ẩm mong muốn.
- **Khối 3 (IC so sánh LM393):** Não bộ so sánh tín hiệu điện áp.
- **Khối 4 (Rơ-le đầu ra):** Khối hộp màu xanh lam để đóng mở tải điện áp $220\text{ V}$.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 15

Hình ảnh các linh kiện cảm biến phổ biến:

![Hình 15.2 Các loại cảm biến](../assets/images/H15_2_cac_loai_cam_bien.png)

> **Khám phá:** Tại sao ở các siêu thị cửa kính lại tự động mở ra khi có người bước đến gần?
