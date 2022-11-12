from rmf import * 
from show import *
from layer import *
from mdoc import *
from rt import *
from scrte import *
from info import * 
from get import *
from Messages_Declear import *
from adpsd import *
from adcmd import *
from installer import *
from logout import *
from fder import *
from mkly import *
from view import *
from pwr import *
from exc import *
from pkg_mgr.metis import *
import pathlib, random, json,subprocess

number_register = [ ]
DEFAULT_SOURCE_WORD = ["Hi!", "What?", "Say something...", "Dude..?", "Still alive?", "Why?"
                    "Do something", "Remain clam", "Nothing bad", "How's your day going?", "What?",
                    "Define what you are doing", "Move", "Remember to save", "Make!", "Make something spark",
                    "Did you do your work?", "Why you download this?", "Good morning!", "Pardon me?",
                    "Luck comes to who float", "Motivational quotes?"]
DEFAULT_SOURCE_SENTENCE_EMPTY = [ ]

def cls(*arg, **kwarg):
    sys.stdout.write("\x1b[2J\x1b[H")

def print_error(error_file_name: str, error_name: str, error_ln: int, 
error_class: str, error_func: str, define_class_ln: int, 
define_func_ln: int,  define_file_name: str,
define_main_routine_name: str,define_class_name: str, 
define_function_name: str, exit_code: int, error_details: str):
    '''
    CLASS:    Not defined in class

    FUNCTION: print_error()

    ARGUMENTS:
        1) error_file_name: str         [the file name that the error occured]
        2) error_name: str              [the error's name(What is the error)]
        3) error_ln: int                [the line where the error occured]
        4) error_class: str             [the class where the error occured]
        5) error_func: str              [the function where the error occured]
        6) define_class_ln: int         [the the line where the function called is defined in the class]
        7) define_func_ln: int          [the line where the function called is defined]
        8) define_file_name: str        [the file where the called function is defined]
        9) define_class_name: str       [the class that the function is defined WITH THE CLASS KEYWORD]
        10) define_function_name: str   [the function that been called be defined WITH THE DEF KEYWORD]
        11) exit_code: int              [exit code]
        12) error_details: str          [details of the error]
    '''
    print('\n',"APPLICATION CRASH REPORT:",'\n')
    print(f"    SOFTWARE: {error_file_name} >> ln {error_ln} > {error_class} > {error_func}",'\n')
    print(f"    DEFINITION: {define_file_name} >> {define_main_routine_name}:",'\n')
    print(f"                {define_class_ln}    {define_class_name} ")
    print(f"                {define_func_ln}     {define_function_name}", '\n')
    print(f"    ERROR TYPE: {error_name}",'\n')
    print(f"    EXIT CODE: {exit_code}",'\n')
    print(f"    REPORT DETAILS: {error_details}", '\n')

class executable:
    def fetch_path() -> dict | bool:
        if executable.search(destination=executable.get_addr(file_name="sys_config.json"),filename="sys_config.json"):
            with open(executable.get_addr(file_name="sys_config.json"),'r') as file:
                config = json.load(file)
            return config
        else:
            return False
    
    def get_exec_path(config: dict) -> str | None:
        if len(config) <= 0:
            return None
        else:
            return config["EXEC_PATH"]

    def get_addr(file_name: str | list) -> str | list:
        if type(file_name) is list:
            addr_list = [ ]
            for x in file_name:
                addr = str(Path("executables").absolute()) + "/" + x
                addr_list.append(addr)
            return addr_list
        else:
            return str(Path("executables").absolute()) + "/" + file_name

    def exec(file_name: str):
        if executable.search(destination=executable.get_addr(file_name=file_name),filename=file_name):
           subprocess.call(f"python3 {executable.get_addr(file_name=file_name)}",shell=True)
        else:
            return None

    def search(destination: str | list | tuple, filename: str) -> bool:
        if type(destination) is str and type(filename) is str:
            current_dir = str(Path(destination).absolute()) + "/" + filename
            if os.path.exists(current_dir):
                return True
            else:
                return False
        else:
            for x in destination:
                current_dir = str(Path(destination).absolute()) + "/" + x
                if os.path.exists(current_dir):
                    return True
            else:
                return False
    
    def __init__(self,file: str) -> None:
        executable.exec(file)
