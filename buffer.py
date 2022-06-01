from dataclasses import dataclass
@dataclass
class Buffer:
    '''Container for encrypted and decrypted data'''
    decrypted: str = None
    encrypted: str = None