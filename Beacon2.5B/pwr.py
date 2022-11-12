import os, sys, time as t, Messages_Declear as md

class operations:
    def s(time: int):
        if type(time) == int:
            try:
                t.sleep(float(time))
                os.system("poweroff")
            except OSError:
                t.sleep(float(time))
                os.system("shutdown")
        else:
            return False

    def r(time: int):
        if type(time) == int:
            t.sleep(float(time))
            os.system("reboot")
        else:
            return False

def identifier(operation: str, *args):
    try:
        locals()[operation](*args)
    except KeyError:
        print(md.IllegalOperation)

def pwr(op: str, time: int):
    identifier(op,time)

def pwr_info():
    print("pwr: power manager for BeaconOS")
    print("Command Syntax: pwr [operation] [time]")
    print("operation: s: poweroff, r: reboot")
    print("time: time before operation")