import os, pathlib, urllib.request
import zipfile

class connect:
    def connect(usr: str, credit: str, 
    addr: str, name: str) -> bool:
        try:
            urllib.request.urlopen(f"ftp://{usr}@{addr}")
        except Exception:
            return False
        else:
            return True
    
    def fetch(file_name: str, usr: str, addr: str):
        if connect.connect(name=file_name):
            return urllib.request.urlopen(f"ftp://{usr}@{addr}:/home/beaconos/{file_name}")
        else:
            return None

class remove:
    def get_names(source):
        list = [ ]
        if os.path.exists(source):
            src = open(source,'r')
            content = src.read()
        else:
            return None

    def rm(names: list) -> bool:
        os.chdir("..")
        path = pathlib.Path(names).absolute()
        for x in names:
            if os.path.isfile(path=path):
                os.remove(x)
            else:
                pass
class upgrade:
    def start() -> None: ...
    def connect(usr: str, credit: str, addr: str, name: str) -> None:
        if connect.connect(usr,credit,addr,name) and not connect.fetch(file_name="SYS_UPGD_CATALOG.zip") == None:
            with zipfile.ZipFile(connect.fetch(file_name="SYS_UPGD_CATALOG.zip"), 'r') as zip:
                os.chdir("..")
                path = pathlib.Path("Beacon2.3.1").absolute()
                remove.rm()
                zip.extractall(path=path)
        else:
            print("metis: ERROR: Failed to fetch upgrade packages for BeaconOS")