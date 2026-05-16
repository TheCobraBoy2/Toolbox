import threading

import generic
import util

import requests
import subprocess
import os

class patch(generic.Patcher):
    command = "spicetify"
    install_commands = ["iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex", "curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh", "curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh"]

    def _run_command_thread(self, cmd, windows=False):
        def target():
            if windows:
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

    def install(self):
        if self.is_installed():
            return
        platform = util.get_platform()
        cmd = self.install_commands[platform.value]

        self._run_command_thread(cmd, windows=(platform == util.Platforms.Windows))

    def is_installed(self):
        return util.command_exists(self.command)

    def update(self):
        if not self.is_installed():
            return
        platform = util.get_platform()
        cmd = f"{self.command} update"
        self._run_command_thread(cmd, windows=(platform == util.Platforms.Windows))

    def patch(self, args):
        self.install()
        if self.is_installed():
            self.update()