import pathlib,os

class dmp:
    def __init__(self,name: str, path_to_spesify: str | None = None) -> None:
        dmp.remove(name=name, path=path_to_spesify)
    
    def remove(path: str | None = "/cmd",name: str | None = ...):
        src_pth = str(pathlib.Path("ext_pkg").absolute()) + path + "/" + name
        if os.path.exists(src_pth):
            os.unlink(src_pth)
        else:
            return None