from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES


class AESEncryptor:
    def __init__(self, secretKey: str) -> None:
        self.secretKey = bytes(secretKey, "utf-8")
        self.iv = bytes("_w@?]`1p]3L9\@)q", "utf-8")

    def encrypt(self, plaintext: bytes) -> None:
        obj = AES.new(self.secretKey, AES.MODE_CBC, self.iv)
        self.cipherText = obj.encrypt(pad(plaintext, 16))

    def encryptFile(self, fileName: str) -> None:
        with open(fileName, 'rb') as f1:
            plaintext = b'ipf;' + bytes(
                fileName.split("/")[-1].split(".")[0],
                "utf-8") + b';.' + bytes(
                    fileName.split("/")[-1].split(".")[1], "utf-8") + b':-'
            plaintext += f1.read()
        self.encrypt(plaintext)

    def decrypt(self, cipherText: bytes) -> None:
        obj = AES.new(self.secretKey, AES.MODE_CBC, self.iv)
        self.plaintext = unpad(obj.decrypt(cipherText), 16)