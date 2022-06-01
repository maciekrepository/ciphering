from abc import ABC
import codecs
from buffer import Buffer

class Encrypt(ABC):
    def cipher(self, buffer_: Buffer):
        pass


class EncryptROT13(Encrypt):
    """Responsible for managing ROT13 encryption"""

    def cipher(self, buffer_: Buffer) -> str:
        encoded = codecs.encode(buffer_.decrypted, "rot_13")
        return "rot13" + encoded


class EncryptROT47(Encrypt):
    """Responsible for managing ROT47 encryption"""

    def cipher(self, buffer_: Buffer) -> str:
        text_to_encrypt_ = buffer_.decrypted
        x = []
        for i, z in enumerate(text_to_encrypt_):
            j = ord(text_to_encrypt_[i])
            if 33 <= j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(text_to_encrypt_[i])
        return "rot47" + "".join(x)
