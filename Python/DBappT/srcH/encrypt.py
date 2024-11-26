
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class EncryptPass:
    def __init__(self, encryption_key):
        self._encryption_key = encryption_key 
        self._encrypted_password_b64 = None 
        self._iv_b64 = None 

    def set_encrypt_pass(self, password_b64):
        self._encrypt_password(password_b64)

    def _encrypt_password(self, password_base64):
        iv = get_random_bytes(16)
        cipher = AES.new(self._encryption_key, AES.MODE_CBC, iv)
        encrypted_password = cipher.encrypt(pad(password_base64.encode('utf-8'), AES.block_size))

        self._encrypted_password_b64 = base64.b64encode(encrypted_password).decode('utf-8')
        self._iv_b64 = base64.b64encode(iv).decode('utf-8')
        #print(f"Encrypted Password (Base64): {self._encrypted_password_b64}")
        #print(f"IV (Base64): {self._iv_b64}")

    def get_decrypt_pass(self, encryption_key):
        return self._decrypt_password(encryption_key)

    def _decrypt_password(self, encryption_key):
        if encryption_key == self._encryption_key:
            iv = base64.b64decode(self._iv_b64)
            encrypted_password = base64.b64decode(self._encrypted_password_b64)

            cipher = AES.new(self._encryption_key, AES.MODE_CBC, iv)
            decrypted_password = unpad(cipher.decrypt(encrypted_password), AES.block_size)

            decrypted_password_base64 = decrypted_password.decode('utf-8')
            password = base64.b64decode(decrypted_password_base64).decode('utf-8')
            return password
        return None