# Ứng Dụng Tự Học Tương Tác Công Nghệ 8 (Kết Nối Tri Thức Với Cuộc Sống)

Web App giáo dục tương tác hiện đại dành cho học sinh lớp 8 học môn **Công nghệ 8** (Bộ sách *Kết nối tri thức với cuộc sống* - NXB Giáo dục Việt Nam), tích hợp **Gia sư Socratic AI "Kỹ Sư Trí Đức"**, bộ học liệu số hóa 300 DPI, đấu trường kỹ thuật gamified và hướng dẫn dự án STEM thực hành. Ứng dụng sẵn sàng triển khai toàn cầu miễn phí trên **Streamlit Community Cloud**.

---

## 🌟 Tính Năng Sư Phạm Cốt Lõi (4 Tab Chuẩn Mực)

1. **💡 Tab 1: Bài Học & Lý Thuyết Trực Quan (3 Thẻ)**
   - **Thẻ 1 - Ghi nhớ nhanh:** Thiết kế nền trắng tinh chống mờ chữ, ép font-weight 500, highlight ĐỎ TƯƠI (`#dc2626`) cho từ khóa và công thức kỹ thuật ($i = \frac{n_1}{n_2} = \frac{D_2}{D_1}$).
   - **Safety Alert Box:** Khung cảnh báo nổi bật về an toàn lao động cơ khí (khi cưa/dũa) và an toàn điện (cứu người điện giật, aptomat chống giật).
   - **Video bài giảng tuyển chọn:** Nhúng trực tiếp video bài giảng từ giáo viên uy tín (VietJack, HOCMAI, OLM) trong `st.expander`.
   - **Thẻ 2 - Đọc bản vẽ & Thao tác kỹ thuật:** Trình bày chi tiết bản vẽ mẫu và thao tác từng bước; tích hợp widget mô phỏng tương tác 3D/SVG "Hộp 3 mặt phẳng chiếu vuông góc".
   - **Thẻ 3 - Đọc thêm SGK gốc:** Toàn văn nội dung sách giáo khoa gốc kèm hoạt động Khám phá, Thảo luận, Luyện tập và Kết nối nghề nghiệp.

2. **🔍 Tab 2: Quy Trình Kỹ Thuật & Đọc Bản Vẽ Chi Tiết**
   - **Dạng 1 (Đọc bản vẽ kỹ thuật - 5 bước chuẩn SGK):** Khung tên &rarr; Hình biểu diễn &rarr; Kích thước &rarr; Yêu cầu kĩ thuật &rarr; Tổng hợp hình dung 3D.
   - **Dạng 2 (Quy trình thao tác & lắp ráp an toàn):** Chuẩn bị dụng cụ &rarr; Thao tác chuẩn (tư thế, góc cưa/dũa) &rarr; Đánh giá sản phẩm &rarr; Tuân thủ an toàn.
   - **Dạng 3 (Bài toán tính toán kỹ thuật):** Tính tỉ số truyền $i$, số răng $Z$, đường kính $D$, tốc độ quay $n$ với lời giải 4 tầng.

3. **🎯 Tab 3: Đấu Trường Kỹ Thuật & Tự Chấm Điểm**
   - **⚡ Đấu trường trắc nghiệm tính giờ:** Ngân hàng câu hỏi 3 cấp độ (Dễ • Vừa • Thử thách), đồng hồ bấm giờ (Timer), tự động chấm thang 10, hiệu ứng pháo hoa `st.balloons()` khi điểm $\ge 7/10$.
   - **📚 Lời giải chi tiết 4 bước toàn bộ bài tập SGK:** Phương pháp &rarr; Bước 1 &rarr; Bước 2 &rarr; Kết luận &rarr; Bảo bối then chốt kèm ô nháp tương tác.
   - **Cơ sở dữ liệu SQLite đa luồng (`database.py`):** Theo dõi chuỗi ngày học liên tục (Streak 🔥) và vinh danh Top 5 học sinh trên Bảng Vàng.

4. **🤖 Tab 4: Kỹ Sư AI Socratic — "Kỹ Sư Trí Đức"**
   - **Persona:** Kỹ sư Bách Khoa am hiểu máy móc đời sống, thân thiện, tôn vinh an toàn kỹ thuật.
   - **Phương pháp Socratic:** Không đưa đáp án ngay mà đặt câu hỏi gợi mở để học sinh tự suy nghĩ và giải quyết vấn đề.
   - **Hướng dẫn 2 Dự án STEM lớn:**
     - *Dự án 1 (Bài 10):* Gia công chi tiết kim loại bằng dụng cụ cầm tay (vạch dấu, cưa, dũa góc 90°).
     - *Dự án 2 (Bài 20):* Thiết kế hệ thống tưới cây tự động sử dụng mô đun cảm biến độ ẩm đất, rơ-le và máy bơm mini.
   - **Module Kết nối nghề nghiệp STEM:** Định hướng kỹ sư cơ khí, tự động hóa, kỹ sư IoT, thợ điện tử.
   - **Chế độ Kép:** Google Gemini 2.5 Flash API trực tuyến + Bộ Offline Fallback thông minh phản hồi tức thì khi chưa có API Key.

---

## 📁 Cấu Trúc Toàn Diện Dự Án

```
CONG NGHE LOP 8/
├── .streamlit/
│   ├── config.toml                     # Theme, headless, UTF-8 No BOM chống lỗi Linux
│   └── secrets.toml.example            # Hướng dẫn nạp GEMINI_API_KEY
├── assets/
│   ├── images/                         # Toàn bộ hình ảnh bản vẽ kỹ thuật 300 DPI
│   └── interactive_projection_box.html # Widget mô phỏng tương tác 3 hình chiếu
├── Chuong_01_Ve_ki_thuat/content/      # Bai_01.md -> Bai_05.md, On_Tap_Chuong_01.md
├── Chuong_02_Co_khi/content/           # Bai_06.md -> Bai_10.md, On_Tap_Chuong_02.md
├── Chuong_03_An_toan_dien/content/     # Bai_11.md -> Bai_13.md, On_Tap_Chuong_03.md
├── Chuong_04_Ki_thuat_dien/content/    # Bai_14.md -> Bai_17.md, On_Tap_Chuong_04.md
├── Chuong_05_Thiet_ke_ki_thuat/content/# Bai_18.md -> Bai_20.md, On_Tap_Chuong_05.md
├── data/
│   ├── lesson_videos.json              # 25 video bài giảng tuyển chọn từ giáo viên uy tín
│   ├── sgk_solutions.json              # Lời giải chi tiết 4 bước cho 100% bài tập SGK
│   ├── extra_exercises.json            # Ngân hàng trắc nghiệm đa tầng phân hạng
│   └── technical_procedures.json       # 3 Dạng quy trình kỹ thuật & đọc bản vẽ chuẩn SGK
├── app.py                              # Ứng dụng Streamlit chính (4 Tabs sư phạm)
├── database.py                         # SQLite đa luồng quản lý tiến độ, Streak & Bảng Vàng
├── ai_tutor.py                         # Kỹ Sư AI Socratic "Kỹ Sư Trí Đức" (Gemini + Offline)
├── lesson_parser.py                    # Bộ bóc tách tự động 3 phân vùng Markdown & Base64
├── requirements.txt                    # streamlit, google-genai, pillow, pypdfium2
├── .gitignore                          # Loại trừ file database, secrets, temp_pages
└── README.md
```

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Ứng Dụng

### 1. Chạy trên máy tính cá nhân (Localhost)
```bash
# 1. Cài đặt các thư viện yêu cầu
pip install -r requirements.txt

# 2. Khởi chạy Web App Streamlit
streamlit run app.py
```
Trình duyệt sẽ tự động mở tại địa chỉ `http://localhost:8501`.

---

## ☁️ Hướng Dẫn Triển Khai Lên Streamlit Community Cloud (Miễn Phí)

1. Đẩy toàn bộ mã nguồn lên kho lưu trữ **GitHub** (chế độ Public).
2. Truy cập **[share.streamlit.io](https://share.streamlit.io/)** & đăng nhập bằng GitHub.
3. Bấm **"Create app"** &rarr; Chọn **"I already have an app"**.
4. Khai báo các thông tin:
   - **Repository:** `<tên-tài-khoản-github>/<tên-repo>`
   - **Branch:** `main` (hoặc `master`)
   - **Main file path:** `app.py`
5. *(Cấu hình AI Tutor)*: Vào mục **Advanced settings** &rarr; Tab **Secrets**, dán API Key:
   ```toml
   GEMINI_API_KEY = "AIzaSy..."
   ```
6. Bấm **Deploy!** — Ứng dụng sẽ hoạt động online 24/7 và sẵn sàng phục vụ học sinh trên toàn cầu.
