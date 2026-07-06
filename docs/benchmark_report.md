# Báo cáo Đánh giá Hiệu năng & Bảo mật Hệ thống DRM

## 1. Thuật toán áp dụng
- **Mã hóa dữ liệu âm thanh:** Sử dụng thuật toán mã hóa đối xứng (XOR tuần hoàn) đảm bảo tốc độ stream nhạc thời gian thực.
- **Xác thực:** Kiểm tra ràng buộc với file đối soát tài chính `received_finance.txt`.

## 2. Kết quả kiểm thử an toàn thông tin
- Kiểm thử chỉ ra rằng người dùng không thể tự ý giải mã file nếu không được cấp phép.
- Mọi hành vi cố gắng truy cập trái phép đều được ghi vết tại file nhật ký hệ thống `security_audit.log`.