from pkg_mgr.grb import *
from pkg_mgr.dmp import *
from pkg_mgr.updt import *

def metis(arg: str | None = ... , **kwarg):
    try:
        globals()[arg](**kwarg)
    except KeyError:
        print("metis: Operation Not Found")

def metis_info():
    print("metis: BeaconOS package manager")
    print("Command Syntax: metis [operation] [object]")
    print("[operation] grb: get a software from BeaconOS Server; dmp: remove a local software; updt: update a software")