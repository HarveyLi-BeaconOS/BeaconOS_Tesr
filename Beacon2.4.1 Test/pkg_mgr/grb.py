import os, pathlib,urllib.request

class grb:
    def __init__(self,filename) -> None:
        try:
            grb.get(file_name=filename, server_addr=..., username="beaconos")
        except Exception as e:
            print("metis: FATAL ERROR:",e)

    
    def get(file_name: str, server_addr: str, username: str) -> None:
        if urllib.request.urlopen(url=f"ftp://{username}@{server_addr}:/home/{username}/{file_name}"):
            urllib.request.urlopen(f"ftp://{username}@{server_addr}:/home/{username}/{file_name}", file_name)
        else:
            return None