# FIT4012 - Gửi tập tin nhạc có bản quyền

## Thong Tin Nhom Thuc Hien - Nhom 08
* Truong nhom: Nguyen Tuan Anh - MSSV: 1871 - Lop: CNTT-1802
* Thanh vien: Nguyen Xuan Bach - MSSV: 1871020067 - Lop: CNTT-1802
* Thanh vien: Hoang The Truong - MSSV: 187 - Lop: CNTT-1802
* Thanh vien: Ha Van Viet - MSSV: 187 - Lop: CNTT-1802
**De tai 12:** DRM-like Secure Music Delivery
  **Hoc phan:** Nhap mon An toan va Bao mat thong tin
**De tai 12:** DRM-like Secure Music Delivery
**Don vi:** Dai hoc Dai Nam

---

##  Cấu trúc dự án
- `src/`: Mã nguồn cốt lõi gồm Server mã hóa, Key Server quản lý khóa, Client phát nhạc.
- `tests/`: Kịch bản kiểm thử mã hóa và tấn công thử nghiệm tự động.
- `sample_data/`: Nơi lưu trữ file nhạc gốc và file nhạc đã mã hóa DRM.
- `docs/`: Báo cáo phân tích hiệu năng và kiến trúc mật mã.
- `received_finance.txt`: Cơ sở dữ liệu giả lập để xác minh bản quyền người dùng.
- `security_audit.log`: Nhật ký ghi vết bảo mật hệ thống.

##  Cách chạy thử nghiệm nhanh
1. Mở terminal tại thư mục `tests/`
2. Chạy lệnh: `python test_security.py`
