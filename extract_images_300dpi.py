import os
import pypdfium2 as pdfium
from PIL import Image, ImageEnhance

PDF_PATH = "thuvienhoclieu.com-SGK-Cong-Nghe-Lop-8-thong-nhat.pdf"
RENDER_DIR = "temp_pages/render_300dpi"
OUT_IMG_DIR = "assets/images"

os.makedirs(RENDER_DIR, exist_ok=True)
os.makedirs(OUT_IMG_DIR, exist_ok=True)

def render_page_300dpi(pdf, page_idx):
    """
    Render a PDF page at 300 DPI.
    Standard PDF scale is 72 dpi -> scale = 300 / 72 = 4.1667
    """
    out_file = os.path.join(RENDER_DIR, f"page_{page_idx+1:03d}_300dpi.png")
    if os.path.exists(out_file):
        return Image.open(out_file)
    
    page = pdf[page_idx]
    image = page.render(scale=4.1667).to_pil()
    image.save(out_file, dpi=(300, 300))
    print(f"Rendered Page {page_idx+1} at 300 DPI: {image.size}")
    return image

def crop_and_enhance(img, box_rel, out_name):
    """
    box_rel: (left_ratio, top_ratio, right_ratio, bottom_ratio) in [0, 1]
    """
    w, h = img.size
    crop_box = (
        int(box_rel[0] * w),
        int(box_rel[1] * h),
        int(box_rel[2] * w),
        int(box_rel[3] * h)
    )
    cropped = img.crop(crop_box)
    
    # Tăng tương phản nhẹ để nét vẽ kỹ thuật rõ ràng 100%
    enhancer = ImageEnhance.Contrast(cropped)
    enhanced = enhancer.enhance(1.15)
    
    out_path = os.path.join(OUT_IMG_DIR, out_name)
    enhanced.save(out_path, dpi=(300, 300))
    print(f"Saved {out_name}: {enhanced.size}")
    return out_path

if __name__ == "__main__":
    pdf = pdfium.PdfDocument(PDF_PATH)
    print(f"Loaded PDF: {PDF_PATH}, total pages: {len(pdf)}")
