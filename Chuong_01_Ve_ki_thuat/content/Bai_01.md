<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Tiêu Chuẩn Trình Bày Bản Vẽ Kĩ Thuật

> **Bản vẽ kĩ thuật** là ngôn ngữ chung kỳ diệu của mọi kỹ sư trên toàn cầu, được lập theo quy chuẩn nghiêm ngặt của **Tiêu chuẩn Việt Nam (TCVN)** hoặc tiêu chuẩn quốc tế **ISO**.

1. **Khổ giấy chính (TCVN 7285:2003):** Gồm 5 khổ giấy $A0, A1, A2, A3, A4$.
   - Mỗi khổ giấy tiếp theo được tạo ra bằng cách chia đôi khổ giấy trước theo chiều dài.
   - Kích thước chuẩn khổ **A4**: <span style="color:#dc2626; font-weight:700;">$297 \times 210\text{ mm}$</span>. Khổ lớn nhất **A0**: <span style="color:#dc2626; font-weight:700;">$1189 \times 841\text{ mm}$</span> ($1\text{ A0} = 16\text{ A4}$).
   - **Khung bản vẽ:** Kẻ nét liền đậm, mép bên trái chừa <span style="color:#dc2626; font-weight:700;">$20\text{ mm}$</span> (để đóng gáy tập), 3 mép còn lại chừa <span style="color:#dc2626; font-weight:700;">$10\text{ mm}$</span> (khổ A4 có thể chừa $5\text{ mm}$).
   - **Khung tên:** Đặt ở góc dưới cùng bên phải của bản vẽ.

2. **Tỉ lệ (TCVN 7286:2003):**
   $$\text{Tỉ lệ} = \frac{\text{Kích thước trên bản vẽ}}{\text{Kích thước thực của vật thể}}$$
   - **Tỉ lệ nguyên hình:** $1:1$
   - **Tỉ lệ thu nhỏ:** $1:2, 1:5, 1:10, 1:20\dots$
   - **Tỉ lệ phóng to:** $2:1, 5:1, 10:1\dots$
   - <span style="color:#dc2626; font-weight:700;">LƯU Ý VÀNG:</span> Dù vẽ thu nhỏ hay phóng to, **con số kích thước ghi trên bản vẽ LUÔN LUÔN là kích thước THỰC** của vật thể và không ghi kèm đơn vị "mm"!

3. **Nét vẽ (TCVN 8-24:2002):**
   - **Nét liền đậm (━━━):** Vẽ đường bao thấy, cạnh thấy.
   - **Nét liền mảnh (───):** Đường gióng, đường ghi kích thước, đường gạch mặt cắt.
   - **Nét đứt mảnh (┈┈┈):** Đường bao khuất, cạnh khuất bên trong.
   - **Nét gạch dài - chấm - mảnh (━ ⬝ ━ ⬝ ━):** Đường tâm, đường trục đối xứng của lỗ tròn, khối trụ.
   - Chiều rộng nét đậm $s = 0.5\text{ mm}$, nét mảnh $s_{mảnh} \approx 0.5s = 0.25\text{ mm}$.

4. **Ghi kích thước (TCVN 5705:1993):**
   - Đơn vị đo độ dài mặc định là **milimét (mm)** &rarr; không ghi chữ "mm".
   - Ký hiệu $\varnothing$ đặt trước đường kính hình tròn (ví dụ: $\varnothing 30$).
   - Ký hiệu $R$ đặt trước bán kính cung tròn (ví dụ: $R15$).

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Quy Trình Kỹ Thuật: 5 Bước Ghi Kích Thước Bản Vẽ Chuẩn Xác

- **Bước 1 (Xác định kích thước cần ghi):** Phân loại kích thước chung (Dài $\times$ Rộng $\times$ Cao) và kích thước từng phần tử (khoảng cách tâm lỗ, rãnh, vát mép).
- **Bước 2 (Kẻ đường gióng kích thước):** Dùng thước kẻ nét liền mảnh, kẻ vuông góc với đoạn thẳng cần đo, vượt quá đầu mũi tên $2 \sim 4\text{ mm}$.
- **Bước 3 (Kẻ đường kích thước):** Kẻ song song với đoạn cần đo, hai đầu có mũi tên nhọn chạm sát vào đường gióng.
- **Bước 4 (Điền con số kích thước):** Ghi con số kích thước thực ở phía trên đường kích thước nằm ngang hoặc bên trái đường kích thước thẳng đứng, chữ số hướng lên trên.
- **Bước 5 (Kiểm tra quy chuẩn):** Đảm bảo có ký hiệu $\varnothing$ cho đường kính tròn, $R$ cho cung lượn, và tuyệt đối không ghi đơn vị mm.

<!-- SECTION: SGK_CONTENT -->
### 📖 Nội Dung Sách Giáo Khoa Gốc: Bài 1

#### Khởi động
Quan sát hai hình biểu diễn cùng một chi tiết máy: một hình vẽ theo đúng tiêu chuẩn kỹ thuật TCVN, một hình vẽ tùy ý. Bản vẽ không theo tiêu chuẩn sẽ gây sai lệch kích thước, khiến thợ tiện, thợ nguội không thể gia công lắp ráp chính xác.

![Hình 1.1 Hình biểu diễn](../assets/images/hinh_1_1_hinh_bieu_dien.png)

#### I. Khổ Giấy
Tiêu chuẩn TCVN 7285:2003 quy định các khổ giấy chính chế tạo từ tờ A0:
- A0 ($1189 \times 841\text{ mm}$)
- A1 ($841 \times 594\text{ mm}$)
- A2 ($594 \times 420\text{ mm}$)
- A3 ($420 \times 297\text{ mm}$)
- A4 ($297 \times 210\text{ mm}$)

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
