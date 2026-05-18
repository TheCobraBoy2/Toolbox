import json, os
from util import Themes
config_dir = os.path.join(os.path.expanduser('~'), ".toolbox")
config_file = os.path.join(config_dir, "config.json")

default_config = {
    "theme": Themes.RED.value,
    "window_size": "640x480"
}

def reconcile(t1, t2):
    for k, v in t1.items():
        if k not in t2:
            t2[k] = v
        elif isinstance(v, dict) and isinstance(t2[k], dict):
            reconcile(v, t2[k])
    return t2

class SettingsManager:
    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if hasattr(self, "_initialized"):
            return

        self._initialized = True

        os.makedirs(config_dir, exist_ok=True)
        self.settings = self.load()

    def load(self):

        if not os.path.exists(config_file):
            self.save(default_config)
            return default_config.copy()

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                user_settings = json.load(f)
        except (json.JSONDecodeError, OSError):
            user_settings = {}

        merged = reconcile(default_config.copy(), user_settings)

        self.save(merged)

        return merged

    def save(self, data=None):

        if data is None:
            data = self.settings

        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def get(self, key, default=None):
        if default is None:
            default = default_config.get(key, None)
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value