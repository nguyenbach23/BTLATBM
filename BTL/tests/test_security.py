# tests/test_security.py
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
    
    print("\n[TEST 1] Kiểm tra người dùng hợp pháp:")
    play_drm_music("user_01", "SONG_MTP", "../sample_data/encrypted_song.bin")
    
    print("\n[TEST 2] Kiểm tra Hacker truy cập lậu:")
    play_drm_music("hacker_anonymous", "SONG_MTP", "../sample_data/encrypted_song.bin")

if __name__ == "__main__":
    run_security_test()