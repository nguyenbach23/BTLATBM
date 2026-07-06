# src/key_server.py
import os

def verify_and_get_key(user_id, song_id):
    """Kiểm tra xem người dùng đã thanh toán mua nhạc chưa dựa trên file hóa đơn"""
    finance_file = os.path.join(os.path.dirname(__file__), "../received_finance.txt")
    
    if not os.path.exists(finance_file):
        return None, "Lỗi: Không tìm thấy cơ sở dữ liệu hóa đơn tài chính!"

    has_license = False
    with open(finance_file, "r", encoding="utf-8") as f:
        for line in f:
            if user_id in line and song_id in line and "SUCCESS" in line:
                has_license = True
                break

    if has_license:
        DRM_KEY = b'SecretKeyAES2026' # Khóa AES mô phỏng
        return DRM_KEY, "Xác thực thành công! Đã cấp bản quyền bản nhạc."
    else:
        return None, "Từ chối truy cập: Người dùng chưa thanh toán cho bài hát này!"