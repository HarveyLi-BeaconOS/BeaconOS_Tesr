from time import sleep
from maskpass import askpass
from os import system as cmd
from pathlib import Path as path
from Messages_Declear import *

class verify:
    def init(password: str) -> bool:
        if verify.check(password=password):
            return True
        else:
            return False
    def check(password: str) -> bool:
        global password_file_path
        password_file_path = path("passwords/passwords.bpass").absolute()
        with open(password_file_path) as file:
            password_extracted = file.read().splitlines()
            for x in password_extracted:
                if password == x:
                    return True
            else:
                return False

print("Welcome to BeaconOS v1.7     Kernel Version: Linux 6.0.7    UI Version: v2.4")
while __name__ == '__main__':
    for x in range(10):
        inputs = str(askpass(prompt="Enter Login Password: ", mask="*"))
        if verify.init(password=inputs):
            cmd("python3 MShell4.py")
            break
        else:
            print("login:",PasswordIncorrect)
    else:
        print("login: Too many failed attempts. Please wait for 10 minutes to try again")
        for x in range(600):
            sleep(1)
            print(f"Time Left: {600-x} seconds")
    break