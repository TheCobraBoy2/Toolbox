import platform
from enum import Enum


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