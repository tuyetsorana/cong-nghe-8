# GLOSSARY

### Bản vẽ kĩ thuật (Technical Drawing)
Tài liệu trình bày các thông tin kỹ thuật của sản phẩm dưới dạng hình vẽ, ký hiệu và kích thước theo các quy tắc, tiêu chuẩn thống nhất (TCVN / ISO), dùng trong chế tạo, lắp ráp, thi công và kiểm tra sản phẩm.

### Hình chiếu vuông góc (Orthogonal Projection)
Hình biểu diễn nhận được trên mặt phẳng chiếu khi các tia chiếu vuông góc với mặt phẳng chiếu. Trong chương trình Công nghệ 8, gồm 3 hình chiếu chính:
- **Hình chiếu đứng (Front View):** Hướng chiếu từ trước tới, đặt trên mặt phẳng hình chiếu đứng.
- **Hình chiếu bằng (Top View):** Hướng chiếu từ trên xuống, đặt phía dưới hình chiếu đứng.
- **Hình chiếu cạnh (Left Side View):** Hướng chiếu từ trái sang, đặt bên phải hình chiếu đứng.

### Mặt bằng (Floor Plan)
Hình cắt bằng của ngôi nhà được tạo bởi mặt phẳng cắt nằm ngang tưởng tượng (cách sàn khoảng 1m đến 1.5m), thể hiện vị trí, kích thước tường, vách ngăn, cửa đi, cửa sổ và cách bố trí các phòng chức năng.

### Hộp mặt phẳng chiếu (Projection Box / Glass Box)
Mô hình trực quan gồm 3 mặt phẳng vuông góc với nhau trong không gian:
- **Mặt phẳng hình chiếu đứng ($P_1$):** Mặt phẳng chính diện.
- **Mặt phẳng hình chiếu bằng ($P_2$):** Mặt phẳng nằm ngang dưới đáy.
- **Mặt phẳng hình chiếu cạnh ($P_3$):** Mặt phẳng thẳng đứng bên phải.
Sau khi chiếu, $P_2$ được xoay xuống dưới $90^\circ$ và $P_3$ được xoay sang phải $90^\circ$ để trải phẳng cùng mặt phẳng $P_1$.

### Bản vẽ chi tiết (Detail Drawing)
Bản vẽ chứa đầy đủ các hình biểu diễn, các kích thước cần thiết, yêu cầu kỹ thuật và khung tên của một chi tiết đơn lẻ, phục vụ cho việc chế tạo và kiểm tra.

### Khung tên (Title Block)
Ô quy định đặt ở góc dưới cùng bên phải của bản vẽ kỹ thuật, ghi rõ tên chi tiết/sản phẩm, vật liệu, tỉ lệ, ký hiệu bản vẽ, tên người vẽ và cơ quan/trường học.

### Mô hình Xuất bản Kép (Dual-Output Architecture)
Kiến trúc tổ chức dữ liệu cho phép một nguồn nội dung số hóa (Markdown + tài nguyên ảnh) xuất bản đồng thời ra 2 hình thức:
1. Ứng dụng Web tương tác (Streamlit Web App với tính năng làm bài, timer, trợ lý AI).
2. Cẩm nang HTML tự chứa duy nhất (Self-contained HTML dựa trên thiết kế Metronic v9, nhúng Base64, tối ưu in ấn và đọc ngoại tuyến).

### Bản vẽ nhà (Architectural Drawing / Floor Plan)
Bản vẽ thể hiện hình dáng, kích thước và kết cấu của ngôi nhà, trong đó **Mặt bằng** là hình cắt bằng quan trọng nhất thể hiện vị trí, kích thước các phòng, cửa đi, cửa sổ và cầu thang.

### Mô đun cảm biến (Sensor Module)
Mạch điện tử tích hợp cảm biến (quang trở, nhiệt độ, độ ẩm...), mạch xử lý tín hiệu và cơ cấu chấp hành (relay/transistor) nhằm tự động đóng cắt nguồn điện cho thiết bị phụ tải theo tín hiệu môi trường.

### Gia sư Socratic (Socratic AI Tutor)
Phương pháp sư phạm định hướng người học tự khám phá kiến thức thông qua chuỗi câu hỏi gợi mở, phân tích bản chất hiện tượng kỹ thuật và liên hệ thực tiễn đời sống thay vì cung cấp lời giải trực tiếp.
