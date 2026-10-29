<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi: Truyền Và Biến Đổi Chuyển Động

> Các bộ phận máy móc thường đặt cách xa nhau và cần vận tốc hoặc dạng chuyển động khác nhau &rarr; Do đó cần **Cơ cấu truyền động** và **Cơ cấu biến đổi chuyển động**.

1. **Bộ truyền động ma sát (Truyền động đai):**
   - Cấu tạo: Bánh dẫn 1 (đường kính $D_1$), Bánh bị dẫn 2 ($D_2$) và Dây đai.
   - **Công thức tính tỉ số truyền $i$:**
     <span style="color:#dc2626; font-weight:700;">$$i = \frac{n_1}{n_2} = \frac{D_2}{D_1} \implies n_2 = n_1 \times \frac{D_1}{D_2}$$</span>
   - Trong đó: $n_1$ là tốc độ quay bánh dẫn, $n_2$ là tốc độ quay bánh bị dẫn (vòng/phút).
   - Dây đai mắc thẳng &rarr; Hai bánh quay **CÙNG CHIỀU**; Dây đai mắc chéo &rarr; Hai bánh quay **NGƯỢC CHIỀU**.

2. **Bộ truyền động ăn khớp (Bánh răng & Xích):**
   - **Công thức tính tỉ số truyền theo số răng $Z$:**
     <span style="color:#dc2626; font-weight:700;">$$i = \frac{n_1}{n_2} = \frac{Z_2}{Z_1} \implies n_2 = n_1 \times \frac{Z_1}{Z_2}$$</span>
   - Hai bánh răng ăn khớp ngoài &rarr; Quay **NGƯỢC CHIỀU** nhau.
   - Bánh nào có số răng **ÍT HƠN** thì quay **NHANH HƠN**!

3. **Cơ cấu biến đổi chuyển động:**
   - **Cơ cấu tay quay con trượt:** Biến chuyển động quay thành chuyển động tịnh tiến qua lại (ví dụ: xi lanh pít-tông động cơ xe máy, máy bơm hơi).
   - **Cơ cấu tay quay thanh lắc:** Biến chuyển động quay thành chuyển động lắc qua lại (ví dụ: máy may đạp chân, cần gạt nước ô tô).

<!-- SECTION: STEP_EXAMPLES -->
### 🔍 Bài Toán Tính Toán Kỹ Thuật: Tính Vận Tốc & Tỉ Số Truyền

**Bài toán mẫu:** Đĩa xích xe đạp có số răng $Z_1 = 44$ răng, líp xe có số răng $Z_2 = 20$ răng. Học sinh đạp xe với tốc độ bàn đạp $n_1 = 50\text{ vòng/phút}$.
1. **Bước 1 (Xác định dữ kiện):** $Z_1 = 44, Z_2 = 20, n_1 = 50\text{ vg/ph}$.
2. **Bước 2 (Tính tỉ số truyền $i$):**
   $$i = \frac{Z_2}{Z_1} = \frac{20}{44} = \frac{5}{11} \approx 0.455$$
3. **Bước 3 (Tính tốc độ quay bánh xe $n_2$):**
   $$n_2 = n_1 \times \frac{Z_1}{Z_2} = 50 \times \frac{44}{20} = 110\text{ (vòng/phút)}$$
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

> **Luyện tập:** Nếu bánh đai dẫn có đường kính $D_1 = 120\text{ mm}$, bánh bị dẫn $D_2 = 60\text{ mm}$, hỏi tỉ số truyền $i$ bằng bao nhiêu?
