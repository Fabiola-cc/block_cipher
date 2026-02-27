from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

from key_generation import generate_3des_key, generate_iv

def encrypt_3des_cbc(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Cifra usando 3DES-CBC.
    Devuelve ciphertext.
    """
    if len(key) not in (16, 24):
        raise ValueError("Clave 3DES debe ser de 16 o 24 bytes")
    
    # Crear cipher: DES3.new(key, DES3.MODE_CBC)
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)

    # Agregar padding para asegurar bloques múltiplo de 8 bytes
    padded = pad(plaintext, 8)

    # Cifrar mensaje
    ciphertext = iv + cipher.encrypt(padded)

    # Retornar
    return ciphertext


def decrypt_3des_cbc(ciphertext: bytes, key: bytes) -> bytes:
    """
    Descifra usando 3DES-CBC.
    Asume que el IV está en los primeros 8 bytes.
    """
    # Validar longitud de clave y IV
    if len(iv) != 8:
        raise ValueError("IV debe ser de 8 bytes")

    if len(key) not in (16, 24):
        raise ValueError("Clave 3DES debe ser de 16 o 24 bytes")
    
    iv_fromCipher = ciphertext[:8]
    ciphertext = ciphertext[8:]

    # Crear cipher
    decipher = DES3.new(key, DES3.MODE_CBC, iv=iv_fromCipher)
    
    # Descifrar
    decrypted = decipher.decrypt(ciphertext)

    # Eliminar padding y retornar
    return unpad(decrypted, 8)

if __name__ == "__main__":
    print("Ejemplo de cifrado: ")
    key = generate_3des_key(2)
    iv = generate_iv(8)
    plaintext = b"Mensaje secreto para 3DES"
    print(f"Mensaje original {plaintext}")

    cipher = encrypt_3des_cbc(plaintext, key, iv)
    print(f"Mensaje cifrado {cipher}")

    decipher = decrypt_3des_cbc(cipher, key)
    print(f"Mensaje descifrado {decipher}")