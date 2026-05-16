import threading

import generic
import util

import requests
import subprocess
import os

class patch(generic.Patcher, generic.Downloadable):
    name = "spicetify"
    install_commands = ["iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex", "curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh", "curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh"]
    command_based = True

    def update(self):
        if not self.is_installed():
            return
        platform = util.get_platform()
        cmd = f"{self.name} update"
        self._run_command_thread(cmd, windows=(platform == util.Platforms.Windows))

    def patch(self, args):
        self.install()
        if self.is_installed():
            self.update()