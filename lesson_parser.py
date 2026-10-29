import os
import re
import base64

def parse_lesson_sections(md_text):
    """
    Tách nội dung bài học thành 3 phân vùng chuẩn mực:
    - quick_notes (Thẻ 1: Ghi nhớ nhanh)
    - step_examples (Thẻ 2: Đọc bản vẽ & Thao tác kỹ thuật / Ví dụ mẫu)
    - sgk_content (Thẻ 3: Đọc thêm SGK)
    Nếu không có thẻ phân vùng, toàn bộ nội dung được đưa vào sgk_content.
    """
    sections = {
        "quick_notes": "",
        "step_examples": "",
        "sgk_content": ""
    }
    
    qn_match = re.search(r'<!-- SECTION: QUICK_NOTES -->(.*?)(?=<!-- SECTION: STEP_EXAMPLES -->|<!-- SECTION: SGK_CONTENT -->|$)', md_text, re.DOTALL)
    se_match = re.search(r'<!-- SECTION: STEP_EXAMPLES -->(.*?)(?=<!-- SECTION: SGK_CONTENT -->|$)', md_text, re.DOTALL)
    sgk_match = re.search(r'<!-- SECTION: SGK_CONTENT -->(.*?)$', md_text, re.DOTALL)
    
    if qn_match or se_match or sgk_match:
        if qn_match:
            sections["quick_notes"] = qn_match.group(1).strip()
        if se_match:
            sections["step_examples"] = se_match.group(1).strip()
        if sgk_match:
            sections["sgk_content"] = sgk_match.group(1).strip()
    else:
        # Fallback khi file chưa có thẻ phân vùng
        sections["quick_notes"] = "💡 *Nội dung tóm tắt đang được tối ưu hóa theo chuẩn 3 phân vùng.*"
        sections["step_examples"] = "🔍 *Các bước thao tác kỹ thuật và đọc bản vẽ chi tiết đang được cập nhật.*"
        sections["sgk_content"] = md_text.strip()
        
    return sections

def render_base64_images(md_text, image_dirs):
    """
    Thay thế đường dẫn ảnh Markdown bằng chuỗi Data URI Base64
    để hiển thị độc lập nền tảng, không lo đường dẫn tương đối lỗi trên Cloud.
    """
    if isinstance(image_dirs, str):
        image_dirs = [image_dirs]
        
    def replace_img(match):
        alt = match.group(1)
        rel_path = match.group(2)
        clean_name = os.path.basename(rel_path)
        
        # Tìm ảnh trong các thư mục được cung cấp
        for img_dir in image_dirs:
            if not os.path.exists(img_dir):
                continue
            full_path = os.path.join(img_dir, clean_name)
            if os.path.exists(full_path):
                try:
                    with open(full_path, "rb") as f:
                        encoded = base64.b64encode(f.read()).decode("utf-8")
                    ext = os.path.splitext(clean_name)[1].lower().replace(".", "")
                    if ext == "jpg": ext = "jpeg"
                    return f"![{alt}](data:image/{ext};base64,{encoded})"
                except Exception:
                    pass
        return match.group(0)

    pattern = r'!\[(.*?)\]\((.*?)\)'
    return re.sub(pattern, replace_img, md_text)
