# ADR 0001: Kiến Trúc Ứng Dụng Streamlit 4 Tab Sư Phạm và Phạm Vi Thử Nghiệm Chương I

## Bối cảnh (Context)
Dự án cần xây dựng một ứng dụng học tập tương tác số hóa từ cuốn sách giáo khoa Công nghệ 8 (bộ Kết nối tri thức với cuộc sống). Nguồn tài liệu là file PDF scan 110 trang hoàn toàn là ảnh đồ họa kỹ thuật, bảng biểu và sơ đồ mạch điện. Dự án cần xác định kiến trúc nền tảng và lộ trình triển khai vừa đảm bảo tính trực quan, sư phạm, vừa kiểm soát được tiến độ số hóa dữ liệu.

## Quyết định (Decision)
1. **Khung ứng dụng (App Framework):** Sử dụng Streamlit theo quy chuẩn `edu-tutor-streamlit-builder` chia thành 4 Tab sư phạm:
   - Tab 1: Lý thuyết trực quan, nhúng ảnh Base64 & video bài giảng.
   - Tab 2: Phương pháp giải 4 tầng và Widget mô phỏng tương tác 2D/SVG.
   - Tab 3: Hệ thống luyện tập 2 chế độ (Bài tập SGK + Đấu trường trắc nghiệm phân mức) kèm SQLite lưu tiến trình.
   - Tab 4: Gia sư AI Socratic ("Thầy Kĩ Thuật Pi") với cơ chế gợi mở và chế độ offline fallback.
2. **Chiến lược phân kỳ (Scoping Strategy):** Áp dụng chiến lược "Hạt nhân Chương I (Vẽ kĩ thuật)":
   - Tập trung bóc tách OCR, cắt hình minh họa và lập trình hoàn chỉnh cho 5 bài học đầu tiên (Trang 5 đến 32 của SGK).
   - Đóng gói chạy thử Prototype hoàn chỉnh để kiểm chứng độ mượt của UI/UX và logic sư phạm trước khi mở rộng sang 4 chương còn lại.
3. **Quy trình trích xuất tài liệu:** Sử dụng bộ công cụ từ skill `ocr-translation-premium-html` / `metronic-html-publisher` để bóc tách ảnh sơ đồ (`crop_tool.py`), chuẩn hóa văn bản, đồng thời sẵn sàng đóng gói cẩm nang HTML tự chứa nếu cần.

## Đánh đổi & Hệ quả (Consequences / Trade-offs)
- **Tích cực:** Học sinh có sản phẩm chạy được ngay với độ hoàn thiện cao; giảm thiểu rủi ro token và sai sót khi xử lý cùng lúc 110 trang sách scan; kiểm thử được widget 3 hình chiếu trực quan ngay ở Chương I.
- **Tiêu cực:** Các chương II &rarr; V chưa có nội dung trong bản phát hành đầu tiên; cần duy trì cấu trúc thư mục module hóa để sau này nạp thêm các chương mới mà không làm thay đổi core engine của app.
