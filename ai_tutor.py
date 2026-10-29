import os
import streamlit as st

def get_gemini_client():
    api_key = None
    try:
        if "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        return None, None

    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        return client, "gemini-2.5-flash"
    except Exception:
        return None, None

SYSTEM_PROMPT = """Bạn là 'Kỹ Sư Trí Đức' 🛠️👨‍🏫 - Chuyên gia Kỹ thuật Bách Khoa kiêm Gia sư Công nghệ & STEM tâm huyết dành cho học sinh lớp 8 (13-14 tuổi) học môn Công nghệ 8 (bộ sách Kết nối tri thức với cuộc sống).

Phong cách & Nguyên tắc Sư phạm của bạn:
1. PHƯƠNG PHÁP SOCRATIC: TUYỆT ĐỐI KHÔNG giải tuột đáp án bài tập hoặc vẽ sẵn sơ đồ khi học sinh hỏi. Hãy khen ngợi sự tò mò của học sinh, rồi đặt 1-2 câu hỏi gợi mở từng bước để học sinh tự phân tích bản vẽ, mạch điện và cơ cấu truyền động.
2. AN TOÀN KỸ THUẬT LÀ SỐ 1 (SAFETY FIRST): Luôn nhấn mạnh các quy tắc bảo hộ khi cưa/dũa (kính bảo hộ, không thổi mạt sắt bằng miệng) và an toàn điện (ngắt cầu dao trước khi sửa, kiểm tra bút thử điện, sơ cứu người bị điện giật đúng cách).
3. HƯỚNG DẪN DỰ ÁN HỌC TẬP STEM:
   - Dự án 1 (Bài 10): Gia công chi tiết kim loại bằng dụng cụ cầm tay (vạch dấu -> cưa -> dũa -> kiểm tra vuông góc 90°).
   - Dự án 2 (Bài 20): Thiết kế hệ thống tưới cây tự động dùng cảm biến độ ẩm đất, rơ-le và máy bơm mini (cách ly phần điện với nguồn nước).
4. ĐỊNH HƯỚNG NGHỀ NGHIỆP STEM: Tư vấn truyền cảm hứng về các ngành nghề tương lai: Kỹ sư cơ khí, kỹ thuật viên tự động hóa, thợ điện tử, kỹ sư thiết kế sản phẩm.
5. GIỌNG ĐIỆU: Thân thiện, thực tế, đáng tin cậy. Xưng 'Thầy Đức' hoặc 'Chú Đức' và gọi học sinh là 'Kỹ sư nhí' hoặc 'Nhà sáng chế tương lai'."""

OFFLINE_RESPONSES = {
    # Chương I: Vẽ kỹ thuật
    "kho_giay": "Chào Kỹ sư nhí! 📐 Khổ giấy A0 tiêu chuẩn có kích thước $1189 \\times 841\\text{ mm}$. Mỗi lần bẻ đôi theo chiều dài ta được khổ tiếp theo: A0 &rarr; A1 &rarr; A2 &rarr; A3 &rarr; A4 ($297 \\times 210\\text{ mm}$). Em có nhớ cạnh lề bên trái của khung bản vẽ phải chừa rộng bao nhiêu mm để đóng tập tài liệu không nè?",
    "hinh_chieu": "Ái chà, một câu hỏi rất hay về không gian 3D! 📦 Hãy tưởng tượng một chiếc hộp có 3 mặt vuông góc: Chiếu từ TRƯỚC ra sau là Hình chiếu ĐỨNG ($P_1$); chiếu từ TRÊN xuống là Hình chiếu BẰNG ($P_2$); chiếu từ TRÁI sang là Hình chiếu CẠNH ($P_3$). Khi mở phẳng hộp ra tờ giấy vẽ, hình chiếu bằng sẽ nằm ở đâu so với hình chiếu đứng em nhỉ?",
    "net_ve": "Quy tắc vàng của bản vẽ kỹ thuật: ✏️ Đường bao nào mắt nhìn thấy &rarr; vẽ nét liền ĐẬM ($s = 0.5\\text{ mm}$). Đường nào bị khuất bên trong vật thể &rarr; vẽ nét ĐỨT mảnh. Còn đường tâm và trục đối xứng thì vẽ nét gì em nhỉ?",
    "ban_ve_chi_tiet": "Bản vẽ chi tiết như tấm thẻ Căn cước công dân của một linh kiện! 🪪 Nó có 4 phần: Khung tên, Hình biểu diễn, Kích thước và Yêu cầu kĩ thuật. Thầy đố em bước đầu tiên khi đọc bản vẽ chi tiết là mình phải xem mục nào trước tiên?",
    "ban_ve_lap": "Bản vẽ lắp diễn tả một nhóm chi tiết lắp ghép lại thành cỗ máy (như bộ ròng rọc hay xe đạp) 🏎️. Điểm khác biệt lớn nhất là Bản vẽ lắp CÓ BẢNG KÊ danh mục chi tiết nhưng KHÔNG CÓ yêu cầu gia công từng chi tiết lẻ. Em đã nhìn thấy Bảng kê bao giờ chưa?",
    "ban_ve_nha": "Ngôi nhà xinh đẹp của chúng ta gồm 3 hình biểu diễn: Mặt bằng, Mặt đứng và Mặt cắt 🏡. Trong đó, MẶT BẰNG là hình quan trọng nhất vì cắt ngang tầm cửa sổ nhìn từ trên xuống để thấy rõ từng phòng và lối đi. Em có muốn thử vẽ mặt bằng phòng ngủ của mình không?",

    # Chương II: Cơ khí
    "vat_lieu": "Về vật liệu cơ khí: ⚙️ Kim loại đen gồm Gang (nhiều carbon $C > 2.14\\%$, cứng và giòn) và Thép (dẻo dai, bền). Kim loại màu gồm Đồng (dẫn điện siêu tốt) và Nhôm (nhẹ, bền, chống gỉ). Chất dẻo nhiệt tái chế được, còn chất dẻo nhiệt rắn chịu nhiệt cao không nóng chảy lại. Em thử đoán xem cái vỏ phích cắm điện làm bằng chất dẻo nhiệt hay nhiệt rắn?",
    "ti_so_truyen": "Công thức tỉ số truyền huyền thoại của kỹ sư đây em ơi! 🚲\n$$i = \\frac{n_1}{n_2} = \\frac{D_2}{D_1} = \\frac{Z_2}{Z_1}$$\nBánh nào có số răng ÍT HƠN thì sẽ quay NHANH HƠN. Ví dụ líp xe đạp có 20 răng, đĩa xích có 40 răng, thì khi em đạp 1 vòng, bánh xe sau sẽ quay mấy vòng nè?",
    "bien_doi_chuyen_dong": "Cơ cấu tay quay con trượt biến chuyển động quay tròn của trục khuỷu thành chuyển động tịnh tiến qua lại của pít-tông xi lanh (như trong xe máy) 🛵. Còn cơ cấu tay quay thanh lắc thì biến chuyển động quay thành chuyển động lắc qua lại (như máy may đạp chân). Em còn thấy cơ cấu này ở đâu nữa không?",
    "gia_cong_an_toan": "Lưu ý an toàn sống còn khi cưa và dũa kim loại: ⚠️ Khi cưa chỉ ấn lực khi ĐẨY TỚI, khi lùi kéo nhẹ. TUYỆT ĐỐI KHÔNG dùng miệng thổi mạt sắt (mạt sắt sẽ bay vào mắt gây bỏng giác mạc!), phải dùng chổi quét chuyên dụng! Em đã trang bị kính bảo hộ chưa?",
    "du_an_co_khi": "Dự án Bài 10: Gia công dưỡng đo góc bằng dụng cụ cầm tay 🛠️. Quy trình 4 bước: Vạch dấu chính xác &rarr; Cưa cách vạch $1-2\\text{ mm}$ &rarr; Dũa phẳng tới vạch &rarr; Kiểm tra độ vuông $90^\\circ$ bằng ê-ke. Cạnh dũa phải bóng nhẵn không còn ba via sắc nhọn nhé!",

    # Chương III: An toàn điện
    "tai_nan_dien": "Tai nạn điện cực kỳ nguy hiểm do 3 nguyên nhân chính: ⚡ 1. Chạm trực tiếp dây trần; 2. Chạm gián tiếp vào vỏ máy giặt, bình nóng lạnh bị rò điện; 3. Vi phạm khoảng cách lưới cao thế phóng tia lửa điện. Khi thấy dây cao áp đứt rơi trên đường, em phải đứng cách xa tối thiểu bao nhiêu mét?",
    "bien_phap_an_toan": "Để không bao giờ bị điện giật: 🛡️ Hãy nối đất vỏ kim loại cho bình nóng lạnh/máy giặt, lắp aptomat chống giật ELCB, và kiểm tra ổ cắm bằng Bút thử điện. Thầy đố em khi dùng bút thử điện, ngón tay của mình phải chạm vào đâu?",
    "so_cuu_dien": "Sơ cứu khẩn cấp người bị điện giật: 🚨 NGUYÊN TẮC BẤT DI BẤT DỊCH: CẮT CẦU DAO TRƯỚC TIÊN! Nếu chưa ngắt được điện, dùng sào tre/gỗ khô gạt dây điện ra; CẤM DÙNG TAY KHÔNG CHẠM VÀO NẠN NHÂN! Nếu ngừng thở, ép tim ngoài lồng ngực theo chu kỳ 30 lần ép tim : 2 lần thổi ngạt liên tục!",

    # Chương IV: Kỹ thuật điện
    "mach_dien": "Một mạch điện hoàn chỉnh luôn gồm 3 khối: 🔌 1. Nguồn điện (Pin/Ắc quy/Lưới điện); 2. Thiết bị đóng cắt bảo vệ (Công tắc, Aptomat); 3. Phụ tải tiêu thụ điện (Bóng đèn phát quang, quạt phát cơ năng, ấm nước phát nhiệt năng).",
    "cam_bien": "Cảm biến là giác quan của ngôi nhà thông minh! 👁️ Cảm biến ánh sáng (Quang trở LDR) thay đổi điện trở theo ánh sáng; cảm biến nhiệt độ (NTC) đo độ nóng; cảm biến độ ẩm đất đo lượng nước. Trái tim đóng cắt tải lớn chính là chiếc Rơ-le (Relay) màu xanh lam!",
    "mach_cam_bien": "Mạch điều khiển cảm biến tự động: Khi trời tối, quang trở đổi điện trở &rarr; IC so sánh LM393 kích hoạt Rơ-le đóng tiếp điểm &rarr; Đèn tự động sáng rực! Quy trình 5 bước lắp ráp: Tìm hiểu mô đun &rarr; Vẽ sơ đồ &rarr; Chuẩn bị &rarr; Lắp ráp &rarr; Vận hành hiệu chỉnh chiết áp.",

    # Chương V: Thiết kế kỹ thuật & Dự án STEM
    "quy_trinh_thiet_ke": "Quy trình thiết kế kỹ thuật chuẩn 5 bước của các kỹ sư Bách Khoa: 🚀 1. Xác định vấn đề & Tiêu chí &rarr; 2. Tìm hiểu & Chọn giải pháp &rarr; 3. Lập bản vẽ thiết kế &rarr; 4. Chế tạo nguyên mẫu & Thử nghiệm &rarr; 5. Đánh giá hoàn thiện hồ sơ.",
    "du_an_tuoi_cay": "Dự án STEM Bài 20: Hệ thống tưới cây tự động thông minh 🌱💧. Mô đun cảm biến độ ẩm cắm vào đất chậu hoa: Khi đất khô kiệt &rarr; Rơ-le đóng máy bơm mini $12\\text{V}$ tưới nước; khi đất đã ngậm đủ nước &rarr; Rơ-le ngắt bơm tức thì, chống úng rễ. Lưu ý quan trọng nhất là hộp mạch điện phải cách ly khô ráo với nước!",
    "nghe_nghiep_stem": "Ngành nghề STEM mở ra tương lai rực rỡ cho các em: 🌟 Kỹ sư Cơ khí chế tạo rô bốt, Kỹ sư Điện tự động hóa, Kỹ sư IoT Nhà thông minh, Kỹ sư Thiết kế sản phẩm. Điểm cốt lõi là sự đam mê khám phá máy móc, tính cẩn thận và tư duy giải quyết vấn đề!",

    "default": "Kỹ Sư Trí Đức 🛠️ chào Kỹ sư nhí! Thầy rất hào hứng được đồng hành cùng em. Em đang muốn tìm hiểu về đọc Bản vẽ kỹ thuật, tính Tỉ số truyền bánh răng, bí kíp An toàn điện, mạch Mô đun cảm biến, hay Dự án chế tạo hệ thống tưới cây tự động? Cứ thoải mái đặt câu hỏi cho Thầy nhé!"
}

def ask_ai_tutor(user_message, current_lesson_context=""):
    client, model_name = get_gemini_client()
    if client:
        try:
            full_prompt = f"{SYSTEM_PROMPT}\n\nBài học hiện tại của học sinh: {current_lesson_context}\n\nCâu hỏi của học sinh: {user_message}"
            response = client.models.generate_content(
                model=model_name,
                contents=full_prompt
            )
            return response.text, "online"
        except Exception:
            pass

    # Offline Socratic Fallback thông minh đa tầng
    msg_lower = user_message.lower()
    
    # Chương I
    if any(k in msg_lower for k in ["khổ giấy", "a4", "a0", "kích thước giấy"]):
        reply = OFFLINE_RESPONSES["kho_giay"]
    elif any(k in msg_lower for k in ["hình chiếu", "vuông góc", "chiếu bằng", "chiếu cạnh", "chiếu đứng", "mặt phẳng chiếu"]):
        reply = OFFLINE_RESPONSES["hinh_chieu"]
    elif any(k in msg_lower for k in ["nét vẽ", "nét đứt", "nét đậm", "đường tâm", "chiều rộng nét"]):
        reply = OFFLINE_RESPONSES["net_ve"]
    elif any(k in msg_lower for k in ["chi tiết", "ống lót", "bản vẽ chi tiết"]):
        reply = OFFLINE_RESPONSES["ban_ve_chi_tiet"]
    elif any(k in msg_lower for k in ["bản vẽ lắp", "bảng kê", "ròng rọc"]):
        reply = OFFLINE_RESPONSES["ban_ve_lap"]
    elif any(k in msg_lower for k in ["bản vẽ nhà", "mặt bằng", "mặt đứng", "mặt cắt"]):
        reply = OFFLINE_RESPONSES["ban_ve_nha"]
        
    # Chương II
    elif any(k in msg_lower for k in ["gang", "thép", "đồng", "nhôm", "chất dẻo", "vật liệu", "cao su"]):
        reply = OFFLINE_RESPONSES["vat_lieu"]
    elif any(k in msg_lower for k in ["tỉ số truyền", "bánh răng", "dây đai", "tốc độ quay", "xích xe", "truyền động"]):
        reply = OFFLINE_RESPONSES["ti_so_truyen"]
    elif any(k in msg_lower for k in ["tay quay", "con trượt", "thanh lắc", "biến đổi chuyển động", "pít-tông"]):
        reply = OFFLINE_RESPONSES["bien_doi_chuyen_dong"]
    elif any(k in msg_lower for k in ["cưa", "dũa", "mạt sắt", "an toàn cơ khí", "ê tô", "gia công tay"]):
        reply = OFFLINE_RESPONSES["gia_cong_an_toan"]
    elif any(k in msg_lower for k in ["bài 10", "dự án cơ khí", "thước", "dưỡng kiểm"]):
        reply = OFFLINE_RESPONSES["du_an_co_khi"]

    # Chương III
    elif any(k in msg_lower for k in ["tai nạn điện", "rò điện", "cao thế", "điện áp bước"]):
        reply = OFFLINE_RESPONSES["tai_nan_dien"]
    elif any(k in msg_lower for k in ["nối đất", "aptomat", "bút thử điện", "cách điện", "elcb"]):
        reply = OFFLINE_RESPONSES["bien_phap_an_toan"]
    elif any(k in msg_lower for k in ["sơ cứu", "điện giật", "ép tim", "thổi ngạt", "cpr", "cứu người"]):
        reply = OFFLINE_RESPONSES["so_cuu_dien"]

    # Chương IV
    elif any(k in msg_lower for k in ["mạch điện", "nguồn điện", "phụ tải"]):
        reply = OFFLINE_RESPONSES["mach_dien"]
    elif any(k in msg_lower for k in ["cảm biến", "ldr", "ntc", "quang trở", "nhiệt điện trở", "độ ẩm đất"]):
        reply = OFFLINE_RESPONSES["cam_bien"]
    elif any(k in msg_lower for k in ["mạch điều khiển", "rơ-le", "relay", "mô đun"]):
        reply = OFFLINE_RESPONSES["mach_cam_bien"]

    # Chương V & STEM
    elif any(k in msg_lower for k in ["thiết kế kỹ thuật", "5 bước", "quy trình thiết kế"]):
        reply = OFFLINE_RESPONSES["quy_trinh_thiet_ke"]
    elif any(k in msg_lower for k in ["tưới cây", "bài 20", "dự án tưới", "máy bơm"]):
        reply = OFFLINE_RESPONSES["du_an_tuoi_cay"]
    elif any(k in msg_lower for k in ["nghề nghiệp", "stem", "kỹ sư", "tương lai", "học gì"]):
        reply = OFFLINE_RESPONSES["nghe_nghiep_stem"]
    else:
        reply = OFFLINE_RESPONSES["default"]

    return reply, "offline"
