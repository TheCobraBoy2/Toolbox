import os, requests
import util
import subprocess
import threading

class Downloadable:
    install_dir = os.path.join(os.path.expanduser('~'), ".toolbox", "bin")
    url = None
    install_commands = None
    name = None
    command_based = False
    show_terminal = True

    def _run_command_thread(self, cmd, windows=False):
        def target():
            # I don't think the linux works
            if windows:
                if self.show_terminal:
                    subprocess.Popen(
                        ["powershell", "-Command", f"{cmd}; Read-Host 'Press Enter to exit'"],
                        creationflags=subprocess.CREATE_NEW_CONSOLE
                    )
                else:
                    subprocess.Popen(
                        ["powershell", "-Command", f"{cmd}; Read-Host 'Press Enter to exit'"],
                        creationflags=subprocess.CREATE_NEW_CONSOLE
                    )
            else:
                subprocess.Popen([
                    "gnome-terminal", "--", "bash", "-c", f"{cmd}; echo 'Press Enter to exit'; read line"
                ])
        thread = threading.Thread(target=target)
        thread.start()

    def get_final_path(self):
        if not self.name:
            raise ValueError("No file name specified for Downloadable")
        return os.path.join(self.install_dir, self.name)

    def install(self, quiet=False):
        if self.is_installed():
            if not quiet:
                print(f"{self.name} already installed.")
            return
        if not self.command_based:
            os.makedirs(self.install_dir, exist_ok=True)
            if not self.url:
                print(f"No URL provided for {self.name}")
                return
            response = requests.get(self.url, stream=True)
            if response.status_code == 200:
                with open(self.get_final_path(), "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                if not quiet:
                    print(f"{self.name} downloaded successfully.")
            else:
                print(f"Failed to download {self.name}: {response.status_code}")
        else:
            platform = util.get_platform()
            cmd = self.install_commands[platform.value]
            self._run_command_thread(cmd, windows=(platform == util.Platforms.Windows))

    def is_installed(self):
        if self.command_based:
            return util.command_exists(self.name)
        else:
            return self.get_final_path() and os.path.exists(self.get_final_path())