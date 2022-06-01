from manager import Manager


if __name__ == "__main__":
    start = Manager()
    start.execute()


"""
1. Encrypt (> type text to encrypt; > way of encryption - ROT47, ROT13) - saving to buffer
2. Save to file (.txt lub .json)
3. Read from file and decrypt
4. Exit

OOP, SOLID, GRASP
advanced concept
multiple files/directories

what classes?
Menu
Encrypt
Decrypt
FileOperations
...

distinguishing between rot47 and rot13
Markup at the beginning of file
...

directory for encrypted files?
ciphered_json
ciphered_txt
to_decrypt
...

which design patterns?
Facade
...

"""
