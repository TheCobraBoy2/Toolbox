import generic

import requests
import subprocess
import os

class patch(generic.Patcher):
    install_dir = os.path.join(os.path.expanduser('~'), ".toolbox", "bin")
    url = "https://github.com/Vencord/Installer/releases/latest/download/VencordInstaller.exe"
    installer_path = os.path.join(install_dir, "VencordInstaller.exe")

    def install(self):
        if self.isInstalled():
            return
        os.makedirs(self.install_dir, exist_ok=True)
        response = requests.get(self.url, stream=True)
        if response.status_code == 200:
            with open(self.installer_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        else:
            print("Failed to download VencordInstaller:", response.status_code)

    def isInstalled(self):
        return os.path.exists(self.installer_path)

    def patch(self, args):
        self.install()
        subprocess.run([self.installer_path])