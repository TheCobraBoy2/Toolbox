import shutil

def command_exists(command):
    return shutil.which(command) is not None