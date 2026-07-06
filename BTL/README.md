# Đề tài 12: DRM-like Secure Music Delivery 🎵
Môn học: An toàn và Bảo mật thông tin

Hệ thống mô phỏng kiến trúc quản lý bản quyền số DRM (Digital Rights Management) giúp bảo vệ và phân phối các tập tin âm nhạc có bản quyền một cách an toàn.

## 📂 Cấu trúc dự án (Khớp chuẩn mẫu image_d07562.png)
- `src/`: Mã nguồn cốt lõi gồm Server mã hóa, Key Server quản lý khóa, Client phát nhạc.
- `tests/`: Kịch bản kiểm thử mã hóa và tấn công thử nghiệm tự động.
- `sample_data/`: Nơi lưu trữ file nhạc gốc và file nhạc đã mã hóa DRM.
- `docs/`: Báo cáo phân tích hiệu năng và kiến trúc mật mã.
- `received_finance.txt`: Cơ sở dữ liệu giả lập để xác minh bản quyền người dùng.
- `security_audit.log`: Nhật ký ghi vết bảo mật hệ thống.

## 🚀 Cách chạy thử nghiệm nhanh
1. Mở terminal tại thư mục `tests/`
2. Chạy lệnh: `python test_security.py`