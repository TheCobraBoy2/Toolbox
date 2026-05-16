import generic

import requests
import subprocess
import os

class patch(generic.Patcher, generic.Downloadable):
    display_name = "Discord"
    install_dir = os.path.join(os.path.expanduser('~'), ".toolbox", "bin")
    url = "https://github.com/Vencord/Installer/releases/latest/download/VencordInstaller.exe"
    name = "VencordInstaller.exe"

    def patch(self, args):
        self.install(quiet=True)
        subprocess.run([self.get_final_path()])