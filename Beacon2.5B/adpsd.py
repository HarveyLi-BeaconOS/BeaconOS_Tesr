from pathlib import Path as path
class adpsd:
    def __init__(self, password: str) -> None:
        adpsd.add(password)
    def add(password: str):
        password_file_path = path("passwords/passwords.bpass").absolute()
        with open(password_file_path,'w') as file:
            file.write(password)
        print("login: password added")

def adpsd_info():
    print("adpsd: add login password")
    print("Syntax: adpsd [login in password in string]")