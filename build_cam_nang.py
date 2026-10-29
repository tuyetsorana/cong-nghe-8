import os
import re
import json
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CH1_DIR = os.path.join(BASE_DIR, "Chuong_01_Ve_Ky_Thuat")
IMG_DIR = os.path.join(CH1_DIR, "assets", "images")
PARETO_PATH = os.path.join(CH1_DIR, "data", "pareto_feynman_data.json")
TEMPLATE_PATH = r"G:\My Drive\0_HOME\GỠ RỐI AI\Qua Tang\SKILL GÓI D\SKILL GÓI D\skill ocr sach\skill ocr sach\metronic-html-publisher\assets\template-classic.html"
OUTPUT_PATH = os.path.join(BASE_DIR, "_CamNang_VI", "Cong_Nghe_8", "Chuong_01_Ve_Ky_Thuat.html")

def get_base64_image(filename):
    full_path = os.path.join(IMG_DIR, filename)
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        ext = os.path.splitext(filename)[1].lower().replace(".", "")
        if ext == "jpg": ext = "jpeg"
        return f"data:image/{ext};base64,{encoded}"
    return ""

def md_to_metronic_html(md_text):
    def img_repl(m):
        alt = m.group(1)
        src = os.path.basename(m.group(2))
        b64 = get_base64_image(src)
        if b64:
            return f'<figure class="illustration"><img src="{b64}" alt="{alt}" loading="lazy"><figcaption>{alt}</figcaption></figure>'
        return f'<p><em>[{alt}]</em></p>'
    
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', img_repl, md_text)
    
    html = re.sub(r'> \[!NOTE\]\s*\n((?:> .*\n?)+)', 
                  lambda m: f'<div class="callout callout-info"><div class="callout-title">📌 Ghi Nhớ Trọng Tâm</div>{m.group(1).replace("> ", "")}</div>', 
                  html)
    html = re.sub(r'> \[!IMPORTANT\]\s*\n((?:> .*\n?)+)', 
                  lambda m: f'<div class="callout callout-warning"><div class="callout-title">⚠️ Lưu Ý Quan Trọng</div>{m.group(1).replace("> ", "")}</div>', 
                  html)
    html = re.sub(r'> \[!TIP\]\s*\n((?:> .*\n?)+)', 
                  lambda m: f'<div class="callout callout-tip"><div class="callout-title">💡 Mẹo Kỹ Thuật</div>{m.group(1).replace("> ", "")}</div>', 
                  html)

    html = re.sub(r'^# (.*?)$', r'<h1 class="lesson-main-title">\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2 class="section-title">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3 class="subsection-title">\1</h3>', html, flags=re.MULTILINE)

    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Tables
    lines = html.split('\n')
    in_table = False
    table_lines = []
    new_lines = []
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            in_table = True
            table_lines.append(line.strip())
        else:
            if in_table:
                if len(table_lines) >= 2:
                    t_html = '<div class="table-wrap"><table class="data-table"><thead><tr>'
                    headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]
                    for h in headers:
                        t_html += f'<th>{h}</th>'
                    t_html += '</tr></thead><tbody>'
                    for r_line in table_lines[2:]:
                        t_html += '<tr>'
                        cols = [c.strip() for c in r_line.split('|')[1:-1]]
                        for c in cols:
                            t_html += f'<td>{c}</td>'
                        t_html += '</tr>'
                    t_html += '</tbody></table></div>'
                    new_lines.append(t_html)
                table_lines = []
                in_table = False
            new_lines.append(line)
            
    if in_table and len(table_lines) >= 2:
        t_html = '<div class="table-wrap"><table class="data-table"><thead><tr>'
        headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]
        for h in headers:
            t_html += f'<th>{h}</th>'
        t_html += '</tr></thead><tbody>'
        for r_line in table_lines[2:]:
            t_html += '<tr>'
            cols = [c.strip() for c in r_line.split('|')[1:-1]]
            for c in cols:
                t_html += f'<td>{c}</td>'
            t_html += '</tr>'
        t_html += '</tbody></table></div>'
        new_lines.append(t_html)

    body = '\n'.join(new_lines)
    
    paragraphs = body.split('\n\n')
    res_paragraphs = []
    for p in paragraphs:
        p_strip = p.strip()
        if not p_strip: continue
        if p_strip.startswith('<h') or p_strip.startswith('<div') or p_strip.startswith('<figure') or p_strip.startswith('<ul') or p_strip.startswith('<ol') or p_strip.startswith('<table'):
            res_paragraphs.append(p_strip)
        elif p_strip.startswith('- ') or p_strip.startswith('• ') or p_strip.startswith('1. '):
            items = [re.sub(r'^[-\•\d\.]+\s*', '', it.strip()) for it in p_strip.split('\n') if it.strip()]
            ul = '<ul class="list-bullet">' + ''.join([f'<li>{it}</li>' for it in items]) + '</ul>'
            res_paragraphs.append(ul)
        else:
            res_paragraphs.append(f'<p>{p_strip}</p>')

    return '\n'.join(res_paragraphs)

def build():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    pareto_dict = {}
    if os.path.exists(PARETO_PATH):
        with open(PARETO_PATH, "r", encoding="utf-8") as pf:
            pareto_dict = json.load(pf)

    lessons = [
        ("bai_01", "Bài 1: Một số tiêu chuẩn bản vẽ", "Bai_01.md"),
        ("bai_02", "Bài 2: Hình chiếu vuông góc", "Bai_02.md"),
        ("bai_03", "Bài 3: Bản vẽ chi tiết", "Bai_03.md"),
        ("bai_04", "Bài 4: Bản vẽ lắp", "Bai_04.md"),
        ("bai_05", "Bài 5: Bản vẽ nhà", "Bai_05.md"),
        ("on_tap", "Ôn tập tổng kết Chương I", "On_Tap_Chuong_01.md")
    ]

    toc_html = ""
    content_html = ""

    for l_id, l_title, l_file in lessons:
        toc_html += f'<li><a href="#{l_id}" class="toc-link">{l_title}</a></li>\n'
        
        md_path = os.path.join(CH1_DIR, "content", l_file)
        if os.path.exists(md_path):
            with open(md_path, "r", encoding="utf-8") as mf:
                raw_md = mf.read()
            rendered = md_to_metronic_html(raw_md)

            # Khối Pareto & Feynman chèn phía trên bài học
            p_info = pareto_dict.get(l_id, {})
            f_box = ""
            if p_info:
                p_items = "".join([f"<li><strong>Điểm cốt lõi #{i+1}:</strong> {item}</li>" for i, item in enumerate(p_info.get("pareto_20", []))])
                f_data = p_info.get("feynman_kid", {})
                f_box = f"""
                <div style="background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); border: 2px solid #fde68a; border-radius: 12px; padding: 16px 20px; margin-bottom: 20px;">
                    <h3 style="color: #b45309; margin-top: 0;">⚡ Bí Kíp Pareto 80/20 (20% Cốt Lõi Lấy Trọn Điểm 10)</h3>
                    <ul style="color: #78350f; line-height: 1.6; padding-left: 20px;">
                        {p_items}
                    </ul>
                </div>
                <div style="background: linear-gradient(135deg, #eff6ff 0%, #e0e7ff 100%); border: 2px solid #c7d2fe; border-radius: 12px; padding: 16px 20px; margin-bottom: 24px;">
                    <h3 style="color: #4338ca; margin-top: 0;">🧸 Góc Feynman: Giải Thích Cho Đứa Trẻ 10 Tuổi</h3>
                    <p style="font-weight: 700; color: #3730a3; margin-bottom: 8px;">{f_data.get('analogy_title', '')}</p>
                    <p style="color: #1e1b4b; line-height: 1.6;">{f_data.get('story', '')}</p>
                    <div style="background: #ffffff; border-left: 5px solid #ec4899; padding: 10px 14px; border-radius: 6px; font-weight: 700; color: #be185d; margin-top: 10px;">
                        💖 Thần chú 5 giây: {f_data.get('mantra', '')}
                    </div>
                </div>
                """

            content_html += f"""
            <section id="{l_id}" class="card lesson-section" style="margin-bottom: 2.5rem; padding: 2.2rem; border-radius: 16px;">
                {f_box}
                {rendered}
            </section>
            """

    out = template
    out = out.replace("{{BRAND}}", "CÔNG NGHỆ 8 • KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
    out = out.replace("{{TITLE}}", "Chương I: Vẽ Kĩ Thuật (Pareto 80/20 & Feynman)")
    out = out.replace("{{SUBTITLE}}", "Cẩm Nang Tự Học Sư Phạm Chuẩn TCVN — Phương Pháp Pareto 80/20 & Kỹ Thuật Feynman Trực Quan")
    out = out.replace("{{TAGS}}", '<span class="badge">TCVN 7285:2003</span> <span class="badge">Pareto 80/20</span> <span class="badge">Kỹ Thuật Feynman</span> <span class="badge">Hình Chiếu Vuông Góc</span>')
    out = out.replace("{{TOC}}", f'<ul class="toc-list">{toc_html}</ul>')
    out = out.replace("{{CONTENT}}", content_html)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as of:
        of.write(out)

    print(f"Successfully generated Metronic self-contained guide: {OUTPUT_PATH} ({os.path.getsize(OUTPUT_PATH) // 1024} KB)")

if __name__ == "__main__":
    build()
