import codecs


class Decrypt:
    def decrypt(self, type_of_encoding_: str, text_to_decrypt_: str) -> str:
        """Checks and executes proper decription method"""
        if type_of_encoding_ == "rot13":
            result = self.decrypt_rot_13(text_to_decrypt_)
        elif type_of_encoding_ == "rot47":
            result = self.decrypt_rot_47(text_to_decrypt_)
        else:
            print("Wystąpił błąd")
            exit()
        return result

    def decrypt_rot_13(self, text_to_decrypt_: str) -> str:
        """Does ROT13 decritption"""
        return codecs.decode(text_to_decrypt_, "rot_13")

    def decrypt_rot_47(self, text_to_decrypt_: str) -> str:
        """Does ROT47 decritption"""
        key = 47
        decryp_text = ""

        for i, z  in enumerate(text_to_decrypt_):
            temp = ord(text_to_decrypt_[i]) - key
            if ord(text_to_decrypt_[i]) == 32:
                decryp_text += " "
            elif temp < 32:
                temp += 94
                decryp_text += chr(temp)
            else:
                decryp_text += chr(temp)
                # if-else

        return decryp_text
