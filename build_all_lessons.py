# -*- coding: utf-8 -*-
"""
Script tạo lập nội dung chuẩn mực 3 phân vùng cho 20 bài học và 5 bài ôn tập môn Công nghệ 8.
Mỗi bài gồm:
<!-- SECTION: QUICK_NOTES -->
<!-- SECTION: STEP_EXAMPLES -->
<!-- SECTION: SGK_CONTENT -->
"""
import os

LESSONS_CONTENT = {
    # ------------------ CHƯƠNG I: VẼ KĨ THUẬT ------------------
    "Chuong_01_Ve_ki_thuat/content/Bai_01.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Tiêu Chuẩn Trình Bày Bản Vẽ Kĩ Thuật

> **Bản vẽ kĩ thuật** là ngôn ngữ chung kỳ diệu của mọi kỹ sư trên toàn cầu, được lập theo quy chuẩn nghiêm ngặt của **Tiêu chuẩn Việt Nam (TCVN)** hoặc tiêu chuẩn quốc tế **ISO**.

1. **Khổ giấy chính (TCVN 7285:2003):** Gồm 5 khổ giấy $A0, A1, A2, A3, A4$.
   - Mỗi khổ giấy tiếp theo được tạo ra bằng cách chia đôi khổ giấy trước theo chiều dài.
   - Kích thước chuẩn khổ **A4**: <span style="color:#dc2626; font-weight:700;">$297 \\times 210\\text{ mm}$</span>. Khổ lớn nhất **A0**: <span style="color:#dc2626; font-weight:700;">$1189 \\times 841\\text{ mm}$</span> ($1\\text{ A0} = 16\\text{ A4}$).
   - **Khung bản vẽ:** Kẻ nét liền đậm, mép bên trái chừa <span style="color:#dc2626; font-weight:700;">$20\\text{ mm}$</span> (để đóng gáy tập), 3 mép còn lại chừa <span style="color:#dc2626; font-weight:700;">$10\\text{ mm}$</span> (khổ A4 có thể chừa $5\\text{ mm}$).
   - **Khung tên:** Đặt ở góc dưới cùng bên phải của bản vẽ.

2. **Tỉ lệ (TCVN 7286:2003):**
   $$\\text{Tỉ lệ} = \\frac{\\text{Kích thước trên bản vẽ}}{\\text{Kích thước thực của vật thể}}$$
   - **Tỉ lệ nguyên hình:** $1:1$
   - **Tỉ lệ thu nhỏ:** $1:2, 1:5, 1:10, 1:20\\dots$
   - **Tỉ lệ phóng to:** $2:1, 5:1, 10:1\\dots$
   - <span style="color:#dc2626; font-weight:700;">LƯU Ý VÀNG:</span> Dù vẽ thu nhỏ hay phóng to, **con số kích thước ghi trên bản vẽ LUÔN LUÔN là kích thước THỰC** của vật thể và không ghi kèm đơn vị "mm"!

3. **Nét vẽ (TCVN 8-24:2002):**
   - **Nét liền đậm (━━━):** Vẽ đường bao thấy, cạnh thấy.
   - **Nét liền mảnh (───):** Đường gióng, đường ghi kích thước, đường gạch mặt cắt.
   - **Nét đứt mảnh (┈┈┈):** Đường bao khuất, cạnh khuất bên trong.
   - **Nét gạch dài - chấm - mảnh (━ ⬝ ━ ⬝ ━):** Đường tâm, đường trục đối xứng của lỗ tròn, khối trụ.
   - Chiều rộng nét đậm $s = 0.5\\text{ mm}$, nét mảnh $s_{mảnh} \\approx 0.5s = 0.25\\text{ mm}$.

4. **Ghi kích thước (TCVN 5705:1993):**
   - Đơn vị đo độ dài mặc định là **milimét (mm)** &rarr; không ghi chữ "mm".
   - Ký hiệu $\\varnothing$ đặt trước đường kính hình tròn (ví dụ: $\\varnothing 30$).
   - Ký hiệu $R$ đặt trước bán kính cung tròn (ví dụ: $R15$).

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 5 Bước Ghi Kích Thước Bản Vẽ Chuẩn Xác

- **Bước 1 (Xác định kích thước cần ghi):** Phân loại kích thước chung (Dài $\\times$ Rộng $\\times$ Cao) và kích thước từng phần tử (khoảng cách tâm lỗ, rãnh, vát mép).
- **Bước 2 (Kẻ đường gióng kích thước):** Dùng thước kẻ nét liền mảnh, kẻ vuông góc với đoạn thẳng cần đo, vượt quá đầu mũi tên $2 \\sim 4\\text{ mm}$.
- **Bước 3 (Kẻ đường kích thước):** Kẻ song song với đoạn cần đo, hai đầu có mũi tên nhọn chạm sát vào đường gióng.
- **Bước 4 (Điền con số kích thước):** Ghi con số kích thước thực ở phía trên đường kích thước nằm ngang hoặc bên trái đường kích thước thẳng đứng, chữ số hướng lên trên.
- **Bước 5 (Kiểm tra quy chuẩn):** Đảm bảo có ký hiệu $\\varnothing$ cho đường kính tròn, $R$ cho cung lượn, và tuyệt đối không ghi đơn vị mm.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 1

#### Khởi động
Quan sát hai hình biểu diễn cùng một chi tiết máy: một hình vẽ theo đúng tiêu chuẩn kỹ thuật TCVN, một hình vẽ tùy ý. Bản vẽ không theo tiêu chuẩn sẽ gây sai lệch kích thước, khiến thợ tiện, thợ nguội không thể gia công lắp ráp chính xác.

![Hình 1.1 Hình biểu diễn](../assets/images/hinh_1_1_hinh_bieu_dien.png)

#### I. Khổ Giấy
Tiêu chuẩn TCVN 7285:2003 quy định các khổ giấy chính chế tạo từ tờ A0:
- A0 ($1189 \\times 841\\text{ mm}$)
- A1 ($841 \\times 594\\text{ mm}$)
- A2 ($594 \\times 420\\text{ mm}$)
- A3 ($420 \\times 297\\text{ mm}$)
- A4 ($297 \\times 210\\text{ mm}$)

![Hình 1.2 Các khổ giấy chính](../assets/images/hinh_1_2_kho_giay.png)

#### II. Khung Bản Vẽ & Khung Tên
- Khung bản vẽ được kẻ bằng nét liền đậm cách mép giấy: cạnh lề trái chừa 20 mm để đóng gáy tập, 3 cạnh còn lại chừa 10 mm.
- Khung tên luôn được đặt ở góc dưới cùng bên phải của bản vẽ.

![Hình 1.3 Khung tên bản vẽ](../assets/images/hinh_1_3_khung_ten.png)

#### III. Nét Vẽ & Ghi Kích Thước
Mỗi nét vẽ truyền tải một thông điệp kỹ thuật riêng biệt:

![Hình 1.4 Các loại nét vẽ](../assets/images/hinh_1_4_net_ve.png)

Quy tắc ghi kích thước chi tiết:

![Hình 1.5 Quy tắc ghi kích thước](../assets/images/hinh_1_5_ghi_kich_thuoc.png)

> **Luyện tập:** Hãy vẽ lại khung bản vẽ và khung tên trên tờ giấy vẽ A4 theo đúng tỉ lệ và kích thước tiêu chuẩn TCVN.
""",

    "Chuong_01_Ve_ki_thuat/content/Bai_02.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Hình Chiếu Vuông Góc

> **Hình chiếu vuông góc** là hình nhận được trên mặt phẳng chiếu khi các tia chiếu đi vuông góc với mặt phẳng chiếu đó.

1. **Ba mặt phẳng hình chiếu trong không gian:**
   - Mặt phẳng hình chiếu đứng: <span style="color:#dc2626; font-weight:700;">$P_1$ (chính diện)</span>. Hướng chiếu từ **TRƯỚC &rarr; SAU**.
   - Mặt phẳng hình chiếu bằng: <span style="color:#dc2626; font-weight:700;">$P_2$ (nằm ngang)</span>. Hướng chiếu từ **TRÊN &rarr; XUỐNG**.
   - Mặt phẳng hình chiếu cạnh: <span style="color:#dc2626; font-weight:700;">$P_3$ (bên phải)</span>. Hướng chiếu từ **TRÁI &rarr; SANG PHẢI**.

2. **Quy tắc mở hộp và vị trí 3 hình chiếu trên bản vẽ (BẮT BUỘC):**
   - Giữ nguyên mặt phẳng hình chiếu đứng $P_1$.
   - Mở phẳng $P_2$ xoay xuống dưới $90^\\circ$ &rarr; <span style="color:#dc2626; font-weight:700;">Hình chiếu BẰNG luôn nằm NGAY DƯỚI hình chiếu đứng</span>.
   - Mở phẳng $P_3$ xoay sang phải $90^\\circ$ &rarr; <span style="color:#dc2626; font-weight:700;">Hình chiếu CẠNH luôn nằm NGAY BÊN PHẢI hình chiếu đứng</span>.

3. **Hình chiếu của các khối hình học cơ bản:**
   - **Khối đa diện (Hình hộp chữ nhật):** Cả 3 hình chiếu đều là hình chữ nhật phản ánh các kích thước Dài, Rộng, Cao.
   - **Khối tròn xoay:**
     - *Hình trụ:* Chiếu đứng và cạnh là hình chữ nhật, chiếu bằng là hình tròn.
     - *Hình nón:* Chiếu đứng và cạnh là tam giác cân, chiếu bằng là hình tròn (có chấm tâm).
     - *Hình cầu:* Cả 3 hình chiếu đều là hình tròn cùng đường kính $d$.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 4 Bước Vẽ 3 Hình Chiếu Vuông Góc

- **Bước 1 (Phân tích vật thể):** Quan sát hình không gian 3D, chia nhỏ thành các khối hình học cơ bản (hộp, trụ, rãnh khoét).
- **Bước 2 (Vẽ hình chiếu đứng):** Chọn hướng nhìn chính diện bộc lộ nhiều đặc điểm nhất. Vẽ đường bao thấy bằng nét liền đậm, đường bao khuất bằng nét đứt mảnh.
- **Bước 3 (Dóng vẽ hình chiếu bằng):** Từ hình chiếu đứng, kẻ các đường gióng thẳng đứng xuống dưới. Vẽ hình chiếu bằng thể hiện chiều dài và chiều rộng.
- **Bước 4 (Dóng vẽ hình chiếu cạnh):** Từ hình chiếu đứng dóng ngang sang phải, kết hợp dóng góc $45^\\circ$ từ hình chiếu bằng để vẽ chính xác chiều cao và chiều rộng của hình chiếu cạnh.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 2

#### I. Phương Pháp Chiếu Góc Thứ Nhất
Trong phương pháp chiếu góc thứ nhất, vật thể được đặt trong góc tạo bởi 3 mặt phẳng vuông góc với nhau từng đôi một:

![Hình 2.3 Các mặt phẳng chiếu](../assets/images/hinh_2_3_mat_phang_chieu.png)

- Hình chiếu đứng có hướng chiếu từ trước tới.
- Hình chiếu bằng có hướng chiếu từ trên xuống.
- Hình chiếu cạnh có hướng chiếu từ trái sang.

![Hình 2.4 Hướng chiếu vật thể](../assets/images/hinh_2_4_chieu_vat_the.png)

#### II. Vị Trí Các Hình Chiếu Sau Khi Mở Phẳng
Sau khi xoay mặt phẳng $P_2$ xuống dưới và $P_3$ sang phải:
- Hình chiếu bằng ở dưới hình chiếu đứng.
- Hình chiếu cạnh ở bên phải hình chiếu đứng.

![Hình 2.5 Vị trí các hình chiếu](../assets/images/hinh_2_5_vi_tri_hinh_chieu.png)

> **Thực hành:** Quan sát vật thể mẫu và đối chiếu với 3 hình chiếu tương ứng để phát hiện đường bao thấy (nét liền đậm) và đường bao khuất (nét đứt mảnh).
""",

    "Chuong_01_Ve_ki_thuat/content/Bai_03.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Bản Vẽ Chi Tiết

> **Bản vẽ chi tiết** là tài liệu kỹ thuật chứa đầy đủ hình biểu diễn, kích thước và yêu cầu kỹ thuật cần thiết để chế tạo và kiểm tra một chi tiết máy riêng lẻ.

1. **Bốn nội dung chính của bản vẽ chi tiết:**
   - **Khung tên:** Tên gọi chi tiết, vật liệu chế tạo, tỉ lệ bản vẽ, nơi thiết kế/chế tạo.
   - **Hình biểu diễn:** Hình chiếu đứng, hình chiếu cạnh hoặc hình cắt diễn tả hình dạng kết cấu bên trong và bên ngoài.
   - **Kích thước:** Kích thước chung và kích thước các phần tử (đường kính lỗ, rãnh then, bề dày).
   - **Yêu cầu kĩ thuật:** Chỉ dẫn về gia công cơ khí (làm tù cạnh, mài bóng) và xử lý bề mặt (mạ kẽm, nhiệt luyện).

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 5 Bước Chuẩn Đọc Bản Vẽ Chi Tiết (SGK)

1. **Bước 1 - Đọc Khung tên:** Tên gọi chi tiết? Làm bằng vật liệu gì? Tỉ lệ vẽ bao nhiêu?
2. **Bước 2 - Phân tích Hình biểu diễn:** Gồm những hình chiếu nào? Có hình cắt không?
3. **Bước 3 - Đọc Kích thước:** Kích thước chung (Dài $\\times$ Rộng $\\times$ Cao)? Kích thước các phần tử cấu tạo?
4. **Bước 4 - Đọc Yêu cầu kĩ thuật:** Cần gia công cơ khí ra sao? Có yêu cầu xử lý nhiệt luyện chống mài mòn không?
5. **Bước 5 - Tổng hợp:** Tưởng tượng hoàn chỉnh hình dáng 3D của chi tiết và vị trí sử dụng trong máy móc.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 3

Bản vẽ chi tiết ống lót diễn đạt cấu tạo hình trụ có lỗ bậc thông suốt ở giữa:

![Hình 3.1 Bản vẽ chi tiết ống lót](../assets/images/hinh_3_1_ban_ve_ong_lot.png)

> **Luyện tập:** Thực hành đọc bản vẽ chi tiết Côn có ren theo đúng trình tự 5 bước kỹ thuật.
""",

    "Chuong_01_Ve_ki_thuat/content/Bai_04.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Bản Vẽ Lắp

> **Bản vẽ lắp** diễn đạt hình dạng, kết cấu và vị trí tương quan của một nhóm chi tiết được lắp ghép với nhau tạo thành một bộ phận máy hoặc một cỗ máy hoàn chỉnh.

1. **Nội dung bản vẽ lắp:** Gồm Khung tên, Hình biểu diễn, Kích thước chung/lắp ghép và <span style="color:#dc2626; font-weight:700;">BẢNG KÊ</span>.
2. **Điểm khác biệt then chốt giữa Bản vẽ lắp và Bản vẽ chi tiết:**
   - Bản vẽ lắp **CÓ BẢNG KÊ** (liệt kê tên gọi, số lượng, vật liệu của từng chi tiết con).
   - Bản vẽ lắp **KHÔNG CÓ YÊU CẦU KĨ THUẬT GIA CÔNG** chi tiết lẻ mà chỉ có yêu cầu lắp ráp.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 5 Bước Đọc Bản Vẽ Lắp Chuẩn Mực

1. **Bước 1 - Khung tên:** Tên gọi sản phẩm, tỉ lệ bản vẽ.
2. **Bước 2 - Bảng kê:** Đọc danh sách các chi tiết, số lượng mỗi loại và vật liệu tương ứng.
3. **Bước 3 - Hình biểu diễn:** Nhận diện vị trí từng chi tiết trên hình chiếu và hình cắt.
4. **Bước 4 - Kích thước:** Đọc kích thước chung và kích thước lắp ghép giữa các chi tiết.
5. **Bước 5 - Tổng hợp & Quy trình tháo lắp:** Hình dung nguyên lý vận hành, vạch ra trình tự tháo trước - lắp sau hợp lý.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 4

Bản vẽ lắp bộ ròng rọc bao gồm giá đỡ, bánh ròng rọc, trục và đai ốc:

![Hình 4.1 Bản vẽ lắp bộ ròng rọc](../assets/images/hinh_4_1_ban_ve_lap_rong_roc.png)

> **Khám phá:** Từ bản vẽ lắp, hãy chỉ ra chi tiết nào quay quanh trục và chi tiết nào làm nhiệm vụ giữ cố định.
""",

    "Chuong_01_Ve_ki_thuat/content/Bai_05.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Bản Vẽ Nhà

> **Bản vẽ nhà** là bản vẽ thể hiện hình dáng, kích thước và kết cấu của một ngôi nhà dùng trong thiết kế và thi công xây dựng.

1. **Ba hình biểu diễn cơ bản của bản vẽ nhà:**
   - **Mặt bằng (Hình quan trọng nhất):** Hình cắt nằm ngang cắt qua tầm cửa sổ. Thể hiện cách phân chia các phòng khách, phòng ngủ, vị trí cửa đi và cửa sổ.
   - **Mặt đứng:** Hình chiếu vuông góc các mặt ngoài ngôi nhà, thể hiện vẻ đẹp kiến trúc và chiều cao các tầng.
   - **Mặt cắt:** Hình cắt tạo bởi mặt phẳng thẳng đứng đi qua cửa đi và cầu thang, diễn tả kết cấu sàn, mái và móng nhà.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 4 Bước Đọc Bản Vẽ Nhà

1. **Bước 1 - Khung tên:** Tên ngôi nhà (Nhà ở 1 tầng, nhà phố), tỉ lệ bản vẽ.
2. **Bước 2 - Mặt bằng:** Đếm số lượng phòng, diện tích từng phòng, lối đi và hướng mở cửa sổ/cửa chính.
3. **Bước 3 - Mặt đứng & Mặt cắt:** Đọc chiều cao tổng thể của ngôi nhà, chiều cao sàn và chiều dày tường.
4. **Bước 4 - Tổng hợp:** Hình dung phối cảnh không gian ngôi nhà hoàn chỉnh ngoài thực tế.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 5

Hình ảnh minh họa mặt bằng và mặt đứng ngôi nhà một tầng:

![Hình 5.1 Bản vẽ nhà một tầng](../assets/images/hinh_5_1_ban_ve_nha.png)

> **Vận dụng:** Dựa vào các ký hiệu quy ước, hãy đọc số lượng cửa sổ và cửa ra vào trên mặt bằng phòng ở của em.
""",

    "Chuong_01_Ve_ki_thuat/content/On_Tap_Chuong_01.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Tổng Kết Ôn Tập Chương I: Vẽ Kĩ Thuật

- **Bản vẽ kỹ thuật:** Lập theo tiêu chuẩn TCVN. Khổ A4 ($297 \\times 210\\text{ mm}$). Lề trái $20\\text{ mm}$, lề khác $10\\text{ mm}$.
- **Quy tắc 3 hình chiếu:** Đứng ($P_1$) - Bằng ($P_2$, nằm dưới Đứng) - Cạnh ($P_3$, bên phải Đứng).
- **Phân loại bản vẽ:** Bản vẽ chi tiết (có Yêu cầu KT, không có Bảng kê) vs Bản vẽ lắp (có Bảng kê, không có Yêu cầu KT gia công chi tiết).
- **Bản vẽ nhà:** Mặt bằng là hình biểu diễn quan trọng nhất.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Bảng Tra Cứu Nhanh Ký Hiệu & Tiêu Chuẩn Chương I
| Hạng mục | Quy chuẩn TCVN | Lưu ý then chốt |
|---|---|---|
| Khổ giấy A4 | $297 \\times 210\\text{ mm}$ | Gấp đôi được A3, 16 tờ A4 = 1 tờ A0 |
| Nét đậm | $s = 0.5\\text{ mm}$ | Cạnh thấy, bao thấy |
| Nét đứt | $s \\approx 0.25\\text{ mm}$ | Cạnh khuất, bao khuất |
| Ghi kích thước | Không ghi đơn vị "mm" | Số ghi luôn là kích thước thật |

<!-- SECTION: SGK_CONTENT -->
### 📖 Câu Hỏi Tổng Kết Ôn Tập Chương I
1. Nêu vị trí tương đối của hình chiếu bằng và hình chiếu cạnh so với hình chiếu đứng?
2. Trình bày sự giống và khác nhau giữa bản vẽ chi tiết và bản vẽ lắp?
""",

    # ------------------ CHƯƠNG II: CƠ KHÍ ------------------
    "Chuong_02_Co_khi/content/Bai_06.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Vật Liệu Cơ Khí

> Vật liệu cơ khí là nền tảng để chế tạo mọi chi tiết máy móc, thiết bị và công cụ trong sản xuất đời sống.

1. **Vật liệu kim loại:**
   - **Kim loại đen:** Thành phần chủ yếu là Sắt ($Fe$) và Carbon ($C$).
     - *Gang:* Tỉ lệ $C > 2.14\\%$. Cứng, giòn, chịu nén tốt &rarr; Đúc bệ máy, vỏ động cơ, nắp cống.
     - *Thép:* Tỉ lệ $C \\le 2.14\\%$. Dẻo, dễ uốn, độ bền cao &rarr; Chế tạo xích xe, ray tàu hỏa, khung xe máy, dao kéo.
   - **Kim loại màu:** Đồng, Nhôm và hợp kim của chúng.
     - Dẫn điện, dẫn nhiệt cực tốt, ít bị gỉ sét ăn mòn.
     - *Đồng & hợp kim đồng:* Lõi dây dẫn điện, cánh bơm, ổ trượt.
     - *Nhôm & hợp kim nhôm:* Nhẹ, bền &rarr; Khung vỏ máy bay, nồi xoong, thanh tản nhiệt vi tính.

2. **Vật liệu phi kim loại:**
   - **Chất dẻo nhiệt:** Nóng chảy ở nhiệt độ cao, có khả năng tái chế nhiều lần &rarr; Chai lọ, rổ rá, dép nhựa, áo mưa.
   - **Chất dẻo nhiệt rắn:** Sau khi nung nóng định hình thì không thể nóng chảy lại (sẽ bị cháy hỏng) &rarr; Tay cầm chảo chống dính, vỏ phích cắm điện, ổ cắm.
   - **Cao su:** Có tính đàn hồi siêu việt, giảm chấn, cách điện cách nhiệt &rarr; Lốp xe máy/ô tô, găng tay cách điện, gioăng đệm làm kín ống nước.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: Nhận Biết Nhanh Vật Liệu Bằng Thực Nghiệm

- **Phương pháp quan sát màu sắc:** Gang xám/thép màu xám đen bóng, đồng đỏ/đồng thau vàng ánh kim, nhôm màu trắng bạc sáng.
- **Phương pháp từ tính:** Dùng nam châm thử. Nam châm hút mạnh &rarr; Kim loại đen (Sắt, Thép, Gang); không hút &rarr; Kim loại màu (Đồng, Nhôm) hoặc phi kim.
- **Phương pháp tác dụng nhiệt:** Đốt que thử chất dẻo. Nóng chảy dẻo ra &rarr; Chất dẻo nhiệt; bốc khói đen biến tính giòn &rarr; Chất dẻo nhiệt rắn.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 6

#### I. Vật Liệu Kim Loại
Trong đời sống, phần lớn các chi tiết máy được làm từ kim loại đen và kim loại màu nhờ tính chất cơ học ưu việt:

![Vật liệu cơ khí](../assets/images/H8_2_dung_cu_gia_cong.png)

#### II. Vật Liệu Phi Kim Loại
Chất dẻo và cao su chiếm vị trí ngày càng quan trọng nhờ đặc tính nhẹ, chống ăn mòn và cách điện tuyệt đối:
- Chất dẻo nhiệt và chất dẻo nhiệt rắn.
- Cao su tự nhiên và cao su nhân tạo.

> **Khám phá:** Hãy kể tên 3 vật dụng trong gia đình em được làm từ hợp kim nhôm và 2 vật dụng làm từ cao su?
""",

    "Chuong_02_Co_khi/content/Bai_07.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Truyền Và Biến Đổi Chuyển Động

> Các bộ phận máy móc thường đặt cách xa nhau và cần vận tốc hoặc dạng chuyển động khác nhau &rarr; Do đó cần **Cơ cấu truyền động** và **Cơ cấu biến đổi chuyển động**.

1. **Bộ truyền động ma sát (Truyền động đai):**
   - Cấu tạo: Bánh dẫn 1 (đường kính $D_1$), Bánh bị dẫn 2 ($D_2$) và Dây đai.
   - **Công thức tính tỉ số truyền $i$:**
     <span style="color:#dc2626; font-weight:700;">$$i = \\frac{n_1}{n_2} = \\frac{D_2}{D_1} \\implies n_2 = n_1 \\times \\frac{D_1}{D_2}$$</span>
   - Trong đó: $n_1$ là tốc độ quay bánh dẫn, $n_2$ là tốc độ quay bánh bị dẫn (vòng/phút).
   - Dây đai mắc thẳng &rarr; Hai bánh quay **CÙNG CHIỀU**; Dây đai mắc chéo &rarr; Hai bánh quay **NGƯỢC CHIỀU**.

2. **Bộ truyền động ăn khớp (Bánh răng & Xích):**
   - **Công thức tính tỉ số truyền theo số răng $Z$:**
     <span style="color:#dc2626; font-weight:700;">$$i = \\frac{n_1}{n_2} = \\frac{Z_2}{Z_1} \\implies n_2 = n_1 \\times \\frac{Z_1}{Z_2}$$</span>
   - Hai bánh răng ăn khớp ngoài &rarr; Quay **NGƯỢC CHIỀU** nhau.
   - Bánh nào có số răng **ÍT HƠN** thì quay **NHANH HƠN**!

3. **Cơ cấu biến đổi chuyển động:**
   - **Cơ cấu tay quay con trượt:** Biến chuyển động quay thành chuyển động tịnh tiến qua lại (ví dụ: xi lanh pít-tông động cơ xe máy, máy bơm hơi).
   - **Cơ cấu tay quay thanh lắc:** Biến chuyển động quay thành chuyển động lắc qua lại (ví dụ: máy may đạp chân, cần gạt nước ô tô).

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Bài Toán Tính Toán Kỹ Thuật: Tính Vận Tốc & Tỉ Số Truyền

**Bài toán mẫu:** Đĩa xích xe đạp có số răng $Z_1 = 44$ răng, líp xe có số răng $Z_2 = 20$ răng. Học sinh đạp xe với tốc độ bàn đạp $n_1 = 50\\text{ vòng/phút}$.
1. **Bước 1 (Xác định dữ kiện):** $Z_1 = 44, Z_2 = 20, n_1 = 50\\text{ vg/ph}$.
2. **Bước 2 (Tính tỉ số truyền $i$):**
   $$i = \\frac{Z_2}{Z_1} = \\frac{20}{44} = \\frac{5}{11} \\approx 0.455$$
3. **Bước 3 (Tính tốc độ quay bánh xe $n_2$):**
   $$n_2 = n_1 \\times \\frac{Z_1}{Z_2} = 50 \\times \\frac{44}{20} = 110\\text{ (vòng/phút)}$$
4. **Bước 4 (Kết luận & Nhận xét):** Bánh sau xe đạp quay nhanh gấp $2.2$ lần tốc độ đạp chân của em, giúp xe chạy nhanh hơn rất nhiều!

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 7

#### I. Truyền Chuyển Động
Tại sao xe đạp cần có đĩa xích, líp và xích xe? Vì trục bàn đạp đặt cách xa trục bánh xe sau:

![Hình 7.1 Truyền động xe đạp](../assets/images/H7_1_truyen_dong_xe_dap.png)

Bộ truyền động đai ma sát:

![Hình 7.2 Truyền động đai](../assets/images/H7_2_truyen_dong_dai.png)

Bộ truyền động ăn khớp bánh răng và xích:

![Hình 7.3 Bánh răng và xích](../assets/images/H7_3_truyen_dong_banh_rang_xich.png)

#### II. Biến Đổi Chuyển Động
Mô hình cơ cấu tay quay con trượt biến chuyển động quay của trục khuỷu thành chuyển động tịnh tiến lên xuống của pít-tông:

![Hình 7.4 Tay quay con trượt](../assets/images/H7_4_co_cau_tay_quay_con_truot.png)

Cơ cấu tay quay thanh lắc dùng trong bàn đạp máy may:

![Hình 7.5 Tay quay thanh lắc](../assets/images/H7_5_co_cau_tay_quay_thanh_lac.png)

> **Luyện tập:** Nếu bánh đai dẫn có đường kính $D_1 = 120\\text{ mm}$, bánh bị dẫn $D_2 = 60\\text{ mm}$, hỏi tỉ số truyền $i$ bằng bao nhiêu?
""",

    "Chuong_02_Co_khi/content/Bai_08.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Gia Công Cơ Khí Bằng Tay

> Gia công cơ khí bằng tay là phương pháp chế tạo chi tiết bằng các dụng cụ cầm tay như cưa, dũa, đục, búa để đạt kích thước và độ bóng bề mặt yêu cầu.

1. **Dụng cụ đo và vạch dấu:**
   - Thước lá, thước cuộn, thước cặp (đo chính xác đến $0.1\\text{ mm}$ hoặc $0.02\\text{ mm}$).
   - Mũi vạch, chấm dấu (đột dấu tâm).

2. **Cưa kim loại:**
   - Dùng để cắt kim loại tấm hoặc thanh phôi thép ra khỏi thanh dài.
   - Lưỡi cưa lắp hướng răng về phía **TRƯỚC**.
   - <span style="color:#dc2626; font-weight:700;">Hành trình cắt:</span> Đẩy cưa về phía trước &rarr; **Ấn nhẹ lực** để răng cưa ăn sâu vào kim loại; Kéo cưa lùi lại &rarr; **Không ấn lực**, kéo nhẹ nhàng.

3. **Dũa kim loại:**
   - Dùng để hớt đi lớp kim loại mỏng trên bề mặt (từ $0.1 \\sim 0.5\\text{ mm}$) để bề mặt nhẵn bóng phẳng phiu.
   - Các loại dũa: Dũa dẹt (mặt phẳng), dũa tròn (lỗ tròn), dũa tam giác (góc nhọn), dũa bán nguyệt.

> [!CAUTION]
> **SAFETY ALERT BOX • AN TOÀN KHI GIA CÔNG CƠ KHÍ:**
> - Kẹp chặt phôi trên ê tô, tay nắm cán dụng cụ chắc chắn, tuyệt đối không dùng dũa/cưa bị lỏng cán hoặc nứt vỡ!
> - Mặc trang phục bảo hộ: kính bảo hộ chống mạt sắt bắn vào mắt, đi giày bít mũi.
> - Tuyệt đối **KHÔNG dùng miệng thổi mạt sắt** hoặc **dùng tay gạt phoi** trên mặt phôi (dễ bị mạt sắt ghim vào tay hoặc bay vào mắt); phải dùng chổi quét chuyên dụng!

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 4 Bước Thao Tác Cưa Kim Loại An Toàn

- **Bước 1 (Lấy dấu & Kẹp phôi):** Dùng thước lá và mũi vạch kẻ đường cần cắt. Kẹp phôi vào má kẹp ê tô sao cho đường vạch dấu nhô lên cách mép ê tô chừng $5 \\sim 10\\text{ mm}$.
- **Bước 2 (Tư thế đứng chuẩn):** Đứng thẳng tự nhiên, chân trái bước chếch một góc $75^\\circ$ so với đường cưa, chân phải lùi sau tạo góc $45^\\circ$. Trọng tâm dồn đều lên hai chân.
- **Bước 3 (Thao tác cưa):** Tay phải nắm cán cưa, tay trái nắm đầu khung cưa. Đẩy cưa từ từ kết hợp ấn lực đều đặn (nhịp cưa khoảng 40 - 50 lần/phút).
- **Bước 4 (Kết thúc cưa):** Khi sắp đứt thanh kim loại, giảm lực ấn tay và đỡ đầu thanh phôi để không làm rơi vào chân hoặc làm gãy lưỡi cưa.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 8

Dụng cụ gia công cầm tay phổ biến:

![Hình 8.2 Dụng cụ gia công](../assets/images/H8_2_dung_cu_gia_cong.png)

> **Thực hành:** Thực hiện dũa mặt phẳng kim loại kích thước $50 \\times 50\\text{ mm}$ đạt độ phẳng và kiểm tra bằng thước góc $90^\\circ$.
""",

    "Chuong_02_Co_khi/content/Bai_09.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Ngành Nghề Trong Lĩnh Vực Cơ Khí

1. **Kỹ sư cơ khí:** Thiết kế các cỗ máy, dây chuyền sản xuất, rô bốt và giám sát quy trình chế tạo.
2. **Kỹ thuật viên cơ khí:** Vận hành máy móc, máy cắt gọt kim loại CNC, bảo trì và hiệu chỉnh thiết bị.
3. **Thợ cơ khí (thợ tiện, thợ hàn, thợ nguội, thợ sửa xe máy/ô tô):** Trực tiếp gia công chi tiết, hàn nối kim loại và sửa chữa lắp ráp máy móc.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: Phân Tích Cơ Hội Nghề Nghiệp STEM Cơ Khí
- Bước 1: Xác định sở thích cá nhân (thích tháo lắp máy móc, thích lập trình điều khiển tay máy rô bốt).
- Bước 2: Rèn luyện kỹ năng đọc bản vẽ kỹ thuật và tư duy hình học không gian.
- Bước 3: Tìm hiểu các trường đào tạo kỹ thuật (Đại học Bách Khoa, trường Cao đẳng Kỹ thuật Công nghệ).

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 9
Bài học giới thiệu các hướng phát triển sự nghiệp trong ngành cơ khí chế tạo máy tại Việt Nam và trên thế giới.
""",

    "Chuong_02_Co_khi/content/Bai_10.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Dự Án Gia Công Chi Tiết Bằng Dụng Cụ Cầm Tay

> Dự án STEM thực hành: Gia công dưỡng đo góc kiểm tra hoặc một chiếc thước vạch dấu bằng thép tấm kích thước chuẩn.

1. **Yêu cầu kỹ thuật sản phẩm:**
   - Kích thước đúng theo bản vẽ chi tiết (dung sai $\\pm 0.5\\text{ mm}$).
   - Các cạnh được dũa nhẵn bóng, không còn ba via sắc nhọn nguy hiểm.
   - Hai cạnh góc vuông tạo thành đúng góc $90^\\circ$.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 4 Bước Thi Công Dự Án Gia Công
- **Bước 1:** Chuẩn bị phôi thép tấm, ê tô, dũa dẹt, cưa sắt, mũi vạch, dưỡng đo góc.
- **Bước 2:** Vạch dấu hình dạng chi tiết lên bề mặt phôi bằng mũi vạch nhọn.
- **Bước 3:** Cưa bỏ phần kim loại thừa cách đường vạch dấu $1 \\sim 2\\text{ mm}$.
- **Bước 4:** Dũa phẳng các cạnh đến đúng vạch dấu, bo tròn các góc nhọn và kiểm tra độ vuông góc.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 10
Báo cáo đánh giá sản phẩm gia công theo các tiêu chí: độ chính xác kích thước, độ nhẵn bề mặt và tuân thủ tuyệt đối an toàn lao động.
""",

    "Chuong_02_Co_khi/content/On_Tap_Chuong_02.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Tổng Kết Ôn Tập Chương II: Cơ Khí
- **Vật liệu:** Kim loại đen (Gang $C > 2.14\\%$, Thép $C \\le 2.14\\%$), Kim loại màu (Đồng, Nhôm), Chất dẻo nhiệt vs nhiệt rắn, Cao su đàn hồi.
- **Truyền động:** $i = \\frac{n_1}{n_2} = \\frac{D_2}{D_1} = \\frac{Z_2}{Z_1}$.
- **Biến đổi chuyển động:** Tay quay con trượt (quay &harr; tịnh tiến), Tay quay thanh lắc (quay &harr; lắc).
- **Gia công tay:** Cưa ấn lực khi đẩy, dũa tạo độ phẳng, cấm thổi phoi bằng miệng!

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Bảng Công Thức Tỉ Số Truyền & Nguyên Lý Chuyển Động
| Bộ truyền động | Tỉ số truyền $i$ | Đặc điểm chiều quay |
|---|---|---|
| Truyền động đai thẳng | $i = \\frac{n_1}{n_2} = \\frac{D_2}{D_1}$ | Cùng chiều |
| Truyền động đai chéo | $i = \\frac{n_1}{n_2} = \\frac{D_2}{D_1}$ | Ngược chiều |
| Bánh răng ăn khớp ngoài | $i = \\frac{n_1}{n_2} = \\frac{Z_2}{Z_1}$ | Ngược chiều |
| Truyền động xích | $i = \\frac{n_1}{n_2} = \\frac{Z_2}{Z_1}$ | Cùng chiều |

<!-- SECTION: SGK_CONTENT -->
### 📖 Câu Hỏi Trọng Tâm Ôn Tập Chương II
1. Nêu sự khác nhau cơ bản giữa gang và thép?
2. Bánh đai bị dẫn có quay nhanh hơn bánh đai dẫn khi $D_2 < D_1$ không? Tại sao?
""",

    # ------------------ CHƯƠNG III: AN TOÀN ĐIỆN ------------------
    "Chuong_03_An_toan_dien/content/Bai_11.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Tai Nạn Điện

> Điện năng đem lại tiện ích to lớn nhưng có thể cướp đi sinh mạng trong tích tắc nếu không hiểu biết về các mối nguy hiểm.

1. **Nguyên nhân gây tai nạn điện:**
   - **Chạm trực tiếp vào vật mang điện:** Chạm tay vào dây trần không bọc cách điện, sửa điện khi chưa ngắt cầu dao.
   - **Chạm gián tiếp qua vỏ thiết bị rò điện:** Vỏ kim loại của máy giặt, bình nóng lạnh bị hỏng lớp cách điện bên trong làm rò điện ra vỏ ngoài.
   - **Vi phạm khoảng cách an toàn lưới điện cao thế:** Đứng quá gần đường dây cao thế hoặc trạm biến áp gây hiện tượng phóng điện trong không khí tạo hồ quang điện tử.
   - **Đến gần dây điện cao thế bị đứt rơi xuống đất:** Xuất hiện điện áp bước cực kỳ nguy hiểm trong bán kính dưới $10\\text{ m}$.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: Cách Thoát Khỏi Vùng Rơi Dây Điện Cao Áp (Điện Áp Bước)
- **Bước 1:** Giữ bình tĩnh, tuyệt đối không bước chân sải dài hay chạy (chênh lệch điện thế giữa 2 bàn chân sẽ làm dòng điện giật ngã).
- **Bước 2:** Chụm hai bàn chân sát vào nhau.
- **Bước 3:** Nhảy chụm hai chân đồng thời (hoặc lướt nhẹ hai chân sát nhau không nhấc rời) từ từ di chuyển ra xa vùng có dây điện đứt tối thiểu $10\\text{ m}$.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 11

Các sự cố đường dây điện và rò điện thường gặp:

![Hình 11.1 Sự cố đường dây](../assets/images/H11_1_su_co_duong_day.png)

Người bị điện giật do chạm vào vỏ máy giặt bị rò điện:

![Hình 11.2 Rò điện máy giặt](../assets/images/H11_2_tai_nan_ro_dien.png)

> **Khám phá:** Tại sao ở các trạm biến áp luôn có biển báo hình tia sét và dòng chữ "CẤM LẠI GẦN - CÓ ĐIỆN NGUY HIỂM CHẾT NGƯỜI"?
""",

    "Chuong_03_An_toan_dien/content/Bai_12.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Biện Pháp An Toàn Điện

1. **Biện pháp an toàn khi sử dụng thiết bị điện:**
   - Nối đất vỏ kim loại cho các đồ dùng điện lớn (máy giặt, bình nước nóng lạnh, tủ lạnh, lò vi sóng). Khi có rò điện, dòng điện sẽ truyền thẳng xuống đất bảo vệ người dùng.
   - Lắp đặt **Aptomat chống rò (ELCB / RCCB)** tự động ngắt điện khi phát hiện dòng rò dù chỉ vài chục milli-ampe ($30\\text{ mA}$).
   - Kiểm tra cách điện định kỳ bằng **Bút thử điện**.

2. **Biện pháp an toàn khi sửa chữa điện:**
   - Cắt cầu dao/aptomat nguồn điện tổng và treo biển: "CÓ NGƯỜI ĐANG SỬA ĐIỆN - CẤM ĐÓNG CẦU DAO".
   - Sử dụng dụng cụ cách điện: kìm có cán bọc cao su chịu điện $1000\\text{ V}$, găng tay cao su, ủng cách điện, thảm cao su.

> [!WARNING]
> **SAFETY ALERT BOX • NGUYÊN TẮC VÀNG:**
> Tuyệt đối không thay bóng đèn hoặc cắm rút phích cắm khi tay hoặc chân đang ướt, chân trần chạm sàn nhà ẩm!

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 4 Bước Sử Dụng Bút Thử Điện Đúng Chuẩn

1. **Bước 1:** Cầm bút thử điện bằng tay thuận, đầu ngón tay cái hoặc ngón trỏ chạm vào chốt tiếp xúc kim loại ở đỉnh chuôi bút.
2. **Bước 2:** Đưa đầu nhọn của bút chạm vào điểm cần thử (ổ cắm hoặc vỏ kim loại nghi ngờ rò điện).
3. **Bước 3:** Quan sát bóng đèn Neon bên trong thân bút: Nếu đèn sáng &rarr; Điểm đó có điện pha lửa cực kỳ nguy hiểm! Nếu đèn không sáng &rarr; Dây nguội (trung tính) hoặc không có điện.
4. **Bước 4:** Rút bút cất vào túi bảo hộ, không dùng bút thử điện để cạy mở ốc vít sai công năng.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 12

Các tình huống sửa chữa điện nguy hiểm cần tuyệt đối tránh:

![Hình 12.3 Sửa điện không an toàn](../assets/images/H12_3_sua_chua_dien_nguy_hiem.png)

> **Luyện tập:** Hãy phân tích tại sao việc đi chân trần trên sàn nhà ẩm ướt khi sửa điện lại khiến nguy cơ tử vong tăng gấp nhiều lần?
""",

    "Chuong_03_An_toan_dien/content/Bai_13.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Sơ Cứu Người Bị Tai Nạn Điện

> Khi phát hiện người bị điện giật, thời gian là vàng ngọc! Cứu nạn nhân trong 1 phút đầu tiên cơ hội sống sót đạt tới $90\\%$.

1. **Nguyên tắc cứu hộ số 1:** <span style="color:#dc2626; font-weight:700;">TUYỆT ĐỐI KHÔNG DÙNG TAY TRẦN CHẠM VÀO NGƯỜI NẠN NHÂN KHI CHƯA NGẮT ĐIỆN</span> (bạn sẽ bị điện giật dính theo ngay lập tức!).
2. **Tách nạn nhân ra khỏi nguồn điện an toàn:**
   - Cắt ngay aptomat, cầu dao, hoặc rút phích cắm điện gần nhất.
   - Nếu không ngắt được điện ngay: Đứng trên ván gỗ khô, dùng gậy tre/gỗ khô hoặc sào nhựa gạt dây điện ra khỏi người nạn nhân.

3. **Sơ cứu khẩn cấp:**
   - Đặt nạn nhân nằm ngửa nơi thoáng khí, nới lỏng thắt lưng, cổ áo.
   - Nếu nạn nhân ngừng thở, tim ngừng đập: Thực hiện ép tim ngoài lồng ngực kết hợp hô hấp nhân tạo (tỉ lệ chuẩn: **30 lần ép tim &rarr; 2 lần thổi ngạt**) liên tục cho đến khi y tế đến.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 3 Bước Sơ Cứu Cấp Bách

- **Bước 1 (Cắt nguồn điện):** Nhanh chóng ngắt aptomat hoặc dùng thanh gỗ khô gạt dây điện rời khỏi cơ thể người gặp nạn.
- **Bước 2 (Kiểm tra tri giác & đường thở):** Vỗ vai, gọi lớn, áp tai vào mũi nạn nhân lắng nghe hơi thở, kiểm tra mạch đập ở cổ.
- **Bước 3 (Hồi sinh tim phổi CPR):** Đặt hai bàn tay lồng vào nhau giữa ngực nạn nhân, ép sâu xuống $5\\text{ cm}$ với tần số $100 \\sim 120$ lần/phút, kết hợp thổi ngạt.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 13

Quy trình tách nạn nhân ra khỏi nguồn điện trong các tình huống thực tế:

![Hình 13.2 Tách nạn nhân khỏi nguồn điện](../assets/images/H13_2_tach_nan_nhan_khoi_nguon.png)

> **Vận dụng:** Hãy diễn tập thao tác gạt dây điện bằng sào gỗ khô cùng các bạn trong nhóm học tập.
""",

    "Chuong_03_An_toan_dien/content/On_Tap_Chuong_03.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Tổng Kết Ôn Tập Chương III: An Toàn Điện
- **Nguyên nhân tai nạn:** Chạm trực tiếp dây trần, chạm gián tiếp vỏ rò điện, vi phạm khoảng cách lưới cao thế, điện áp bước.
- **Biện pháp an toàn:** Nối đất vỏ kim loại, lắp aptomat chống giật ELCB, dùng bút thử điện, găng ủng cao su cách điện.
- **Sơ cứu điện giật:** Cắt cầu dao trước &rarr; Dùng gậy gỗ khô gạt dây &rarr; Cấm sờ tay trần &rarr; CPR ép tim 30 : thổi ngạt 2.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Bảng Xử Lý Tình Huống Khẩn Cấp Về Điện
| Tình huống | Hành động ĐÚNG | Hành động SAI (NGUY HIỂM) |
|---|---|---|
| Nạn nhân đang bị dính vào dây điện | Ngắt cầu dao, lấy chổi gỗ khô gạt | Chạy lại ôm kéo nạn nhân bằng tay |
| Dây điện cao áp đứt rơi trên đường | Chụm chân nhảy lùi xa $> 10\\text{ m}$ | Bước chân dài, chạy tháo thân |
| Vỏ máy giặt rò tê tê giật nhẹ | Rút điện, gọi thợ kiểm tra nối đất | Tiếp tục giặt, lấy băng dính dán vỏ |

<!-- SECTION: SGK_CONTENT -->
### 📖 Câu Hỏi Trọng Tâm Ôn Tập Chương III
1. Nêu 4 biện pháp bảo đảm an toàn khi sử dụng đồ điện trong gia đình?
2. Em sẽ làm gì khi thấy một người bị điện giật tại phòng thực hành?
""",

    # ------------------ CHƯƠNG IV: KĨ THUẬT ĐIỆN ------------------
    "Chuong_04_Ki_thuat_dien/content/Bai_14.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Khái Quát Về Mạch Điện

> Mạch điện là một tập hợp các phần tử điện được kết nối với nhau bằng các dây dẫn để tạo thành một vòng khép kín cho dòng điện chạy qua.

1. **Ba khối thành phần chính của một mạch điện:**
   - **Nguồn điện:** Cung cấp năng lượng điện liên tục (Pin, ắc quy, máy phát điện, lưới điện xoay chiều $220\\text{ V}$).
   - **Thiết bị đóng cắt, điều khiển và bảo vệ:** Đóng/ngắt mạch, bảo vệ khi quá tải, chập mạch (Công tắc, aptomat, cầu chì, relay rơ-le).
   - **Phụ tải tiêu thụ điện:** Biến đổi điện năng thành các dạng năng lượng khác hữu ích:
     - Biến thành quang năng: Bóng đèn LED, đèn sợi đốt.
     - Biến thành nhiệt năng: Bàn là, ấm đun nước, bếp từ.
     - Biến thành cơ năng: Quạt điện, máy bơm nước, động cơ xe điện.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 4 Bước Vẽ Sơ Đồ Khối Mạch Điện
- **Bước 1:** Xác định nguồn điện cung cấp (nguồn điện một chiều DC hay xoay chiều AC).
- **Bước 2:** Vẽ khối thiết bị đóng cắt và bảo vệ (nối tiếp sau nguồn điện).
- **Bước 3:** Vẽ khối phụ tải nhận điện.
- **Bước 4:** Nối dây dẫn tạo thành mạch khép kín từ cực dương qua tải về cực âm (đối với nguồn một chiều).

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 14
Cấu tạo và nguyên lý hoạt động của mạch điện cơ bản:
Nguồn điện &rarr; Thiết bị đóng cắt bảo vệ &rarr; Phụ tải điện.
""",

    "Chuong_04_Ki_thuat_dien/content/Bai_15.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Cảm Biến Và Mô Đun Cảm Biến

> **Cảm biến (Sensor)** là linh kiện điện tử cảm nhận và biến đổi đại lượng vật lý/môi trường (ánh sáng, nhiệt độ, độ ẩm) thành tín hiệu điện.

1. **Các loại cảm biến thông dụng:**
   - **Cảm biến ánh sáng (Quang điện trở LDR):** Khi trời sáng &rarr; điện trở giảm; Khi trời tối &rarr; điện trở tăng vọt.
   - **Cảm biến nhiệt độ (Nhiệt điện trở NTC):** Cảm nhận nhiệt độ môi trường tăng hoặc giảm.
   - **Cảm biến độ ẩm (Độ ẩm đất/không khí):** Đầu dò hai chân cắm vào đất đo hàm lượng nước có trong đất.

2. **Mô đun cảm biến (Sensor Module):**
   - Là một mạch điện hoàn chỉnh tích hợp: Cảm biến + Mạch khuếch đại so sánh điện áp + Rơ-le (Relay) đóng cắt tải công suất lớn.
   - Cổng vào: Nối nguồn cấp ($5\\text{ V}$ hoặc $12\\text{ V}$).
   - Cổng ra: Tiếp điểm rơ-le (NO - Thường mở, NC - Thường đóng, COM - Chân chung) để điều khiển bật/tắt đèn, quạt, bơm.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: Nhận Diện Các Khối Trên Mô Đun Cảm Biến Thực Tế
- **Khối 1 (Đầu vào tín hiệu):** Hai chân cắm linh kiện cảm biến (quang trở hoặc que đo ẩm).
- **Khối 2 (Chiết áp tinh chỉnh):** Biến trở xoay hình vuông có ốc vặn nhỏ màu xanh để chỉnh ngưỡng nhạy sáng hoặc độ ẩm mong muốn.
- **Khối 3 (IC so sánh LM393):** Não bộ so sánh tín hiệu điện áp.
- **Khối 4 (Rơ-le đầu ra):** Khối hộp màu xanh lam để đóng mở tải điện áp $220\\text{ V}$.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 15

Hình ảnh các linh kiện cảm biến phổ biến:

![Hình 15.2 Các loại cảm biến](../assets/images/H15_2_cac_loai_cam_bien.png)

> **Khám phá:** Tại sao ở các siêu thị cửa kính lại tự động mở ra khi có người bước đến gần?
""",

    "Chuong_04_Ki_thuat_dien/content/Bai_16.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Mạch Điện Điều Khiển Dùng Mô Đun Cảm Biến

1. **Sơ đồ khối nguyên lý hoạt động:**
   $$\\text{Môi trường biến đổi} \\longrightarrow \\text{Cảm biến} \\longrightarrow \\text{Mạch khuếch đại} \\longrightarrow \\text{Rơ-le (Relay)} \\longrightarrow \\text{Bật/Tắt Tải}$$
2. **Ứng dụng tiêu biểu trong đời sống thông minh (Smart Home):**
   - **Mô đun cảm biến ánh sáng:** Tự động bật đèn đường khi trời tối ($6\\text{h tối}$) và tắt đèn khi trời sáng ($6\\text{h sáng}$).
   - **Mô đun cảm biến nhiệt độ:** Tự động bật quạt thông gió khi nhiệt độ chuồng trại/phòng máy $> 35^\\circ\\text{C}$.
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

> **Luyện tập:** Hãy trình bày cách đấu nối mô đun cảm biến độ ẩm để điều khiển một máy bơm mini $12\\text{ V}$.
""",

    "Chuong_04_Ki_thuat_dien/content/Bai_17.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Ngành Nghề Trong Lĩnh Vực Kĩ Thuật Điện

1. **Kỹ sư điện:** Thiết kế hệ thống mạng lưới điện tòa nhà, trạm biến áp, tối ưu hóa năng lượng tái tạo (điện mặt trời, điện gió).
2. **Kỹ thuật viên điện:** Lắp đặt tủ điện phân phối, kiểm tra bảo trì đường dây, xử lý sự cố rò chập điện.
3. **Thợ điện:** Thi công đường dây dân dụng trong nhà, lắp đặt công tắc, quạt trần, ổ cắm an toàn.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Phân Tích Nghề Nghiệp STEM: Kỹ Năng Cốt Lõi Của Người Làm Ngành Điện
- Cẩn thận, tỉ mỉ, tôn trọng kỷ luật an toàn lao động lên hàng đầu.
- Nắm vững nguyên lý mạch điện, đọc thành thạo sơ đồ mạch và sử dụng thành thạo đồng hồ vạn năng (VOM).

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 17
Bài học hướng nghiệp giúp học sinh hiểu về môi trường làm việc và yêu cầu phát triển nghề nghiệp trong ngành kỹ thuật điện hiện đại.
""",

    "Chuong_04_Ki_thuat_dien/content/On_Tap_Chuong_04.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Tổng Kết Ôn Tập Chương IV: Kĩ Thuật Điện
- **Mạch điện cơ bản:** Nguồn điện &rarr; Thiết bị đóng cắt bảo vệ &rarr; Phụ tải điện (quang năng, nhiệt năng, cơ năng).
- **Cảm biến:** Biến đổi đại lượng vật lý thành tín hiệu điện tử (LDR quang trở, NTC nhiệt điện trở, que đo độ ẩm).
- **Mô đun cảm biến:** Tích hợp bộ so sánh và rơ-le đóng cắt tải $220\\text{ V}$.
- **Quy trình lắp ráp 5 bước:** Tìm hiểu &rarr; Vẽ sơ đồ &rarr; Chuẩn bị &rarr; Lắp ráp &rarr; Vận hành hiệu chỉnh.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Bảng So Sánh 3 Loại Mô Đun Cảm Biến Cốt Lõi
| Tên mô đun | Linh kiện cảm nhận | Đại lượng môi trường | Ứng dụng thực tế đời sống |
|---|---|---|---|
| Cảm biến ánh sáng | Quang điện trở (LDR) | Cường độ ánh sáng | Đèn đường tự bật tắt ban đêm |
| Cảm biến nhiệt độ | Nhiệt điện trở (NTC) | Nhiệt độ môi trường | Quạt thông gió nhà kính, tủ lạnh |
| Cảm biến độ ẩm | Que đo điện trở đất | Hàm lượng nước trong đất | Hệ thống tưới cây tự động |

<!-- SECTION: SGK_CONTENT -->
### 📖 Câu Hỏi Trọng Tâm Ôn Tập Chương IV
1. Nêu vai trò của rơ-le (Relay) trong mô đun cảm biến?
2. Em hãy thiết kế một mạch điện đơn giản tự động báo động khi nhiệt độ phòng vượt quá $40^\\circ\\text{C}$?
""",

    # ------------------ CHƯƠNG V: THIẾT KẾ KĨ THUẬT ------------------
    "Chuong_05_Thiet_ke_ki_thuat/content/Bai_18.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Giới Thiệu Về Thiết Kế Kĩ Thuật

> **Thiết kế kĩ thuật** là hoạt động sáng tạo của con người nhằm biến ý tưởng thành các giải pháp kỹ thuật, bản vẽ và hồ sơ công nghệ để chế tạo ra sản phẩm đáp ứng nhu cầu cuộc sống.

1. **Vai trò to lớn của thiết kế kỹ thuật:**
   - Phát triển sản phẩm mới thông minh, tiện ích hơn.
   - Tiết kiệm nguyên vật liệu, giảm chi phí sản xuất và giảm ô nhiễm môi trường.
   - Thúc đẩy đổi mới sáng tạo xã hội.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: Vòng Đời Của Một Sản Phẩm Công Nghệ
Nhu cầu thực tiễn &rarr; Thiết kế kỹ thuật &rarr; Chế tạo thử nghiệm &rarr; Đánh giá cải tiến &rarr; Sản xuất đại trà đưa ra thị trường.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 18
Bài học cung cấp cái nhìn tổng quan về phương pháp tiếp cận thiết kế kỹ thuật trong kỷ nguyên công nghệ số 4.0.
""",

    "Chuong_05_Thiet_ke_ki_thuat/content/Bai_19.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Các Bước Cơ Bản Trong Thiết Kế Kĩ Thuật

> Quy trình thiết kế kỹ thuật tiêu chuẩn của SGK bao gồm **5 bước tuần tự lặp lại**:

1. **Bước 1 - Xác định vấn đề & Đề xuất tiêu chí sản phẩm:** Tìm hiểu nhu cầu thực tế cần giải quyết là gì? Sản phẩm cần đạt tiêu chí gì về kích thước, chức năng, chi phí?
2. **Bước 2 - Tìm hiểu tổng quan & Lựa chọn giải pháp:** Nghiên cứu các sản phẩm đã có, đề xuất các ý tưởng khả thi và chọn giải pháp tối ưu nhất.
3. **Bước 3 - Thiết kế chi tiết sản phẩm:** Vẽ bản vẽ kỹ thuật, lập sơ đồ nguyên lý và danh mục vật tư cần chuẩn bị.
4. **Bước 4 - Chế tạo nguyên mẫu & Thử nghiệm:** Tiến hành gia công lắp ráp sản phẩm mẫu và chạy thử trong điều kiện thực tế.
5. **Bước 5 - Đánh giá, hiệu chỉnh & Lập hồ sơ kỹ thuật:** Đánh giá sản phẩm theo các tiêu chí ban đầu; nếu chưa đạt thì quay lại hiệu chỉnh thiết kế; sau đó đóng gói tài liệu hướng dẫn sử dụng.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: Sơ Đồ Tư Duy Thiết Kế 5 Bước Lặp (Iterative Design)
$$\\text{Xác định vấn đề} \\longrightarrow \\text{Chọn giải pháp} \\longrightarrow \\text{Lập bản vẽ} \\longrightarrow \\text{Chế tạo mẫu} \\longrightarrow \\text{Đánh giá (Chưa đạt thì sửa lại)}$$

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 19
Khám phá quá trình cải tiến chiếc quạt bàn từ thời kỳ đầu cho đến các dòng quạt không cánh hiện đại.
""",

    "Chuong_05_Thiet_ke_ki_thuat/content/Bai_20.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Dự Án Thiết Kế Hệ Thống Tưới Cây Tự Động

> Dự án STEM đỉnh cao kết hợp kiến thức liên môn: Cơ khí (lắp đặt ống nước, giá đỡ), Điện tử (mô đun cảm biến độ ẩm, rơ-le, bơm mini) và Sinh học (nhu cầu nước của cây trồng).

1. **Nhiệm vụ thiết kế:**
   - Khi đất khô (độ ẩm $< 40\\%$) &rarr; Mô đun cảm biến kích hoạt rơ-le bật máy bơm hút nước tưới cho chậu cây.
   - Khi đất đã đủ ẩm (độ ẩm $> 70\\%$) &rarr; Mô đun cảm biến ngắt rơ-le, máy bơm tự động dừng hoạt động, tránh ngập úng thối rễ cây.
2. **Linh kiện chính cần chuẩn bị:**
   - 01 Mô đun cảm biến độ ẩm đất kèm que đo.
   - 01 Máy bơm nước mini $5\\text{V} \\sim 12\\text{V}$ và ống dẫn nước dẻo.
   - 01 Hộp chứa nước tưới và nguồn pin/adapter cấp nguồn.
   - Dây nối, cầu đấu vít và hộp bảo vệ mạch điện chống nước.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 4 Bước Triển Khai Lắp Đặt Dự Án Tưới Cây
- **Bước 1 (Đấu nối mạch điện):** Cấp nguồn $5\\text{V}$ cho mô đun cảm biến độ ẩm. Đấu chân tiếp điểm rơ-le nối tiếp với cực dương nguồn máy bơm.
- **Bước 2 (Lắp đặt hệ thống thủy lực):** Cắm đầu hút máy bơm vào bình nước, kéo ống dẫn nước đến gốc cây cảnh, gắn đầu phun tưới nhỏ giọt.
- **Bước 3 (Hiệu chỉnh ngưỡng cảm biến):** Cắm que đo vào chậu đất khô &rarr; Xoay chiết áp trên mô đun cho đèn LED báo hiệu sáng lên và bơm chạy. Sau đó tưới nước ẩm đất &rarr; Kiểm tra máy bơm tự ngắt chuẩn xác.
- **Bước 4 (Đóng gói hoàn thiện):** Cố định đường dây điện và ống nước gọn gàng thẩm mỹ bằng dây rút nhựa, đảm bảo nước không bắn vào mạch điện.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 20

Hình ảnh minh họa mô hình hệ thống tưới cây tự động:

![Hình 20.1 Tưới cây tự động](../assets/images/H20_1_tuoi_cay_tu_dong.png)

Hệ thống tưới cây hẹn giờ tự động:

![Hình 20.2 Tưới cây hẹn giờ](../assets/images/H20_2_he_thong_tuoi_cay_hen_gio.png)

> **Báo cáo sản phẩm:** Trưng bày chậu cây có lắp hệ thống tưới tự động tại lớp và thuyết trình cơ chế vận hành thông minh của nhóm.
""",

    "Chuong_05_Thiet_ke_ki_thuat/content/On_Tap_Chuong_05.md": """<!-- SECTION: QUICK_NOTES -->
### 💡 Tổng Kết Ôn Tập Chương V: Thiết Kế Kĩ Thuật
- **Thiết kế kỹ thuật:** Biến ý tưởng sáng tạo thành hiện thực phục vụ cuộc sống.
- **Quy trình 5 bước:** 1. Xác định vấn đề &rarr; 2. Chọn giải pháp &rarr; 3. Thiết kế chi tiết &rarr; 4. Chế tạo thử nghiệm &rarr; 5. Đánh giá hoàn thiện.
- **Dự án STEM tưới cây:** Cảm biến độ ẩm đất đo tín hiệu &rarr; Rơ-le đóng cắt máy bơm mini theo ngưỡng độ ẩm thiết lập.

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Bảng Tiêu Chí Đánh Giá Dự Án STEM Kỹ Thuật Lớp 8
| Tiêu chí | Mức Đạt (Tốt) | Mức Cần Cải Thiện |
|---|---|---|
| Tính năng tự động | Bơm tự bật khi khô, tự tắt khi ẩm 100% | Bơm chạy liên tục hoặc không tự tắt |
| Độ an toàn điện | Dây bọc cách điện gọn gàng, cách xa nước | Dây hở mối nối, nguy cơ rò điện |
| Tính thẩm mỹ | Đường ống và hộp mạch gọn gàng, chắc chắn | Dây dợ chằng chịt, cồng kềnh |

<!-- SECTION: SGK_CONTENT -->
### 📖 Câu Hỏi Trọng Tâm Ôn Tập Chương V
1. Hãy nêu sự khác biệt giữa thiết kế kỹ thuật và sáng tạo nghệ thuật đơn thuần?
2. Trong quá trình chế tạo thử nghiệm nguyên mẫu, nếu phát hiện sản phẩm không đạt tiêu chí thì em cần làm gì?
"""
}

# Ghi toàn bộ các file bài học
written_count = 0
for file_path, content in LESSONS_CONTENT.items():
    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    written_count += 1
    print(f"Created: {file_path}")

print(f"Successfully generated {written_count} structured lesson files across 5 chapters!")
