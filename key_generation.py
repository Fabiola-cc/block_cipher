"""
Generador de claves criptográficamente seguras.
"""
import secrets

def generate_des_key():
    """
    Genera una clave DES aleatoria de 8 bytes (64 bits).
    Nota: DES usa efectivamente 56 bits (los otros 8 son de paridad),
    pero la clave es de 8 bytes.
    """
    return secrets.token_bytes(8)

def generate_3des_key(key_option: int = 2):
    """
    Genera una clave 3DES.
    
    key_option:
        2 → 16 bytes (K1, K2)
        3 → 24 bytes (K1, K2, K3)
    """
    if key_option == 2:
        return secrets.token_bytes(16)  # 2 claves DES
    elif key_option == 3:
        return secrets.token_bytes(24)  # 3 claves DES
    else:
        raise ValueError("key_option debe ser 2 o 3")
    
def generate_aes_key(key_size: int = 256):
    """
    Genera una clave AES aleatoria.
    
    key_size puede ser:
        128, 192, 256
    """
    if key_size not in (128, 192, 256):
        raise ValueError("AES solo permite 128, 192 o 256 bits")

    return secrets.token_bytes(key_size // 8)

def generate_iv(block_size: int = 8) -> bytes:
    """
    Genera un IV del tamaño del bloque.
    
    DES / 3DES → 8 bytes
    AES → 16 bytes
    """
    return secrets.token_bytes(block_size)
