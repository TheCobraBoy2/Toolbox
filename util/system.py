from __future__ import annotations
import platform
from enum import Enum

import os
import subprocess
import sys
from pathlib import Path


class Platforms(Enum):
    Windows = 0
    Linux = 1
    Mac = 2
    Unknown = 3

def get_platform():
    os_name = platform.system()
    if os_name == "Windows":
        return Platforms.Windows
    elif os_name == "Linux":
        return Platforms.Linux
    elif os_name == "Darwin":
        return Platforms.Mac
    return Platforms.Unknown

def print_platform():
    print(get_platform())

def open_folder(path: str | Path) -> None:
    p = Path(path).resolve()

    if sys.platform.startswith("win"):
        os.startfile(str(p))
    elif sys.platform == "darwin":
        subprocess.Popen(["open", str(p)])
    else:
        subprocess.Popen(["xdg-open", str(p)])