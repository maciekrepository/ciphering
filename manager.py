from encrypt import EncryptROT13, EncryptROT47
from decrypt import Decrypt
from file_operation import FileReadOperation, FileSaveOperation
from buffer import Buffer
from main_menu import MainMenu, SaveMenu, SelectEncodingMenu
from utils import EncodingOptions


class Manager:
    """
    Allows to initialize program, it takes a role of facade
    """

    def __init__(self) -> None:
        self.main_menu = MainMenu()
        self.save_menu = SaveMenu()
        self.encoding_menu = SelectEncodingMenu()
        self.buffer = Buffer()
        self.rot13 = EncryptROT13()
        self.rot47 = EncryptROT47()
        self.file_save_operation = FileSaveOperation()
        self.file_read_operation = FileReadOperation()
        self.type_of_encoding = None
        self.decrypt = Decrypt()
        self.options = {1: self.__do_cipher, 2: self.__do_decipher, 3: self.__do_exit}

        self.save_options = {
            1: self.file_save_operation.save_json,
            2: self.file_save_operation.save_txt,
        }
        self.select_encoding_options = {
            1: self.__do_cipher_rot13,
            2: self.__do_cipher_rot47,
        }

    def execute(self) -> None:
        """Executes selected option from main menu"""
        selected_option = self.main_menu.select_option()
        self.options.get(selected_option, self.error)()

    def __do_cipher(self) -> None:
        """Executes ciphering"""
        self.__enter_text()
        self.type_of_encoding = self.encoding_menu.select_option()
        if self.type_of_encoding == EncodingOptions.ENCRYPT_ROT13:
            self.__do_cipher_rot13()
        elif self.type_of_encoding == EncodingOptions.ENCRYPT_ROT47:
            self.__do_cipher_rot47()
        else:
            print("Nieprawidłowa wartość!")
            self.__do_cipher()

    def __do_cipher_rot13(self) -> None:
        """Pushes ciphered string into buffer"""
        self.buffer.encrypted = self.rot13.cipher(self.buffer)
        self.save_options.get(self.save_menu.select_option())(self.buffer)

    def __do_cipher_rot47(self) -> None:
        """Pushes ciphered string into buffer"""
        self.buffer.encrypted = self.rot47.cipher(self.buffer)
        self.save_options.get(self.save_menu.select_option())(self.buffer)

    def __enter_text(self) -> None:
        """Allows to enter text from console"""
        self.buffer.decrypted = input("Podaj tekst \n")

    def __do_decipher(self) -> None:
        """Read data from file, does decription and pushes result into buffer"""
        self.__read_file()
        self.buffer.decrypted = self.decrypt.decrypt(
            self.type_of_encoding, self.buffer.encrypted
        )
        print(self.buffer.decrypted)

    def __read_file(self) -> None:
        """Read data from file"""
        file = self.file_read_operation.file_read()
        self.buffer.encrypted = file["encrypted_text"]
        self.type_of_encoding = file["encoding"]

    def __do_exit(self) -> None:
        """Exits from application"""
        print("Wyszedłeś z programu")

    def error(self):
        print("Some error occured!")
