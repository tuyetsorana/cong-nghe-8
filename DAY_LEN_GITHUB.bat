@echo off
chcp 65001 > nul
title Đẩy Dự Án Công Nghệ 8 Lên GitHub
echo ===================================================================
echo       CÔNG CỤ ĐẨY DỰ ÁN CÔNG NGHỆ 8 LÊN GITHUB TỰ ĐỘNG
echo ===================================================================
echo.

cd /d "%~dp0"

echo [1/3] Đang kiểm tra trạng thái Git trong thư mục dự án...
git status > nul 2>&1
if errorlevel 1 (
    echo [LỖI] Chưa có Git repository. Đang khởi tạo lại...
    git init
    git branch -M main
    git add .
    git commit -m "feat: Khoi tao Edu Tutor Streamlit Cong Nghe 8"
) else (
    echo [OK] Thư mục dự án đã sẵn sàng với nhánh main!
)

echo.
echo ===================================================================
echo HƯỚNG DẪN LẤY LINK GITHUB CỦA BẠN:
echo 1. Vào https://github.com/new tạo 1 repository mới (chọn Public).
echo 2. Sao chép (Copy) đường link màu xanh dạng:
echo    https://github.com/<ten-user>/<ten-repo>.git
echo ===================================================================
echo.
set /p REPO_URL=">>> Hãy DÁN (Paste) đường link GitHub của bạn vào đây rồi bấm Enter: "

if "%REPO_URL%"=="" (
    echo.
    echo [LỖI] Bạn chưa dán link GitHub! Vui lòng chạy lại file này.
    pause
    exit /b
)

echo.
echo [2/3] Đang kết nối với GitHub: %REPO_URL% ...
git remote remove origin > nul 2>&1
git remote add origin %REPO_URL%
git branch -M main

echo.
echo [3/3] Đang tải mã nguồn lên GitHub...
git push -u origin main

if errorlevel 1 (
    echo.
    echo ===================================================================
    echo [LƯU Ý] Nếu GitHub yêu cầu đăng nhập:
    echo - Hãy đăng nhập tài khoản GitHub trên cửa sổ trình duyệt hiện ra.
    echo - Hoặc dùng Personal Access Token nếu dùng mật khẩu.
    echo ===================================================================
) else (
    echo.
    echo ===================================================================
    echo 🎉 THÀNH CÔNG RỰC RỠ! Toàn bộ dự án đã được đưa lên GitHub!
    echo Bây giờ bạn có thể vào https://share.streamlit.io để Deploy lên Cloud!
    echo ===================================================================
)

echo.
pause
