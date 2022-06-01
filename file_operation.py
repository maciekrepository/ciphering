import json
import os
from buffer import Buffer
import sys


class FileSaveOperation:
    """Saves encrypted string into JSON or txt"""

    @staticmethod
    def save_txt(buffer_: Buffer) -> None:
        with open("./ciphered_txt/ciphered.txt", "w", encoding="utf-8") as file:
            file.write(buffer_.encrypted)
            file.close()

    def save_json(self, buffer_: Buffer) -> None:
        json_dict = {"data": buffer_.encrypted}
        with open("./ciphered_json/ciphered.json", "w", encoding="utf-8") as outfile:
            json.dump(json_dict, outfile)




class FileReadOperation:
    """Reads data from file"""

    def __init__(self) -> None:
        self.file_name = None
        self.content = None
        self.encoding = None
        self.encrypted_text = None

    def file_name_check(self) -> None:
        """Checks if there is only one file to decrypt and if the file has correct format"""
        decrypt_address = "./to_decrypt"
        files = os.listdir(decrypt_address)
        if len(files) == 1:
            if files[0].endswith((".txt", ".json")):
                self.file_name = files[0]
            else:
                print("Nieprawidlowy plik do odszyfrowania")
                sys.exit()
        else:
            print("W katalogu musi znajdować się 1 plik do deszyfracji")
            sys.exit()

    def get_content(self) -> None:
        """Gets data from file"""
        with open("./to_decrypt/" + self.file_name, encoding="utf-8") as file:
            if self.file_name.endswith(".txt"):
                file_content = file.read()
            elif self.file_name.endswith(".json"):
                file = json.load(file)
                file_content = file["data"]
            else:
                print("Błąd")
                sys.exit()

            self.encoding = file_content[:5]
            self.encrypted_text = file_content[5:]

    def file_read(self) -> dict:
        """Coordinates operation of reading data from file"""
        self.file_name_check()
        self.get_content()

        return {"encoding": self.encoding, "encrypted_text": self.encrypted_text}
