from importlib import reload
import datetime
import threading
from MShell_Support import *
from Shell_Prerequ import pre
import Messages_Declear
import gnureadline

class cmd:
    def split(input: str | None = ...) -> list:
        repository = [ ]
        for x in input.split():
            repository.append(x)
        return repository
    
    def length(source: list | None = ...) -> int | bool:
        if not len(source) < 1:
            return len(source)
        else:
            return False
    
    def exec(length: int | None = 1, source: list | None = ...) -> None:
        try:
            if length == 1:
                globals()[source[0]]()
            else:
                globals()[source[0]](*source[1:])
        except KeyError:
            print("Margaret Shell:",source[0],Messages_Declear.CanNotFindCommand)
        except Exception as e:
            print(e)
    
def run(source: list | None = ..., name: str | None = "Thread") -> None:
    thread = threading.Thread(target=cmd.exec, args=(cmd.length(source=source), source), name=name)
    thread.start()
    thread.join()

class interface:
    def io() -> str:
        inputs = input("Margaret Shell>>> ")
        return inputs
    
    def main():
        inputs = interface.io()
        run(source=cmd.split(input=inputs), name=cmd.split(input=inputs)[0])

pre()
print(f"Login time {datetime.datetime.now()}")
while __name__ == '__main__':
    try:
        interface.main()
    except KeyboardInterrupt:
        print('\n')
    except Exception as e:
        if e == None:
            print_error(
            error_file_name="MShell4.py",
            error_name="InterpreterError",
            error_ln=53,
            error_class=None,
            error_func="interface.main()",
            define_class_ln=37,
            define_func_ln=45,
            define_file_name="MShell4.py",
            define_main_routine_name="run(source=cmd.split(input=inputs), name=cmd.split(input=inputs)[0])",
            define_class_name="class interface:",
            define_function_name="def main():",
            exit_code=1,
            error_details=e
            )
