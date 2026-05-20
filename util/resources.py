import os
import sys
from enum import Enum

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

theme_dir = resource_path("resources/themes")
theme_files = os.listdir(theme_dir)
theme_values = [os.path.splitext(f)[0] for f in theme_files]

Themes = Enum('Themes', {name.upper(): name for name in theme_values})

def _theme_path(name):
    return os.path.join(resource_path("resources/themes"), name)

def get_theme_path(theme=Themes.RED):
    file_name = f"{theme.value}.json"
    path = _theme_path(file_name)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Theme {theme} not found. Expected path: {path}")
    return path

def get_theme_path_str(theme=Themes.RED.value):
    file_name = f"{theme}.json"
    path = _theme_path(file_name)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Theme {theme} not found. Expected path: {path}")
    return path