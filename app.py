# -*- coding: utf-8 -*-
import os
import re
import json
import time
import random
import base64
import streamlit as st
import streamlit.components.v1 as components
from database import init_db, save_result, get_leaderboard, get_student_streak
from ai_tutor import ask_ai_tutor
from lesson_parser import parse_lesson_sections, render_base64_images

# Khởi tạo SQLite DB
init_db()

# Cấu hình giao diện Streamlit
st.set_page_config(
    page_title="Công Nghệ 8 • Cùng Kỹ Sư Trí Đức 🤖",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_IMG_DIR = os.path.join(BASE_DIR, "assets", "images")
STICKERS_DIR = os.path.join(BASE_DIR, "assets", "stickers")

# Helper nạp ảnh Base64 an toàn cho Sticker 3D
def get_sticker_base64(name):
    path = os.path.join(STICKERS_DIR, name)
    if os.path.exists(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        ext = os.path.splitext(name)[1].lower().replace(".", "")
        return f"data:image/{ext};base64,{encoded}"
    return ""

robot_sticker = get_sticker_base64("robot_avatar.png")
compass_sticker = get_sticker_base64("compass_3d.png")
gear_sticker = get_sticker_base64("gear_3d.png")
flash_sticker = get_sticker_base64("flash_3d.png")
bulb_sticker = get_sticker_base64("bulb_3d.png")
rocket_sticker = get_sticker_base64("rocket_3d.png")
trophy_sticker = get_sticker_base64("trophy_3d.png")
book_sticker = get_sticker_base64("book_3d.png")
shield_sticker = get_sticker_base64("shield_3d.png")
fire_sticker = get_sticker_base64("fire_3d.png")
medal_sticker = get_sticker_base64("medal_3d.png")

# CSS Chuyên Sâu & Cơ chế chống lỗi React removeChild do Trình duyệt / Google Dịch
st.markdown("""
<meta name="google" content="notranslate">
<meta name="robots" content="notranslate">
<div class="notranslate" translate="no" style="display:none;"></div>
<script>
    // Tự động gán thuộc tính cấm Google Dịch can thiệp phá hỏng DOM React
    document.documentElement.lang = "vi";
    document.documentElement.setAttribute("translate", "no");
    document.documentElement.classList.add("notranslate");
    if (document.body) {
        document.body.setAttribute("translate", "no");
        document.body.classList.add("notranslate");
    }
</script>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@600;700&family=Nunito:wght@400;500;600;700;800&display=swap');
    
    /* Chống Google Translate / Edge Translator can thiệp làm vỡ DOM */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], .notranslate {
        translate: no !important;
    }

    /* Áp dụng font chỉ cho văn bản thuần, TUYỆT ĐỐI KHÔNG can thiệp vào thẻ icon và SVG của Streamlit */
    html, body, p, li, [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
        font-family: 'Nunito', sans-serif !important;
        color: #1e293b;
        font-size: 15.5px;
        line-height: 1.7;
    }
    
    /* BẢO VỆ NGUYÊN BẢN CÁC ICON CỦA STREAMLIT (Chống lỗi ligature arrow_down, smart_toy) */
    [data-testid="stExpanderIcon"], 
    [data-testid*="Icon"], 
    .material-symbols-rounded, 
    .material-symbols-sharp, 
    .material-symbols-outlined, 
    [class*="material-symbols"], 
    [class*="material-icons"] {
        font-family: 'Material Symbols Rounded', 'Material Icons' !important;
        font-style: normal !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        line-height: 1 !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        white-space: nowrap !important;
        word-wrap: normal !important;
        direction: ltr !important;
    }
    
    /* Header Công Nghệ 3D Rực Rỡ & Nổi Bật */
    .hero-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #06b6d4 100%);
        padding: 24px 30px;
        border-radius: 20px;
        color: #ffffff !important;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.25);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .hero-header h1 {
        font-family: 'Comfortaa', cursive !important;
        margin: 0;
        font-size: 26px;
        font-weight: 700;
        color: #ffffff !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .hero-header p {
        margin: 6px 0 0 0;
        font-size: 15px;
        color: #e0f2fe !important;
    }
    
    /* Thẻ Ghi Nhớ Cốt Lõi: Nền trắng tinh, viền bo pastel, độ tương phản hoàn hảo */
    .quick-card {
        background: #ffffff;
        border: 2px solid #e2e8f0;
        border-radius: 18px;
        padding: 24px 28px;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
    }
    
    /* Highlight ĐỎ TƯƠI có chọn lọc cho từ khóa kỹ thuật then chốt */
    .key-red {
        color: #dc2626 !important;
        font-weight: 800 !important;
    }
    
    /* Hộp Cảnh Báo An Toàn Lao Động & Điện (Safety Alert Box) có Sticker */
    .safety-alert-danger {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        border: 2px solid #f87171;
        border-left: 8px solid #dc2626;
        border-radius: 16px;
        padding: 18px 22px;
        margin: 18px 0;
        color: #991b1b;
        box-shadow: 0 4px 12px rgba(220, 38, 38, 0.08);
    }
    
    /* Card trắc nghiệm 3D */
    .quiz-card-3d {
        background: #ffffff;
        border: 2px solid #e2e8f0;
        border-radius: 16px;
        padding: 20px 22px;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .quiz-card-3d:hover {
        border-color: #3b82f6;
        transform: translateY(-2px);
    }
    
    /* Sidebar Cute & Hiện Đại */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 2px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Cấu trúc 5 Chương, 20 Bài học và 5 Bài ôn tập tổng kết SGK Công nghệ 8
CHAPTERS = {
    "chuong_01": {
        "name": "Chương I: Vẽ Kĩ Thuật",
        "icon_sticker": compass_sticker,
        "folder": "Chuong_01_Ve_ki_thuat",
        "alt_folder": "Chuong_01_Ve_Ky_Thuat",
        "lessons": {
            "bai_01": {"title": "Bài 1: Tiêu chuẩn bản vẽ kĩ thuật 📐", "file": "Bai_01.md"},
            "bai_02": {"title": "Bài 2: Hình chiếu vuông góc 📦", "file": "Bai_02.md", "interactive": True},
            "bai_03": {"title": "Bài 3: Bản vẽ chi tiết 🪪", "file": "Bai_03.md"},
            "bai_04": {"title": "Bài 4: Bản vẽ lắp 🏎️", "file": "Bai_04.md"},
            "bai_05": {"title": "Bài 5: Bản vẽ nhà 🏡", "file": "Bai_05.md"},
            "on_tap_chuong_01": {"title": "Ôn tập tổng kết Chương I 🏆", "file": "On_Tap_Chuong_01.md"}
        }
    },
    "chuong_02": {
        "name": "Chương II: Cơ Khí",
        "icon_sticker": gear_sticker,
        "folder": "Chuong_02_Co_khi",
        "lessons": {
            "bai_06": {"title": "Bài 6: Vật liệu cơ khí 🔩", "file": "Bai_06.md"},
            "bai_07": {"title": "Bài 7: Truyền và biến đổi chuyển động 🚲", "file": "Bai_07.md"},
            "bai_08": {"title": "Bài 8: Gia công cơ khí bằng tay 🛠️", "file": "Bai_08.md"},
            "bai_09": {"title": "Bài 9: Ngành nghề trong lĩnh vực cơ khí 🏭", "file": "Bai_09.md"},
            "bai_10": {"title": "Bài 10: Dự án: Gia công chi tiết cầm tay 📏", "file": "Bai_10.md"},
            "on_tap_chuong_02": {"title": "Ôn tập tổng kết Chương II 🏆", "file": "On_Tap_Chuong_02.md"}
        }
    },
    "chuong_03": {
        "name": "Chương III: An Toàn Điện",
        "icon_sticker": flash_sticker,
        "folder": "Chuong_03_An_toan_dien",
        "lessons": {
            "bai_11": {"title": "Bài 11: Tai nạn điện ⚠️", "file": "Bai_11.md"},
            "bai_12": {"title": "Bài 12: Biện pháp an toàn điện 🛡️", "file": "Bai_12.md"},
            "bai_13": {"title": "Bài 13: Sơ cứu người bị tai nạn điện 🚨", "file": "Bai_13.md"},
            "on_tap_chuong_03": {"title": "Ôn tập tổng kết Chương III 🏆", "file": "On_Tap_Chuong_03.md"}
        }
    },
    "chuong_04": {
        "name": "Chương IV: Kĩ Thuật Điện",
        "icon_sticker": bulb_sticker,
        "folder": "Chuong_04_Ki_thuat_dien",
        "lessons": {
            "bai_14": {"title": "Bài 14: Khái quát về mạch điện 🔌", "file": "Bai_14.md"},
            "bai_15": {"title": "Bài 15: Cảm biến và mô đun cảm biến 👁️", "file": "Bai_15.md"},
            "bai_16": {"title": "Bài 16: Mạch điều khiển dùng mô đun cảm biến 🎛️", "file": "Bai_16.md"},
            "bai_17": {"title": "Bài 17: Ngành nghề trong lĩnh vực kĩ thuật điện 👷", "file": "Bai_17.md"},
            "on_tap_chuong_04": {"title": "Ôn tập tổng kết Chương IV 🏆", "file": "On_Tap_Chuong_04.md"}
        }
    },
    "chuong_05": {
        "name": "Chương V: Thiết Kế Kĩ Thuật & STEM",
        "icon_sticker": rocket_sticker,
        "folder": "Chuong_05_Thiet_ke_ki_thuat",
        "lessons": {
            "bai_18": {"title": "Bài 18: Giới thiệu về thiết kế kĩ thuật 💡", "file": "Bai_18.md"},
            "bai_19": {"title": "Bài 19: Các bước cơ bản trong thiết kế kĩ thuật 📋", "file": "Bai_19.md"},
            "bai_20": {"title": "Bài 20: Dự án: Hệ thống tưới cây tự động 🌱", "file": "Bai_20.md"},
            "on_tap_chuong_05": {"title": "Ôn tập tổng kết Chương V 🏆", "file": "On_Tap_Chuong_05.md"}
        }
    }
}

MOTIVATIONAL_QUOTES = [
    "🚀 'Bản vẽ kỹ thuật là ngôn ngữ chung kỳ diệu của mọi nhà sáng chế trên toàn thế giới!'",
    "⚙️ 'Cơ khí chính xác và tự động hóa là xương sống của mọi nền công nghiệp hiện đại.'",
    "⚡ 'An toàn lao động không phải là điều ngẫu nhiên - đó là kỷ luật và sự hiểu biết khoa học.'",
    "🌱 'Sáng tạo STEM là học cách quan sát thế giới và tự tay chế tạo giải pháp phục vụ con người.'",
    "💡 'Hiểu sâu bản chất từng cơ cấu máy móc - bạn đã nắm chắc tương lai kỹ thuật trong tầm tay!'"
]

# ----------------- SIDEBAR ĐIỀU HƯỚNG CÓ STICKER 3D -----------------
with st.sidebar:
    st.markdown(f"""
    <div style="text-align: center; padding: 10px 0;">
        <img src="{robot_sticker}" width="90" style="filter: drop-shadow(0 6px 12px rgba(37,99,235,0.2));">
        <h3 style="margin: 8px 0 2px 0; color: #1e3a8a; font-family: 'Comfortaa';">Kỹ Sư Trí Đức</h3>
        <p style="font-size: 13px; color: #64748b; margin: 0;">Gia Sư Công Nghệ & STEM Lớp 8</p>
    </div>
    """, unsafe_allow_html=True)
    
    student_name = st.text_input("👤 Họ và tên:", value="Bạn Nhỏ Bách Khoa", help="Tên để vinh danh trên bảng vàng")
    student_class = st.text_input("🏫 Lớp:", value="8A1")
    streak_days = get_student_streak(student_name)
    
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: center; gap: 8px; background: #fffbeb; border: 1.5px solid #fef3c7; padding: 6px 14px; border-radius: 20px; margin: 6px 0 16px 0;">
        <img src="{fire_sticker}" width="22">
        <span style="color: #b45309; font-weight: 700; font-size: 13px;">Chuỗi học: {streak_days} ngày liên tục</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h4 style='color:#1e3a8a; margin-bottom: 6px;'>📚 Danh Mục Chương Học</h4>", unsafe_allow_html=True)
    
    selected_ch_key = st.selectbox(
        "Chọn chương muốn học:",
        options=list(CHAPTERS.keys()),
        format_func=lambda k: CHAPTERS[k]["name"]
    )
    
    ch_info = CHAPTERS[selected_ch_key]
    selected_lesson_key = st.selectbox(
        "Chọn bài học:",
        options=list(ch_info["lessons"].keys()),
        format_func=lambda lk: ch_info["lessons"][lk]["title"]
    )
    
    st.markdown("---")
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
        <img src="{trophy_sticker}" width="26">
        <h4 style="color:#b45309; margin: 0;">Bảng Vàng Vinh Danh</h4>
    </div>
    """, unsafe_allow_html=True)
    
    top_students = get_leaderboard(selected_lesson_key, limit=5)
    if top_students:
        medals = ["🥇", "🥈", "🥉", "🎖️", "⭐"]
        for idx, s in enumerate(top_students):
            m = medals[idx] if idx < len(medals) else "✨"
            st.markdown(f"**{m} {s[0]} ({s[1]})** &rarr; `{s[2]:.1f}/10 đ` *({s[3]}s)*")
    else:
        st.caption("Chưa có ai ghi danh! Hãy thử sức tại Tab 3 để leo lên đỉnh Bảng Vàng nhé! 🌟")

# ----------------- HEADER CHÍNH CÓ STICKER CHƯƠNG -----------------
current_lesson = ch_info["lessons"][selected_lesson_key]
st.markdown(f"""
<div class="hero-header">
    <div style="display: flex; align-items: center; gap: 18px;">
        <img src="{ch_info['icon_sticker']}" width="65" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15));">
        <div>
            <h1>⚙️ CÔNG NGHỆ 8 • KẾT NỐI TRI THỨC VỚI CUỘC SỐNG</h1>
            <p>Hôm nay chúng mình cùng học: <b>{current_lesson['title']}</b> ({ch_info['name']})</p>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.2); backdrop-filter: blur(8px); padding: 8px 18px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.4); font-weight: 700; color: white;">
        🛠️ Kỹ sư nhí: <b>{student_name}</b> ({student_class})
    </div>
</div>
""", unsafe_allow_html=True)

# Lời nhắn động lực
quote = random.choice(MOTIVATIONAL_QUOTES)
st.markdown(f"""
<div style="background:#eff6ff; border-left: 5px solid #2563eb; border-radius: 12px; padding: 12px 20px; margin-bottom: 20px; color: #1e3a8a; font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 20px;">💡</span>
    <span><b>Lời nhắn từ Kỹ Sư Trí Đức:</b> {quote}</span>
</div>
""", unsafe_allow_html=True)

# Đọc Markdown trực tiếp từ đĩa
def load_lesson_markdown(ch_dict, lesson_file):
    search_dirs = [
        os.path.join(BASE_DIR, ch_dict.get("folder", ""), "content"),
        os.path.join(BASE_DIR, ch_dict.get("alt_folder", ""), "content")
    ]
    for s_dir in search_dirs:
        full_p = os.path.join(s_dir, lesson_file)
        if os.path.exists(full_p):
            with open(full_p, "r", encoding="utf-8") as f:
                return f.read(), s_dir
    return "", ""

raw_md, md_dir = load_lesson_markdown(ch_info, current_lesson["file"])
img_dirs = [ASSETS_IMG_DIR, os.path.join(os.path.dirname(md_dir), "assets", "images")]
sections = parse_lesson_sections(raw_md)

# ----------------- 4 TAB SƯ PHẠM CÔNG NGHỆ -----------------
tab1, tab2, tab3, tab4 = st.tabs([
    "💡 Tab 1: Bài Học & Lý Thuyết Trực Quan",
    "🔍 Tab 2: Quy Trình Kỹ Thuật & Đọc Bản Vẽ Chi Tiết",
    "🎯 Tab 3: Đấu Trường Kỹ Thuật & Tự Chấm Điểm",
    "🤖 Tab 4: Kỹ Sư AI Socratic — Kỹ Sư Trí Đức"
])

# ================= TAB 1: BÀI HỌC & LÝ THUYẾT TRỰC QUAN =================
with tab1:
    sub_tab1, sub_tab2, sub_tab3 = st.tabs([
        "💡 Thẻ 1: Ghi Nhớ Nhanh & Trọng Tâm",
        "📝 Thẻ 2: Đọc Bản Vẽ & Thao Tác Kỹ Thuật",
        "📖 Thẻ 3: Đọc Thêm SGK Gốc"
    ])
    
    with sub_tab1:
        if sections["quick_notes"]:
            rendered_qn = render_base64_images(sections["quick_notes"], img_dirs)
            st.markdown(f'<div class="quick-card">\n\n{rendered_qn}\n\n</div>', unsafe_allow_html=True)
        else:
            st.info("Nội dung ghi nhớ nhanh đang được nạp...")
        
        # Nhúng Video bài giảng YouTube
        videos_path = os.path.join(BASE_DIR, "data", "lesson_videos.json")
        if os.path.exists(videos_path):
            with open(videos_path, "r", encoding="utf-8") as vf:
                v_all = json.load(vf)
            v_info = v_all.get(selected_lesson_key, {})
            if v_info:
                with st.expander("🎬 Video bài giảng giáo viên tuyển chọn (VietJack / HOCMAI / OLM)", expanded=False):
                    st.video(v_info.get("video_url", ""))
                    st.info(f"👨‍🏫 **Giáo viên hướng dẫn:** {v_info.get('teacher', '')}\n\n🎯 **Mục tiêu then chốt:** {v_info.get('objectives', '')}")
                    
    with sub_tab2:
        if current_lesson.get("interactive"):
            st.subheader("📐 Widget Mô Phỏng Tương Tác 3D/SVG: Hộp 3 Mặt Phẳng Chiếu")
            st.caption("Em hãy bấm đổi góc nhìn 3D không gian và bấm 'Mở hộp' để quan sát cách trải phẳng ra tờ giấy vẽ.")
            w_paths = [
                os.path.join(BASE_DIR, "assets", "interactive_projection_box.html"),
                os.path.join(BASE_DIR, "Chuong_01_Ve_Ky_Thuat", "assets", "interactive_projection_box.html")
            ]
            for wp in w_paths:
                if os.path.exists(wp):
                    with open(wp, "r", encoding="utf-8") as wf:
                        components.html(wf.read(), height=530, scrolling=False)
                    break
            st.markdown("---")
            
        if sections["step_examples"]:
            rendered_se = render_base64_images(sections["step_examples"], img_dirs)
            st.markdown(f'<div class="quick-card">\n\n{rendered_se}\n\n</div>', unsafe_allow_html=True)
        else:
            st.info("Các bước đọc bản vẽ và thao tác kỹ thuật đang được hiển thị chi tiết tại Tab 2.")
        
    with sub_tab3:
        with st.expander("📖 Xem toàn bộ nội dung Sách Giáo Khoa gốc & Hoạt động Khám phá", expanded=True):
            if sections["sgk_content"]:
                rendered_sgk = render_base64_images(sections["sgk_content"], img_dirs)
                st.markdown(rendered_sgk, unsafe_allow_html=True)
            else:
                st.info("Nội dung SGK chi tiết đang được cập nhật.")

# ================= TAB 2: QUY TRÌNH KỸ THUẬT & ĐỌC BẢN VẼ CHI TIẾT =================
with tab2:
    st.subheader("🔍 Chuẩn Hóa 3 Dạng Quy Trình Kỹ Thuật & Đọc Bản Vẽ SGK")
    st.caption("Kỹ sư Trí Đức đã chuẩn hóa toàn bộ các dạng bài tập kỹ thuật thành 3 quy trình tư duy 4 tầng chuẩn mực:")
    
    proc_path = os.path.join(BASE_DIR, "data", "technical_procedures.json")
    proc_data = {}
    if os.path.exists(proc_path):
        with open(proc_path, "r", encoding="utf-8") as pf:
            proc_data = json.load(pf)
            
    p_type = st.radio(
        "Chọn dạng bài kỹ thuật muốn tìm hiểu:",
        [
            "Dạng 1: Đọc Bản Vẽ Kỹ Thuật (5 Bước Chuẩn SGK)",
            "Dạng 2: Quy Trình Thao Tác & Lắp Ráp An Toàn",
            "Dạng 3: Bài Toán Tính Toán Kỹ Thuật (Tỉ Số Truyền & Thông Số)"
        ],
        horizontal=True
    )
    
    target_key = "dang_1_doc_ban_ve" if "Dạng 1" in p_type else ("dang_2_thao_tac_an_toan" if "Dạng 2" in p_type else "dang_3_tinh_toan_ky_thuat")
    curr_proc = proc_data.get(target_key, {})
    
    if curr_proc:
        st.markdown(f"""
        <div style="background:#eff6ff; border:2px solid #bfdbfe; border-radius:16px; padding:18px 24px; margin: 16px 0;">
            <h4 style="color:#1e40af; margin-top:0;">{curr_proc.get('title', '')}</h4>
            <p style="font-size:14.5px; color:#1e3a8a; margin:0;">{curr_proc.get('description', '')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        for p_step in curr_proc.get("steps", []):
            with st.expander(f"📌 {p_step['step']}", expanded=True):
                st.markdown(f"**Hành động chuẩn mực:** {p_step['action']}")
                st.info(f"💡 **Ví dụ minh họa thực tế:** {p_step['example']}")
                
        st.success(f"💖 **Bảo Bối Then Chốt Của Kỹ Sư:** {curr_proc.get('key_takeaway', '')}")

# ================= TAB 3: ĐẤU TRƯỜNG KỸ THUẬT & TỰ CHẤM ĐIỂM =================
with tab3:
    arena_mode = st.radio("Chọn hình thức luyện tập:", [
        "⚡ Đấu Trường Trắc Nghiệm Tính Giờ (Gamified Quiz)",
        "📚 Lời Giải Chi Tiết 4 Bước Toàn Bộ Bài Tập SGK"
    ], horizontal=True)
    
    if arena_mode == "⚡ Đấu Trường Trắc Nghiệm Tính Giờ (Gamified Quiz)":
        ex_path = os.path.join(BASE_DIR, "data", "extra_exercises.json")
        quiz_data = {}
        if os.path.exists(ex_path):
            with open(ex_path, "r", encoding="utf-8") as ef:
                quiz_data = json.load(ef)
        questions = quiz_data.get(selected_lesson_key, [])
        
        if questions:
            timer_key = f"quiz_timer_{selected_lesson_key}"
            if timer_key not in st.session_state:
                st.session_state[timer_key] = time.time()
                
            with st.form(f"quiz_form_{selected_lesson_key}"):
                st.markdown(f"**Đề thi gồm {len(questions)} câu hỏi trắc nghiệm kiểm tra kiến thức bài: *{current_lesson['title']}***")
                user_answers = {}
                for q in questions:
                    lvl_badge = "background:#dcfce7; color:#166534;" if q["level"]=="Dễ" else ("background:#fef3c7; color:#92400e;" if q["level"]=="Vừa" else "background:#fee2e2; color:#991b1b;")
                    st.markdown(f"""
                    <div class="quiz-card-3d">
                        <span style="{lvl_badge} padding:4px 12px; border-radius:12px; font-size:12px; font-weight:800;">Cấp độ: {q['level']}</span>
                        <p style="font-size:15px; font-weight:700; margin:10px 0 0 0; color:#1e293b;">{q['question']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    user_answers[q["id"]] = st.radio(
                        "Chọn đáp án đúng nhất:",
                        options=[opt[0] for opt in q["options"]],
                        format_func=lambda o, q_opts=q["options"]: next(opt for opt in q_opts if opt.startswith(o)),
                        key=f"q_{selected_lesson_key}_{q['id']}",
                        horizontal=True
                    )
                    st.write("")
                    
                submitted = st.form_submit_button("Nộp Bài & Tự Chấm Điểm 🎯✨")
                if submitted:
                    time_spent = int(time.time() - st.session_state[timer_key])
                    correct_count = sum(1 for q in questions if user_answers.get(q["id"]) == q["correct"])
                    score = round((correct_count / len(questions)) * 10, 1)
                    save_result(student_name, student_class, selected_lesson_key, score, len(questions), time_spent)
                    
                    if score >= 7.0:
                        st.balloons()
                        st.success(f"🎉 Xuất sắc! Kỹ sư nhí **{student_name}** đạt **{score}/10 điểm** ({correct_count}/{len(questions)} câu đúng) trong **{time_spent} giây**! Thành tích đã được ghi danh trên Bảng Vàng!")
                    else:
                        st.warning(f"Bạn đạt **{score}/10 điểm** ({correct_count}/{len(questions)} câu đúng) trong **{time_spent} giây**. Hãy xem lại phần Ghi nhớ nhanh ở Tab 1 và thử lại nhé!")
                        
                    with st.expander("🔍 Xem giải thích chi tiết đáp án từng câu hỏi"):
                        for q in questions:
                            ans = user_answers.get(q["id"])
                            is_r = (ans == q["correct"])
                            st.markdown(f"**{'✅' if is_r else '❌'} {q['question']}**")
                            st.markdown(f"- Đáp án đúng: **{q['correct']}** (Bạn chọn: {ans})")
                            st.info(f"💡 {q['explanation']}")
        else:
            st.info("Chưa có câu hỏi trắc nghiệm cho bài này.")
    else:
        st.subheader("📚 Lời Giải Chi Tiết 4 Bước Toàn Bộ Bài Tập SGK")
        sol_path = os.path.join(BASE_DIR, "data", "sgk_solutions.json")
        sol_data = {}
        if os.path.exists(sol_path):
            with open(sol_path, "r", encoding="utf-8") as sf:
                sol_data = json.load(sf)
        exercises = sol_data.get(selected_lesson_key, [])
        if exercises:
            for idx, ex in enumerate(exercises):
                with st.expander(f"📌 {ex['question']}", expanded=(idx==0)):
                    st.markdown(f"**1. Phương pháp tư duy:** {ex['method']}")
                    st.markdown(f"**2. Bước 1:** {ex['step_1']}")
                    st.markdown(f"**3. Bước 2:** {ex['step_2']}")
                    if 'step_3' in ex:
                        st.markdown(f"**3. Bước 3:** {ex['step_3']}")
                    st.markdown(f"**✅ Kết luận:** {ex['conclusion']}")
                    st.success(f"💡 **Bảo bối then chốt:** {ex['key_takeaway']}")
                    
            st.markdown("---")
            st.subheader("📝 Ô Nháp Kỹ Thuật Tương Tác")
            st.text_area("Học sinh tự nháp công thức, tính toán tỉ số truyền hoặc tóm tắt sơ đồ tại đây:", height=120)
        else:
            st.info("Lời giải chi tiết đang được cập nhật.")

# ================= TAB 4: KỸ SƯ AI SOCRATIC — KỸ SƯ TRÍ ĐỨC =================
with tab4:
    col_t_head, col_t_badge = st.columns([3, 1])
    with col_t_head:
        st.subheader("🤖 Trò Chuyện Cùng Kỹ Sư Trí Đức")
        st.caption("Thầy Đức giải thích máy móc đời sống bằng phương pháp Socratic gợi mở, hỗ trợ 2 Dự án STEM và Định hướng nghề nghiệp!")
    with col_t_badge:
        st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:flex-end; gap:6px;">
            <img src="{robot_sticker}" width="32">
            <span style="background:#dbeafe; border:1px solid #93c5fd; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:bold; color:#1e40af;">Socratic AI</span>
        </div>
        """, unsafe_allow_html=True)
        
    chat_key = f"chat_history_{selected_lesson_key}"
    if chat_key not in st.session_state:
        st.session_state[chat_key] = [
            {"role": "assistant", "content": f"Chào Kỹ sư nhí **{student_name}**! 🛠️ Thầy là Kỹ Sư Trí Đức. Hôm nay chúng mình cùng học **{current_lesson['title']}** nhé! Em có chỗ nào thắc mắc về đọc bản vẽ, tính tỉ số truyền, an toàn điện hay dự án STEM không? Cứ hỏi Thầy thoải mái nhé!"}
        ]
        
    for msg in st.session_state[chat_key]:
        msg_avatar = robot_sticker if msg["role"] == "assistant" else "🧑‍🎓"
        with st.chat_message(msg["role"], avatar=msg_avatar):
            st.markdown(msg["content"])
            
    if user_prompt := st.chat_input("Hỏi Thầy Đức về bản vẽ, mạch điện cảm biến, dự án tưới cây..."):
        st.session_state[chat_key].append({"role": "user", "content": user_prompt})
        with st.chat_message("user", avatar="🧑‍🎓"):
            st.markdown(user_prompt)
            
        with st.spinner("🤖 Kỹ Sư Trí Đức đang tư duy gợi ý cho bạn..."):
            reply, mode = ask_ai_tutor(user_prompt, current_lesson["title"])
            st.session_state[chat_key].append({"role": "assistant", "content": reply})
            with st.chat_message("assistant", avatar=robot_sticker):
                st.markdown(reply)
                if mode == "offline":
                    st.caption("*(Gợi ý Socratic Offline thông minh)*")
