from sys import platform

import psutil
import subprocess
from AppOpener import open
import util

def is_running(process_name):
    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() == process_name.lower():
                return True
        except:
            pass
    return False

def focus_windows(title_contains, maximize):
    try:
        import pygetwindow as gw

        windows = gw.getAllWindows()

        for win in windows:
            if title_contains.lower() in win.title.lower():
                if win.isMinimized:
                    win.restore()

                win.activate()
                if maximize:
                    win.maximize()

                return True
    except Exception as e:
        print("Windows focus error:", e)
    return False


def focus_linux(title_contains):
    try:
        result = subprocess.check_output(["wmctrl", "-l"]).decode()

        for line in result.splitlines():
            if title_contains.lower() in line.lower():
                window_id = line.split()[0]
                subprocess.run(["wmctrl", "-ia", window_id], check=True)
                subprocess.run(["wmctrl", "-ir", window_id, "-b", "add,maximized_vert,maximized_horz"], check=True)
                return True
    except Exception as e:
        print("Linux focus error:", e)
    return False


def launch_or_focus(app_name, title_contains, maximize=True):
    system = util.get_platform()
    focused = False
    if system == util.Platforms.Windows:
        focused = focus_windows(title_contains, maximize)
    elif system == util.Platforms.Linux:
        focused = focus_linux(title_contains)
    if not focused:
        open(app_name)