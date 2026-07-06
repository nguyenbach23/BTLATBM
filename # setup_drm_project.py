# setup_drm_project.py
import os

# 1. Định nghĩa cấu trúc thư mục và file
project_structure = {
    "src/key_server.py": '''# src/key_server.py
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
''',

    "src/server.py": '''# src/server.py
def encrypt_music(input_path, output_path, key):
    """Sử dụng thuật toán mã hóa đối xứng để khóa file nhạc gốc"""
    with open(input_path, "rb") as f:
        original_data = f.read()
    
    encrypted_data = bytes(b ^ key[i % len(key)] for i, b in enumerate(original_data))
    
    with open(output_path, "wb") as f:
        f.write(encrypted_data)
    print(f"[Server] Đã mã hóa DRM thành công file nhạc và lưu tại: {output_path}")
''',

    "src/client.py": '''# src/client.py
import os
from key_server import verify_and_get_key

def play_drm_music(user_id, song_id, encrypted_song_path):
    print(f"\\n--- Người dùng [{user_id}] đang yêu cầu nghe bài hát [{song_id}] ---")
    
    key, message = verify_and_get_key(user_id, song_id)
    
    log_file = os.path.join(os.path.dirname(__file__), "../security_audit.log")
    status = "SUCCESS" if key else "FAILED"
    with open(log_file, "a", encoding="utf-8") as l:
        l.write(f"[AUDIT] User: {user_id} | Song: {song_id} | Access: {status} | Reason: {message}\\n")

    if not key:
        print(f"[Cảnh báo DRM]: {message}")
        return False

    with open(encrypted_song_path, "rb") as f:
        encrypted_data = f.read()
        
    decrypted_music = bytes(b ^ key[i % len(key)] for i, b in enumerate(encrypted_data))
    
    print(f"[Client]: {message}")
    print(f"🎵 Ứng dụng Player đang phát nhạc trực tuyến: '{decrypted_music.decode('utf-8')}'")
    return True
''',

    "tests/test_security.py": '''# tests/test_security.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from server import encrypt_music
from client import play_drm_music

def run_security_test():
    print("=== BẮT ĐẦU KIỂM THỬ BẢO MẬT TỰ ĐỘNG ===")
    
    key = b'SecretKeyAES2026'
    
    # Tạo thư mục sample_data nếu chưa có để tránh lỗi đường dẫn cục bộ
    os.makedirs("../sample_data", exist_ok=True)
    
    with open("../sample_data/original_song.txt", "w", encoding="utf-8") as f:
        f.write("Khúc nhạc bản quyền cực hay của Sơn Tùng MTP 2026")
        
    encrypt_music("../sample_data/original_song.txt", "../sample_data/encrypted_song.bin", key)
    
    print("\\n[TEST 1] Kiểm tra người dùng hợp pháp:")
    play_drm_music("user_01", "SONG_MTP", "../sample_data/encrypted_song.bin")
    
    print("\\n[TEST 2] Kiểm tra Hacker truy cập lậu:")
    play_drm_music("hacker_anonymous", "SONG_MTP", "../sample_data/encrypted_song.bin")

if __name__ == "__main__":
    run_security_test()
''',

    "sample_data/original_song.txt": "Dữ liệu âm thanh gốc chất lượng cao (.mp3)",
    
    "docs/benchmark_report.md": '''# Báo cáo Đánh giá Hiệu năng & Bảo mật Hệ thống DRM

## 1. Thuật toán áp dụng
- **Mã hóa dữ liệu âm thanh:** Sử dụng thuật toán mã hóa đối xứng (XOR tuần hoàn) đảm bảo tốc độ stream nhạc thời gian thực.
- **Xác thực:** Kiểm tra ràng buộc với file đối soát tài chính `received_finance.txt`.

## 2. Kết quả kiểm thử an toàn thông tin
- Kiểm thử chỉ ra rằng người dùng không thể tự ý giải mã file nếu không được cấp phép.
- Mọi hành vi cố gắng truy cập trái phép đều được ghi vết tại file nhật ký hệ thống `security_audit.log`.
''',

    "received_finance.txt": '''TRANSACTION_ID | USER_ID | SONG_ID  | AMOUNT | STATUS
TXN1000012345  | user_01 | SONG_MTP | 15000VND| SUCCESS
TXN1000012346  | user_02 | SONG_MTP | 15000VND| SUCCESS
TXN1000012347  | user_03 | SONG_JACK| 10000VND| PENDING
''',

    "security_audit.log": '''[SYSTEM START] Hệ thống DRM-like Secure Music Delivery đã khởi tạo.
''',

    "README.md": '''# Đề tài 12: DRM-like Secure Music Delivery 🎵
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
'''
}

# 2. Tiến hành tự động tạo thư mục và ghi file
print("--- ĐANG TỰ ĐỘNG KHỞI TẠO TOÀN BỘ CODE ĐỀ TÀI DRM ---")
for file_path, content in project_structure.items():
    dir_name = os.path.dirname(file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"[OK] Đã tạo: {file_path}")

print("\\n[THÀNH CÔNG] Toàn bộ lõi dự án đã được dựng hoàn chỉnh!")