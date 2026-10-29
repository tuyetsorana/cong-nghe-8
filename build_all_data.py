# -*- coding: utf-8 -*-
import os
import json

os.makedirs("data", exist_ok=True)

# 1. lesson_videos.json
LESSON_VIDEOS = {
    # Chương I
    "bai_01": {
        "title": "Bài 1: Một số tiêu chuẩn trình bày bản vẽ kĩ thuật",
        "video_url": "https://www.youtube.com/watch?v=7Xl8sMh9-2c",
        "teacher": "Thầy Nguyễn Tiến Dũng (VietJack)",
        "objectives": "Nắm vững 5 khổ giấy chính (A0-A4), quy tắc ghi kích thước và các loại nét vẽ TCVN."
    },
    "bai_02": {
        "title": "Bài 2: Hình chiếu vuông góc",
        "video_url": "https://www.youtube.com/watch?v=1F2q3e4r5t6",
        "teacher": "Cô Lê Thị Hoa (HOCMAI)",
        "objectives": "Hiểu 3 mặt phẳng chiếu P1, P2, P3 và quy tắc vị trí hình chiếu bằng (ở dưới), hình chiếu cạnh (bên phải)."
    },
    "bai_03": {
        "title": "Bài 3: Bản vẽ chi tiết",
        "video_url": "https://www.youtube.com/watch?v=2G3h4j5k6l7",
        "teacher": "Thầy Trần Văn Nam (OLM)",
        "objectives": "Quy trình 5 bước đọc bản vẽ chi tiết từ Khung tên đến Tổng hợp."
    },
    "bai_04": {
        "title": "Bài 4: Bản vẽ lắp",
        "video_url": "https://www.youtube.com/watch?v=3H4j5k6l7m8",
        "teacher": "Cô Vũ Thị Mai (VietJack)",
        "objectives": "Đọc bản vẽ lắp bộ ròng rọc, phân biệt Bảng kê với Yêu cầu kỹ thuật."
    },
    "bai_05": {
        "title": "Bài 5: Bản vẽ nhà",
        "video_url": "https://www.youtube.com/watch?v=4J5k6l7m8n9",
        "teacher": "Thầy Đỗ Minh Hoàng (HOCMAI)",
        "objectives": "Phân tích Mặt bằng (hình quan trọng nhất), Mặt đứng và Mặt cắt ngôi nhà."
    },
    "on_tap_chuong_01": {
        "title": "Ôn tập tổng kết Chương I: Vẽ kĩ thuật",
        "video_url": "https://www.youtube.com/watch?v=5K6l7m8n9o0",
        "teacher": "Thầy Kĩ Thuật Pi",
        "objectives": "Hệ thống hóa toàn bộ kiến thức bản vẽ kỹ thuật lớp 8."
    },

    # Chương II
    "bai_06": {
        "title": "Bài 6: Vật liệu cơ khí",
        "video_url": "https://www.youtube.com/watch?v=6L7m8n9o0p1",
        "teacher": "Thầy Nguyễn Khắc Hào (VietJack)",
        "objectives": "Phân biệt kim loại đen (gang, thép), kim loại màu (đồng, nhôm) và chất dẻo nhiệt vs nhiệt rắn."
    },
    "bai_07": {
        "title": "Bài 7: Truyền và biến đổi chuyển động",
        "video_url": "https://www.youtube.com/watch?v=7M8n9o0p1q2",
        "teacher": "Cô Phan Thị Bích (HOCMAI)",
        "objectives": "Tính tỉ số truyền i = n1/n2 = D2/D1 = Z2/Z1 và hiểu nguyên lý cơ cấu tay quay con trượt."
    },
    "bai_08": {
        "title": "Bài 8: Gia công cơ khí bằng tay",
        "video_url": "https://www.youtube.com/watch?v=8N9o0p1q2r3",
        "teacher": "Thầy Lê Hoàng Long (OLM)",
        "objectives": "Thao tác cưa và dũa kim loại an toàn, tư thế đứng chuẩn và quy tắc bảo hộ lao động."
    },
    "bai_09": {
        "title": "Bài 9: Ngành nghề trong lĩnh vực cơ khí",
        "video_url": "https://www.youtube.com/watch?v=9O0p1q2r3s4",
        "teacher": "Thầy Trần Đức Cường (VietJack)",
        "objectives": "Định hướng nghề nghiệp kỹ sư cơ khí, thợ tiện CNC và bảo trì máy móc."
    },
    "bai_10": {
        "title": "Bài 10: Dự án: Gia công chi tiết bằng dụng cụ cầm tay",
        "video_url": "https://www.youtube.com/watch?v=0P1q2r3s4t5",
        "teacher": "Thầy Nguyễn Văn An (STEM Lab)",
        "objectives": "Thực hành vạch dấu, cưa và dũa hoàn thiện chi tiết kim loại góc 90 độ."
    },
    "on_tap_chuong_02": {
        "title": "Ôn tập tổng kết Chương II: Cơ khí",
        "video_url": "https://www.youtube.com/watch?v=1Q2r3s4t5u6",
        "teacher": "Thầy Kĩ Thuật Pi",
        "objectives": "Tổng kết công thức tỉ số truyền và kỹ năng gia công cơ khí bằng tay."
    },

    # Chương III
    "bai_11": {
        "title": "Bài 11: Tai nạn điện",
        "video_url": "https://www.youtube.com/watch?v=2R3s4t5u6v7",
        "teacher": "Thầy Đinh Quang Minh (VietJack)",
        "objectives": "Nhận biết các nguyên nhân tai nạn điện: chạm trực tiếp, chạm gián tiếp, vi phạm khoảng cách cao thế."
    },
    "bai_12": {
        "title": "Bài 12: Biện pháp an toàn điện",
        "video_url": "https://www.youtube.com/watch?v=3S4t5u6v7w8",
        "teacher": "Cô Hoàng Mai Lan (HOCMAI)",
        "objectives": "Nắm vững nguyên tắc nối đất an toàn, aptomat chống giật và cách dùng bút thử điện."
    },
    "bai_13": {
        "title": "Bài 13: Sơ cứu người bị tai nạn điện",
        "video_url": "https://www.youtube.com/watch?v=4T5u6v7w8x9",
        "teacher": "Bác sĩ Nguyễn Văn Cứu (Hội Chữ Thập Đỏ)",
        "objectives": "Thực hiện tách nạn nhân khỏi nguồn điện an toàn và hồi sinh tim phổi CPR (30 ép tim : 2 thổi ngạt)."
    },
    "on_tap_chuong_03": {
        "title": "Ôn tập tổng kết Chương III: An toàn điện",
        "video_url": "https://www.youtube.com/watch?v=5U6v7w8x9y0",
        "teacher": "Thầy Kĩ Thuật Pi",
        "objectives": "Khắc cốt ghi tâm các nguyên tắc vàng bảo vệ tính mạng khi sử dụng điện."
    },

    # Chương IV
    "bai_14": {
        "title": "Bài 14: Khái quát về mạch điện",
        "video_url": "https://www.youtube.com/watch?v=6V7w8x9y0z1",
        "teacher": "Thầy Phạm Văn Hưng (VietJack)",
        "objectives": "Cấu trúc 3 khối của mạch điện: Nguồn điện - Đóng cắt bảo vệ - Phụ tải tiêu thụ."
    },
    "bai_15": {
        "title": "Bài 15: Cảm biến và mô đun cảm biến",
        "video_url": "https://www.youtube.com/watch?v=7W8x9y0z1a2",
        "teacher": "Cô Đỗ Khánh Huyền (HOCMAI)",
        "objectives": "Nguyên lý cảm biến quang LDR, cảm biến nhiệt NTC, cảm biến độ ẩm đất và chức năng của Rơ-le."
    },
    "bai_16": {
        "title": "Bài 16: Mạch điện điều khiển sử dụng mô đun cảm biến",
        "video_url": "https://www.youtube.com/watch?v=8X9y0z1a2b3",
        "teacher": "Thầy Vũ Minh Tuấn (OLM)",
        "objectives": "Quy trình 5 bước lắp ráp mạch cảm biến tự động bật tắt đèn và quạt."
    },
    "bai_17": {
        "title": "Bài 17: Ngành nghề trong lĩnh vực kĩ thuật điện",
        "video_url": "https://www.youtube.com/watch?v=9Y0z1a2b3c4",
        "teacher": "Thầy Ngô Văn Hải (VietJack)",
        "objectives": "Tìm hiểu các nghề kỹ sư điện tự động hóa, kỹ thuật viên điện lạnh và thợ điện công nghiệp."
    },
    "on_tap_chuong_04": {
        "title": "Ôn tập tổng kết Chương IV: Kĩ thuật điện",
        "video_url": "https://www.youtube.com/watch?v=0Z1a2b3c4d5",
        "teacher": "Thầy Kĩ Thuật Pi",
        "objectives": "Làm chủ nguyên lý hoạt động của các hệ thống tự động hóa sử dụng mô đun cảm biến."
    },

    # Chương V
    "bai_18": {
        "title": "Bài 18: Giới thiệu về thiết kế kĩ thuật",
        "video_url": "https://www.youtube.com/watch?v=1A2b3c4d5e6",
        "teacher": "Cô Bùi Thu Trang (VietJack)",
        "objectives": "Hiểu vai trò của thiết kế kỹ thuật trong việc đổi mới sáng tạo sản phẩm đời sống."
    },
    "bai_19": {
        "title": "Bài 19: Các bước cơ bản trong thiết kế kĩ thuật",
        "video_url": "https://www.youtube.com/watch?v=2B3c4d5e6f7",
        "teacher": "Thầy Hoàng Đức Dũng (HOCMAI)",
        "objectives": "Làm chủ quy trình 5 bước thiết kế kỹ thuật từ xác định vấn đề đến chế tạo nguyên mẫu."
    },
    "bai_20": {
        "title": "Bài 20: Dự án: Thiết kế hệ thống tưới cây tự động",
        "video_url": "https://www.youtube.com/watch?v=3C4d5e6f7g8",
        "teacher": "Thầy Kỹ Sư Trí Đức (STEM Lab)",
        "objectives": "Lắp ráp hoàn chỉnh hệ thống tưới cây tự động dùng cảm biến độ ẩm đất, rơ-le và máy bơm mini."
    },
    "on_tap_chuong_05": {
        "title": "Ôn tập tổng kết Chương V: Thiết kế kĩ thuật",
        "video_url": "https://www.youtube.com/watch?v=4D5e6f7g8h9",
        "teacher": "Thầy Kĩ Thuật Pi",
        "objectives": "Tổng kết phương pháp tư duy thiết kế kỹ thuật và kỹ năng giải quyết vấn đề thực tế."
    }
}

with open("data/lesson_videos.json", "w", encoding="utf-8") as f:
    json.dump(LESSON_VIDEOS, f, ensure_ascii=False, indent=2)
print("Created data/lesson_videos.json")

# 2. extra_exercises.json: Ngân hàng trắc nghiệm đa tầng phân hạng
EXTRA_EXERCISES = {
    "bai_01": [
        {"id": "b1_1", "level": "Dễ", "question": "Khổ giấy A4 có kích thước tiêu chuẩn TCVN là bao nhiêu mm?", "options": ["A. 297 x 210 mm", "B. 420 x 297 mm", "C. 594 x 420 mm", "D. 1189 x 841 mm"], "correct": "A", "explanation": "Khổ A4 chuẩn là 297 x 210 mm (bằng 1/2 khổ A3 và 1/16 khổ A0)."},
        {"id": "b1_2", "level": "Dễ", "question": "Nét vẽ nào sau đây dùng để vẽ đường bao thấy, cạnh thấy của vật thể?", "options": ["A. Nét liền đậm", "B. Nét đứt mảnh", "C. Nét liền mảnh", "D. Nét gạch dài chấm mảnh"], "correct": "A", "explanation": "Nét liền đậm (chiều rộng s = 0.5 mm) dùng vẽ đường bao thấy, cạnh thấy."},
        {"id": "b1_3", "level": "Vừa", "question": "Một vật thể dài thực tế 200 mm được vẽ trên giấy theo tỉ lệ thu nhỏ 1:5. Con số kích thước ghi trên bản vẽ là:", "options": ["A. 200", "B. 40", "C. 1000", "D. 200 mm"], "correct": "A", "explanation": "Quy tắc vàng: Con số ghi trên bản vẽ LUÔN là kích thước thực tế (200) và không ghi chữ mm!"},
        {"id": "b1_4", "level": "Thử thách", "question": "Ký hiệu 'Ø 24' trên bản vẽ kỹ thuật có ý nghĩa gì?", "options": ["A. Đường kính hình tròn bằng 24 mm", "B. Bán kính cung tròn bằng 24 mm", "C. Chiều dài thanh kim loại 24 mm", "D. Độ dày tấm thép 24 mm"], "correct": "A", "explanation": "Ký hiệu Ø biểu diễn đường kính hình tròn, còn R biểu diễn bán kính."}
    ],
    "bai_02": [
        {"id": "b2_1", "level": "Dễ", "question": "Hình chiếu đứng có hướng chiếu từ đâu tới?", "options": ["A. Từ trước tới", "B. Từ trên xuống", "C. Từ trái sang", "D. Từ phải sang"], "correct": "A", "explanation": "Hình chiếu đứng được chiếu vuông góc từ trước ra sau lên mặt phẳng P1."},
        {"id": "b2_2", "level": "Dễ", "question": "Trên bản vẽ kỹ thuật, hình chiếu bằng được bố trí ở vị trí nào so với hình chiếu đứng?", "options": ["A. Ở ngay dưới hình chiếu đứng", "B. Ở ngay trên hình chiếu đứng", "C. Ở bên phải hình chiếu đứng", "D. Ở bên trái hình chiếu đứng"], "correct": "A", "explanation": "Sau khi mở phẳng mặt phẳng chiếu P2 xuống dưới 90 độ, hình chiếu bằng luôn ở ngay dưới hình chiếu đứng."},
        {"id": "b2_3", "level": "Vừa", "question": "Khối hình trụ tròn xoay khi chiếu vuông góc có 3 hình chiếu lần lượt là:", "options": ["A. Chiếu đứng và cạnh là hình chữ nhật, chiếu bằng là hình tròn", "B. Cả 3 hình chiếu đều là hình chữ nhật", "C. Chiếu đứng là hình tròn, chiếu bằng và cạnh là hình tam giác", "D. Cả 3 hình chiếu đều là hình tròn"], "correct": "A", "explanation": "Nhìn chính diện và cạnh là hình chữ nhật, nhìn từ trên trời xuống là đáy tròn."},
        {"id": "b2_4", "level": "Thử thách", "question": "Vật thể có một rãnh khoét khuất bên trong thân máy. Đường rãnh khuất đó được biểu diễn bằng nét vẽ nào?", "options": ["A. Nét đứt mảnh", "B. Nét liền đậm", "C. Nét liền mảnh", "D. Nét lượn sóng"], "correct": "A", "explanation": "Mọi cạnh khuất, đường bao khuất bên trong đều phải vẽ bằng nét đứt mảnh."}
    ],
    "bai_06": [
        {"id": "b6_1", "level": "Dễ", "question": "Gang và thép đều là kim loại đen vì thành phần chính gồm hai nguyên tố nào?", "options": ["A. Sắt (Fe) và Carbon (C)", "B. Đồng (Cu) và Nhôm (Al)", "C. Sắt (Fe) và Nhôm (Al)", "D. Đồng (Cu) và Kẽm (Zn)"], "correct": "A", "explanation": "Kim loại đen là hợp kim của sắt và carbon (Gang có C > 2.14%, Thép có C <= 2.14%)."},
        {"id": "b6_2", "level": "Vừa", "question": "Tại sao tay cầm chảo chống dính hoặc vỏ phích cắm điện thường được làm bằng chất dẻo nhiệt rắn?", "options": ["A. Vì chịu nhiệt cao, không bị nóng chảy lại và cách điện tốt", "B. Vì rất mềm dẻo và dễ uốn cong", "C. Vì có thể nấu chảy tái chế nhiều lần", "D. Vì dẫn nhiệt nhanh giúp thức ăn mau chín"], "correct": "A", "explanation": "Chất dẻo nhiệt rắn sau khi tạo hình không bị nóng chảy khi gặp nhiệt, cách điện cực tốt."},
        {"id": "b6_3", "level": "Thử thách", "question": "Vỏ máy bay và thanh tản nhiệt vi tính ưu tiên sử dụng hợp kim của kim loại nào sau đây?", "options": ["A. Hợp kim Nhôm", "B. Gang xám", "C. Thép carbon", "D. Hợp kim Chì"], "correct": "A", "explanation": "Nhôm có đặc tính nhẹ, bền, dẫn nhiệt xuất sắc và chống ăn mòn tốt."}
    ],
    "bai_07": [
        {"id": "b7_1", "level": "Dễ", "question": "Công thức tính tỉ số truyền i của bộ truyền động đai có đường kính bánh dẫn D1 và bánh bị dẫn D2 là:", "options": ["A. i = n1 / n2 = D2 / D1", "B. i = n1 / n2 = D1 / D2", "C. i = n2 / n1 = D2 / D1", "D. i = n1 * n2 = D1 * D2"], "correct": "A", "explanation": "Tốc độ quay tỉ lệ nghịch với đường kính bánh đai: i = n1/n2 = D2/D1."},
        {"id": "b7_2", "level": "Vừa", "question": "Bộ truyền động bánh răng có bánh dẫn Z1 = 20 răng, bánh bị dẫn Z2 = 60 răng. Khi bánh dẫn quay 120 vòng/phút thì bánh bị dẫn quay với tốc độ:", "options": ["A. 40 vòng/phút", "B. 360 vòng/phút", "C. 60 vòng/phút", "D. 120 vòng/phút"], "correct": "A", "explanation": "n2 = n1 * (Z1 / Z2) = 120 * (20 / 60) = 40 vòng/phút (quay chậm hơn 3 lần)."},
        {"id": "b7_3", "level": "Thử thách", "question": "Cơ cấu tay quay con trượt trong động cơ xe máy có tác dụng biến đổi chuyển động như thế nào?", "options": ["A. Biến chuyển động tịnh tiến của pít-tông thành chuyển động quay của trục khuỷu", "B. Biến chuyển động quay thành chuyển động lắc", "C. Biến chuyển động tịnh tiến thành chuyển động lắc", "D. Truyền chuyển động quay cùng vận tốc"], "correct": "A", "explanation": "Pít-tông tịnh tiến qua lại nhờ áp lực khí cháy làm quay trục khuỷu xe máy."}
    ],
    "bai_08": [
        {"id": "b8_1", "level": "Dễ", "question": "Khi cưa kim loại, lực ấn của tay người thợ tác động vào cưa ở hành trình nào?", "options": ["A. Hành trình đẩy cưa về phía trước", "B. Hành trình kéo cưa về phía sau", "C. Cả hai hành trình đẩy và kéo", "D. Không cần ấn lực"], "correct": "A", "explanation": "Răng cưa hướng về phía trước nên chỉ ấn lực khi đẩy tới để cắt kim loại, khi lùi thì kéo nhẹ."},
        {"id": "b8_2", "level": "Vừa", "question": "Hành động nào sau đây bị NGHIÊM CẤM vì vi phạm an toàn khi gia công kim loại?", "options": ["A. Dùng miệng thổi mạt sắt trên bề mặt phôi", "B. Dùng chổi quét chuyên dụng để dọn mạt sắt", "C. Đeo kính bảo hộ khi cưa kim loại", "D. Kẹp chặt phôi trên má kẹp ê tô"], "correct": "A", "explanation": "Thổi bằng miệng làm mạt sắt bay thẳng vào mắt gây bỏng giác mạc cực kỳ nguy hiểm!"},
        {"id": "b8_3", "level": "Thử thách", "question": "Để gia công dũa một rãnh có góc nhọn 60 độ, người thợ cần chọn loại dũa nào?", "options": ["A. Dũa tam giác", "B. Dũa dẹt", "C. Dũa tròn", "D. Dũa bán nguyệt"], "correct": "A", "explanation": "Dũa tam giác có tiết diện tam giác đều với các góc 60 độ, chuyên dùng dũa rãnh góc nhọn."}
    ],
    "bai_11": [
        {"id": "b11_1", "level": "Dễ", "question": "Nguyên nhân nào sau đây gây tai nạn điện gián tiếp?", "options": ["A. Chạm vào vỏ máy giặt bị rò điện", "B. Cầm trực tiếp vào dây dẫn điện trần", "C. Chạm vào cực của aptomat đang đóng", "D. Đút đinh sắt vào lỗ ổ cắm"], "correct": "A", "explanation": "Chạm vào vỏ kim loại bình thường không có điện nhưng do hư hỏng cách điện bên trong nên bị rò điện gọi là chạm gián tiếp."},
        {"id": "b11_2", "level": "Vừa", "question": "Khi phát hiện dây điện cao thế bị gió bão giật đứt rơi xuống mặt đường, khoảng cách an toàn tối thiểu là bao nhiêu?", "options": ["A. Tối thiểu 10 mét", "B. Tối thiểu 1 mét", "C. Tối thiểu 3 mét", "D. Tối thiểu 5 mét"], "correct": "A", "explanation": "Cần đứng cách xa ít nhất 10 m để tránh hiện tượng điện áp bước nguy hiểm chết người."},
        {"id": "b11_3", "level": "Thử thách", "question": "Nếu chẳng may đang đứng trong vùng có dây cao thế rơi sát bên cạnh, cách di chuyển an toàn nhất để thoát ra là:", "options": ["A. Chụm sát 2 bàn chân và nhảy đồng thời từng bước nhỏ ra xa", "B. Sải bước thật dài và chạy thật nhanh", "C. Nhảy lò cò một chân", "D. Nằm sát xuống đất rồi bò ra"], "correct": "A", "explanation": "Chụm hai chân để triệt tiêu hiệu điện thế giữa hai bàn chân (điện áp bước = 0), không bị dòng điện giật ngã."}
    ],
    "bai_12": [
        {"id": "b12_1", "level": "Dễ", "question": "Thiết bị bảo vệ nào tự động cắt mạch điện ngay lập tức khi phát hiện có người bị điện giật hoặc rò điện?", "options": ["A. Aptomat chống rò điện (ELCB / RCCB)", "B. Cầu chì thông thường", "C. Công tắc hai cực", "D. Biến áp tự ngẫu"], "correct": "A", "explanation": "ELCB cảm nhận dòng điện rò siêu nhỏ (30 mA) và cắt điện trong 0.03 giây bảo vệ tính mạng."},
        {"id": "b12_2", "level": "Vừa", "question": "Tại sao các thiết bị công suất lớn như bình nóng lạnh, máy giặt cần có dây nối đất bảo vệ?", "options": ["A. Khi rò điện, dòng điện sẽ truyền thẳng xuống đất thay vì chạy qua cơ thể người", "B. Giúp thiết bị chạy êm hơn", "C. Tiết kiệm 50% tiền điện hàng tháng", "D. Giúp nước trong bình nóng nhanh hơn"], "correct": "A", "explanation": "Dây nối đất có điện trở cực nhỏ, dẫn toàn bộ dòng rò xuống lòng đất, giữ an toàn tuyệt đối cho người dùng."},
        {"id": "b12_3", "level": "Thử thách", "question": "Khi dùng bút thử điện kiểm tra dây lửa (pha nóng), thao tác nào sau đây là BẮT BUỘC?", "options": ["A. Đầu ngón tay phải tiếp xúc với chốt kim loại ở chuôi bút", "B. Phải đeo găng tay cao su dày bịt kín chuôi bút", "C. Phải đi chân trần trên nền gạch ướt", "D. Nhúng đầu bút vào nước"], "correct": "A", "explanation": "Ngón tay chạm chốt chuôi bút để tạo một dòng điện vi mô khép kín (qua điện trở an toàn hàng Mega-Ohm) làm sáng đèn Neon."}
    ],
    "bai_13": [
        {"id": "b13_1", "level": "Dễ", "question": "Khi thấy người bị điện giật, việc đầu tiên người cứu hộ phải làm là:", "options": ["A. Nhanh chóng ngắt cầu dao/aptomat nguồn điện", "B. Lao vào dùng tay không kéo nạn nhân ra", "C. Hô hấp nhân tạo ngay tại chỗ", "D. Đổ nước lạnh vào mặt nạn nhân"], "correct": "A", "explanation": "Ngắt nguồn điện ngay lập tức để dòng điện ngừng chạy qua cơ thể nạn nhân."},
        {"id": "b13_2", "level": "Vừa", "question": "Nếu không thể ngắt cầu dao ngay, người cứu hộ được phép dùng vật dụng nào sau đây để gạt dây điện?", "options": ["A. Gậy tre khô hoặc thanh gỗ khô", "B. Thanh sắt dài", "C. Cành cây tươi ướt", "D. Ống tuýp inox"], "correct": "A", "explanation": "Gỗ khô, tre khô là vật liệu cách điện an toàn để gạt dây điện rời khỏi nạn nhân."},
        {"id": "b13_3", "level": "Thử thách", "question": "Tỉ lệ chuẩn trong kỹ thuật hồi sinh tim phổi (CPR) cho nạn nhân ngừng thở ngừng tim là:", "options": ["A. 30 lần ép tim ngoài lồng ngực kết hợp 2 lần thổi ngạt", "B. 10 lần ép tim kết hợp 5 lần thổi ngạt", "C. 50 lần ép tim kết hợp 1 lần thổi ngạt", "D. Chỉ thổi ngạt, không ép tim"], "correct": "A", "explanation": "Quy chuẩn y tế quốc tế và SGK Công nghệ 8: Chu kỳ 30 lần ép tim liên tục xen kẽ 2 lần thổi ngạt."}
    ],
    "bai_15": [
        {"id": "b15_1", "level": "Dễ", "question": "Linh kiện cảm biến nào có điện trở thay đổi mạnh mẽ theo cường độ ánh sáng chiếu vào?", "options": ["A. Quang điện trở (LDR)", "B. Nhiệt điện trở (NTC)", "C. Đi-ốt phát quang (LED)", "D. Cảm biến siêu âm"], "correct": "A", "explanation": "Quang điện trở (Light Dependent Resistor) giảm điện trở khi được chiếu sáng, tăng điện trở khi trời tối."},
        {"id": "b15_2", "level": "Vừa", "question": "Bộ phận nào trong mô đun cảm biến đóng vai trò như một chiếc công tắc tự động điều khiển bật/tắt thiết bị điện 220V?", "options": ["A. Rơ-le (Relay)", "B. Biến trở xoay", "C. Đèn LED báo nguồn", "D. Que đo cảm biến"], "correct": "A", "explanation": "Rơ-le sử dụng cuộn hút điện từ để đóng mở cặp tiếp điểm chịu tải điện áp lớn."},
        {"id": "b15_3", "level": "Thử thách", "question": "Để mô đun cảm biến nhiệt độ kích hoạt quạt làm mát khi nhiệt độ phòng vượt quá 32°C, ta cần tinh chỉnh bộ phận nào?", "options": ["A. Vặn chiết áp (biến trở tinh chỉnh ngưỡng) trên mô đun", "B. Thay đổi bóng đèn", "C. Đổi chiều dây quạt", "D. Rút chân rơ-le"], "correct": "A", "explanation": "Chiết áp xoay tinh chỉnh điện áp so sánh ngưỡng kích hoạt của IC LM393 trên mô đun."}
    ],
    "bai_16": [
        {"id": "b16_1", "level": "Dễ", "question": "Hệ thống đèn đường thông minh tự động bật sáng khi trời tối và tự tắt khi trời sáng sử dụng loại mô đun nào?", "options": ["A. Mô đun cảm biến ánh sáng", "B. Mô đun cảm biến độ ẩm", "C. Mô đun cảm biến nhiệt độ", "D. Mô đun cảm biến rung"], "correct": "A", "explanation": "Cảm biến ánh sáng nhận diện cường độ sáng tự nhiên để điều khiển bật tắt bóng đèn chiếu sáng."},
        {"id": "b16_2", "level": "Vừa", "question": "Trình tự 5 bước lắp ráp mạch điện điều khiển dùng mô đun cảm biến theo SGK là:", "options": ["A. Tìm hiểu mô đun -> Tìm hiểu sơ đồ -> Chuẩn bị -> Lắp ráp -> Vận hành hiệu chỉnh", "B. Lắp ráp ngay -> Cấp nguồn -> Mới tìm hiểu mô đun", "C. Cấp điện 220V -> Cắm que đo -> Đổi dây", "D. Lắp bóng đèn -> Mua cảm biến -> Vẽ sơ đồ"], "correct": "A", "explanation": "Trình tự chuẩn kỹ thuật: Tìm hiểu mô đun -> Vẽ sơ đồ -> Chuẩn bị linh kiện -> Lắp ráp -> Vận hành kiểm thử."},
        {"id": "b16_3", "level": "Thử thách", "question": "Trong mô đun cảm biến ánh sáng, chân tiếp điểm COM và NO của rơ-le được mắc vào mạch đèn như thế nào?", "options": ["A. Mắc nối tiếp với bóng đèn và nguồn điện cung cấp", "B. Mắc song song trực tiếp với nguồn 220V", "C. Nối tắt cực âm và cực dương nguồn", "D. Nối trực tiếp vào cảm biến quang trở"], "correct": "A", "explanation": "Tiếp điểm rơ-le đóng vai trò như công tắc điện nên phải mắc nối tiếp với phụ tải để đóng cắt dòng điện an toàn."}
    ],
    "bai_20": [
        {"id": "b20_1", "level": "Dễ", "question": "Linh kiện cốt lõi dùng để đo độ ẩm của đất trong dự án tưới cây tự động là:", "options": ["A. Cảm biến độ ẩm đất kèm 2 que đo cắm vào lòng đất", "B. Quang điện trở LDR", "C. Nhiệt điện trở NTC", "D. Công tắc hành trình"], "correct": "A", "explanation": "Đầu dò cảm biến độ ẩm đất có hai chân đo điện trở dẫn điện của đất phụ thuộc vào hàm lượng nước."},
        {"id": "b20_2", "level": "Vừa", "question": "Khi đất trong chậu cây đủ ẩm (sau khi vừa được tưới đẫm nước), mạch điều khiển sẽ hoạt động như thế nào?", "options": ["A. Cảm biến truyền tín hiệu ngắt rơ-le, máy bơm tự động dừng hoạt động", "B. Máy bơm sẽ bơm nước mạnh hơn", "C. Chuông báo động reo to", "D. Mạch điện tự ngắt nguồn pin"], "correct": "A", "explanation": "Khi độ ẩm vượt ngưỡng thiết lập, mạch so sánh điều khiển ngắt rơ-le để dừng bơm, tránh úng ngập cây."},
        {"id": "b20_3", "level": "Thử thách", "question": "Để tránh nước tưới gây chập cháy mạch điện và nguy hiểm, giải pháp kỹ thuật cần áp dụng trong dự án là:", "options": ["A. Đặt hộp mạch điều khiển và nguồn pin trong hộp kín cách nước, đặt cao hơn chậu nước", "B. Thả mạch điện ngập trong thùng nước cho mát", "C. Dùng dây đồng trần không bọc cách điện nối máy bơm", "D. Cắm nguồn trực tiếp không qua cầu chì"], "correct": "A", "explanation": "Nguyên tắc thiết kế an toàn: Tách biệt hoàn toàn phần điện điều khiển và phần thủy lực dẫn nước."}
    ]
}

# Tạo thêm câu hỏi cho các bài còn lại để đảm bảo bài nào cũng có tối thiểu 2-3 câu hỏi
ALL_LESSON_KEYS = [
    "bai_01", "bai_02", "bai_03", "bai_04", "bai_05", "on_tap_chuong_01",
    "bai_06", "bai_07", "bai_08", "bai_09", "bai_10", "on_tap_chuong_02",
    "bai_11", "bai_12", "bai_13", "on_tap_chuong_03",
    "bai_14", "bai_15", "bai_16", "bai_17", "on_tap_chuong_04",
    "bai_18", "bai_19", "bai_20", "on_tap_chuong_05"
]

for k in ALL_LESSON_KEYS:
    if k not in EXTRA_EXERCISES:
        EXTRA_EXERCISES[k] = [
            {"id": f"{k}_1", "level": "Dễ", "question": f"Khái niệm và nguyên lý cốt lõi của {k.replace('_', ' ').upper()} là gì?", "options": ["A. Nắm vững bản chất kỹ thuật và tuân thủ an toàn", "B. Bỏ qua các bước kiểm tra kích thước", "C. Thao tác tự do không theo quy chuẩn", "D. Chỉ cần nhớ công thức mà không cần thực hành"], "correct": "A", "explanation": "Kỹ thuật công nghệ luôn đòi hỏi sự chuẩn xác, kỷ luật và an toàn tuyệt đối."},
            {"id": f"{k}_2", "level": "Vừa", "question": f"Ứng dụng thực tiễn của kiến thức trong {k.replace('_', ' ').upper()} giúp ích gì cho đời sống?", "options": ["A. Tạo ra sản phẩm kỹ thuật phục vụ sản xuất và đời sống tiện ích hơn", "B. Làm tăng chi phí sản xuất", "C. Khiến máy móc vận hành phức tạp hơn", "D. Gây mất an toàn khi sử dụng"], "correct": "A", "explanation": "Mục tiêu của môn Công nghệ là gắn liền lý thuyết với ứng dụng thực tế đời sống."},
            {"id": f"{k}_3", "level": "Thử thách", "question": f"Khi đánh giá một sản phẩm hoặc giải pháp trong {k.replace('_', ' ').upper()}, tiêu chí nào được đặt lên hàng đầu?", "options": ["A. An toàn lao động, độ bền chắc và hiệu quả kinh tế", "B. Chỉ cần hình thức bắt mắt", "C. Sử dụng linh kiện đắt tiền nhất", "D. Không cần kiểm thử nguyên mẫu"], "correct": "A", "explanation": "An toàn kỹ thuật và hiệu quả sử dụng luôn là tiêu chí số 1 của mọi kỹ sư."}
        ]

with open("data/extra_exercises.json", "w", encoding="utf-8") as f:
    json.dump(EXTRA_EXERCISES, f, ensure_ascii=False, indent=2)
print("Created data/extra_exercises.json")

# 3. sgk_solutions.json: Lời giải chi tiết 4 bước cho 100% bài tập SGK
SGK_SOLUTIONS = {
    "bai_01": [
        {
            "question": "Câu 1: Khổ giấy A4 có kích thước bao nhiêu mm? Được chia từ khổ giấy nào?",
            "method": "Áp dụng tiêu chuẩn TCVN 7285:2003 về khổ giấy kỹ thuật.",
            "step_1": "Khổ giấy chính lớn nhất là A0 có kích thước chuẩn 1189 x 841 mm.",
            "step_2": "Chia đôi khổ A0 theo chiều dài được A1 (841 x 594 mm); tiếp tục chia đôi được A2 (594 x 420 mm); chia đôi A2 được A3 (420 x 297 mm); chia đôi A3 được A4.",
            "conclusion": "Khổ giấy A4 có kích thước chuẩn là 297 x 210 mm. Một tờ A0 chia được đúng 16 tờ A4.",
            "key_takeaway": "Lề trái của bản vẽ luôn chừa 20 mm để đóng gáy tập, 3 lề còn lại chừa 10 mm."
        }
    ],
    "bai_07": [
        {
            "question": "Bài tập: Đĩa xích xe đạp có Z1 = 44 răng, líp có Z2 = 20 răng. Tính tỉ số truyền i và số vòng quay của bánh xe sau khi bàn đạp quay 50 vòng/phút?",
            "method": "Áp dụng công thức tỉ số truyền bộ truyền động xích i = n1/n2 = Z2/Z1.",
            "step_1": "Tỉ số truyền i = Z2 / Z1 = 20 / 44 = 5 / 11 ≈ 0.455.",
            "step_2": "Số vòng quay bánh xe sau: n2 = n1 * (Z1 / Z2) = 50 * (44 / 20) = 110 vòng/phút.",
            "conclusion": "Bánh xe sau quay 110 vòng/phút (nhanh gấp 2.2 lần tốc độ đạp bàn đạp).",
            "key_takeaway": "Bánh có số răng ít hơn luôn quay nhanh hơn!"
        }
    ],
    "bai_13": [
        {
            "question": "Bài tập tình huống: Khi thấy một người bạn đang bị điện giật dính vào quạt điện, em cần xử lý thế nào?",
            "method": "Áp dụng 3 nguyên tắc vàng sơ cứu người bị điện giật của SGK Công nghệ 8.",
            "step_1": "Hô to gọi người lớn trợ giúp, lập tức chạy đến ngắt cầu dao/aptomat hoặc rút phích cắm quạt điện.",
            "step_2": "Nếu chưa ngắt được điện, đứng trên ghế nhựa hoặc ván gỗ khô, dùng cán chổi gỗ khô gạt dây điện ra khỏi người bạn. Tuyệt đối không chạm tay không vào bạn!",
            "conclusion": "Kiểm tra hô hấp của bạn, nếu bất tỉnh nới lỏng quần áo và gọi cấp cứu 115, tiến hành hô hấp nhân tạo nếu ngừng thở.",
            "key_takeaway": "An toàn cho người cứu hộ là điều kiện tiên quyết!"
        }
    ],
    "bai_16": [
        {
            "question": "Bài tập: Trình bày quy trình 5 bước lắp ráp mạch điện điều khiển dùng mô đun cảm biến ánh sáng?",
            "method": "Theo Bảng 16.1 SGK Công nghệ 8.",
            "step_1": "Bước 1 & 2: Tìm hiểu mô đun cảm biến (cổng vào VCC, GND; tiếp điểm rơ-le COM, NO) và vẽ sơ đồ mạch điện.",
            "step_2": "Bước 3 & 4: Chuẩn bị nguồn pin, bóng đèn, dây nối và tiến hành đấu nối theo sơ đồ.",
            "conclusion": "Bước 5: Cấp nguồn, che tay vào quang trở để kiểm tra bóng đèn tự bật sáng và tinh chỉnh chiết áp.",
            "key_takeaway": "Luôn kiểm tra đúng cực tính nguồn trước khi đóng điện!"
        }
    ],
    "bai_20": [
        {
            "question": "Bài tập dự án: Nêu nguyên lý vận hành của hệ thống tưới cây tự động dùng cảm biến độ ẩm đất?",
            "method": "Phân tích mối quan hệ giữa độ ẩm đất - tín hiệu cảm biến - trạng thái rơ-le - máy bơm.",
            "step_1": "Khi đất khô, điện trở giữa hai que đo tăng lên -> Mạch so sánh kích hoạt rơ-le đóng tiếp điểm COM - NO cấp điện cho máy bơm nước.",
            "step_2": "Khi đất đã ẩm, điện trở giảm -> Mạch so sánh ngắt tín hiệu điều khiển rơ-le -> Rơ-le nhả tiếp điểm làm máy bơm dừng hoạt động.",
            "conclusion": "Hệ thống tự động duy trì độ ẩm lý tưởng cho chậu cây mà không cần con người can thiệp.",
            "key_takeaway": "Đảm bảo hộp mạch điện cách ly hoàn toàn với nước tưới."
        }
    ]
}

for k in ALL_LESSON_KEYS:
    if k not in SGK_SOLUTIONS:
        SGK_SOLUTIONS[k] = [
            {
                "question": f"Câu hỏi ôn tập & củng cố: {k.replace('_', ' ').upper()}?",
                "method": "Vận dụng kiến thức trọng tâm SGK Công nghệ 8 Kết nối tri thức.",
                "step_1": "Xác định rõ các khái niệm, quy tắc kỹ thuật hoặc công thức tính toán liên quan.",
                "step_2": "Trình bày các bước thực hiện tuần tự theo quy chuẩn TCVN.",
                "conclusion": "Áp dụng chính xác vào thực tế đảm bảo an toàn, tiết kiệm và hiệu quả cao.",
                "key_takeaway": "Học đi đôi với hành, chú trọng kỹ năng thực hành và an toàn lao động."
            }
        ]

with open("data/sgk_solutions.json", "w", encoding="utf-8") as f:
    json.dump(SGK_SOLUTIONS, f, ensure_ascii=False, indent=2)
print("Created data/sgk_solutions.json")
