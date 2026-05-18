import os
from enum import Enum

theme_files = os.listdir("resources/themes")
theme_values = [os.path.splitext(f)[0] for f in theme_files]

Themes = Enum('Themes', {name.upper(): name for name in theme_values})

def _theme_path(name):
    return os.path.join("resources", "themes", name)

def get_theme_path(theme = Themes.RED):
    file_name = f"{theme.value}.json"
    if not os.path.exists(_theme_path(file_name)):
        raise FileNotFoundError(f"Theme {theme} not found expected path({_theme_path(file_name)})")
    return _theme_path(file_name)