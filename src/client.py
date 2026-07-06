# src/client.py
import os
from key_server import verify_and_get_key

def play_drm_music(user_id, song_id, encrypted_song_path):
    print(f"\n--- Người dùng [{user_id}] đang yêu cầu nghe bài hát [{song_id}] ---")
    
    key, message = verify_and_get_key(user_id, song_id)
    
    log_file = os.path.join(os.path.dirname(__file__), "../security_audit.log")
    status = "SUCCESS" if key else "FAILED"
    with open(log_file, "a", encoding="utf-8") as l:
        l.write(f"[AUDIT] User: {user_id} | Song: {song_id} | Access: {status} | Reason: {message}\n")

    if not key:
        print(f"[Cảnh báo DRM]: {message}")
        return False

    with open(encrypted_song_path, "rb") as f:
        encrypted_data = f.read()
        
    decrypted_music = bytes(b ^ key[i % len(key)] for i, b in enumerate(encrypted_data))
    
    print(f"[Client]: {message}")
    print(f"🎵 Ứng dụng Player đang phát nhạc trực tuyến: '{decrypted_music.decode('utf-8')}'")
    return True