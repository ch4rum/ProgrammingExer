
import mysql.connector
from srcH.encrypt import EncryptPass

class ConnectDB:

    def __init__(self, username, password_b64, encryption_key):
        self.username = username
        self._encryption_key = encryption_key
        self.necrypt = EncryptPass(encryption_key)
        self._encrypted_password_b64 = self.necrypt.set_encrypt_pass(password_b64)
        self.con = self._conect_db()

    def _conect_db(self):
        decrypted_password = self.necrypt.get_decrypt_pass(self._encryption_key)
        if not decrypted_password:
            raise ValueError("La contraseña no se pudo descifrar correctamente.")
        conexion = mysql.connector.connect(
            host="localhost", 
            user=self.username,
            password=decrypted_password,
            charset="utf8mb4",  
            collation="utf8mb4_unicode_ci"
        )
        return conexion 

    def close(self):
        if self.con.is_connected():
            self.con.close()