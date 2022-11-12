from os import kill, system as cmd
import sys
from Errors import ExitSignal

class Logout:
    def init(self: str,target: str, flag: str) -> bool:
        raise ExitSignal

def logout(self: str,target: str, flag: str):
    if not __name__ == '__main__':
        if Logout.init():
            print("logout: Logging out of the system")
        else:
            print("logout: Permission Denied by System")
    else:
        print("logout: Permisson Denied")
    #else:
        #print(__name__)