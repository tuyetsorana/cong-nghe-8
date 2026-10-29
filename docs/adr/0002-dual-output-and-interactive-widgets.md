# ADR 0002: Mô Hình Xuất Bản Kép (Dual-Output) và Widget Mô Phỏng Hình Chiếu Tương Tác

## Bối cảnh (Context)
Chương I (Vẽ kĩ thuật) bao gồm 5 bài học với đặc thù hình học không gian phức tạp. Học sinh lớp 8 rất khó hình dung nguyên lý từ vật thể 3D chiếu lên 3 mặt phẳng $P_1, P_2, P_3$ rồi trải phẳng ra giấy vẽ. Ngoài ra, nhu cầu sử dụng của giáo viên và học sinh rất đa dạng: có lúc cần web app tương tác với bài tập và AI, có lúc cần tài liệu in ấn giấy hoặc đọc nhanh offline không cần máy chủ Python.

## Quyết định (Decision)
1. **Xuất bản kép (Dual-Output Strategy):**
   - Nguồn dữ liệu số hóa dạng chuẩn Markdown và ảnh PNG cắt sắc nét sẽ được dùng đồng thời cho:
     - Ứng dụng tương tác **Streamlit Web App** đa tab.
     - Tệp cẩm nang duy nhất **`_CamNang_VI/Cong_Nghe_8/Chuong_01_Ve_Ky_Thuat.html`** sử dụng engine `metronic-html-publisher` (nhúng font Inter, ảnh Base64, responsive, có print stylesheet `@media print` chống lỗi âm bản).
2. **Widget tương tác "Hộp 3 Mặt phẳng chiếu" (Unfolding Projection Box):**
   - Viết bằng HTML5/SVG/CSS nhúng trực tiếp trong Streamlit qua `streamlit.components.v1.html`.
   - Cung cấp tương tác chuyển đổi giữa góc nhìn 3D không gian và góc nhìn phẳng trải 2D với các chú thích màu sắc tương ứng cho từng hình chiếu.
3. **Theo dõi tiến độ Gamified (SQLite):**
   - Tạo bảng `student_results` trong `congnghe8_progress.db` lưu Tên, Lớp, Mã bài học, Điểm số, Thời gian hoàn thành và số câu đúng để hiển thị Bảng xếp hạng thi đua (Leaderboard).

## Đánh đổi & Hệ quả (Consequences / Trade-offs)
- **Tích cực:** Tối ưu hóa tính ứng dụng thực tế: giáo viên có thể in tài liệu phát cho học sinh, học sinh có thể ôn tập trên cả điện thoại (file HTML tự chứa) lẫn phòng máy tính (Streamlit app); giải quyết triệt để rào cản tư duy không gian nhờ widget mô phỏng.
- **Tiêu cực:** Cần thêm bước build và kiểm tra đồng bộ giữa file HTML Metronic và ứng dụng Streamlit khi cập nhật nội dung bài giảng.
