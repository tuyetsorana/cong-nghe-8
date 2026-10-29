@echo off
chcp 65001 > nul
title Web App Công Nghệ 8 • Kỹ Sư Trí Đức (Cổng 8505)
echo ===================================================================
echo   ĐANG KHỞI CHẠY WEB APP CÔNG NGHỆ 8 TRÊN CỔNG RIÊNG: 8505
echo ===================================================================
echo.
echo Cổng 8501 đang chạy ứng dụng Tiếng Anh của bạn.
echo Ứng dụng Công Nghệ 8 sẽ tự động mở tại: http://localhost:8505
echo.
cd /d "%~dp0"
start "" "http://localhost:8505"
streamlit run app.py --server.port 8505
if errorlevel 1 (
    echo.
    echo [LỖI] Đang thử bằng python -m streamlit...
    python -m streamlit run app.py --server.port 8505
)
pause
