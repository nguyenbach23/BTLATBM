# src/server.py
def encrypt_music(input_path, output_path, key):
    """Sử dụng thuật toán mã hóa đối xứng để khóa file nhạc gốc"""
    with open(input_path, "rb") as f:
        original_data = f.read()
    
    encrypted_data = bytes(b ^ key[i % len(key)] for i, b in enumerate(original_data))
    
    with open(output_path, "wb") as f:
        f.write(encrypted_data)
    print(f"[Server] Đã mã hóa DRM thành công file nhạc và lưu tại: {output_path}")