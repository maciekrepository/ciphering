from abc import ABC
from utils import EncodingOptions


class Menu(ABC):
    def __init__(self):
        self.options = []

    def select_option(self) -> int:
        """Allows to enter option from console"""
        selected_option = input("Wybierz operację: \n" + "".join(self.options))
        return int(selected_option)


class MainMenu(Menu):
    """First menu, displays first menu, allowing to encrypt, decrypt or exit"""

    def __init__(self) -> None:
        super().__init__()
        self.options = [
            "1 - Zaszyfruj tekst \n",
            "2 - Odszyfruj tekst \n",
            "3 - Wyjście \n",
        ]


class SaveMenu(Menu):
    """Third menu, allows to save encrypted string into JSON or txt after string encryption"""

    def __init__(self) -> None:
        super().__init__()
        self.options = ["1 - eksport do pliku JSON \n", "2 - eksport do pliku txt \n"]


class SelectEncodingMenu(Menu):
    """Second menu, allows to choose the standard of encryption"""

    def __init__(self) -> None:
        super().__init__()
        self.options = [
            f"{EncodingOptions.ENCRYPT_ROT13} - szyfruj ROT13 \n",
            f"{EncodingOptions.ENCRYPT_ROT47} - szyfruj ROT47 \n",
        ]
