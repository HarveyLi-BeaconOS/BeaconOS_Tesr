import os
import subprocess
from pathlib import Path

class configure:
    def path() -> str:
        path = str(Path("installer_tool_kit").absolute()) + "/_entry.sh"
        if os.path.exists(path):
            return path

class install:
    def __init__(self) -> None:
        subprocess.call(['sh', configure.path()])