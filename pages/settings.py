import customtkinter
from util import Themes, SettingsManager, default_config

sm = SettingsManager()
def p():
    sm.set("window_size", default_config.get("window_size", "640x480"))

class SettingsView(customtkinter.CTkFrame):
    def __init__(self, master, on_theme_change, app):
        super().__init__(master)

        self.on_theme_change = on_theme_change
        self.app = app
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(
            self,
            text="Options",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        title.grid(row=0, column=0, pady=(20, 10))

        theme_selector = customtkinter.CTkOptionMenu(
            self,
            values=[theme.value for theme in Themes],
            command=self.on_theme_change,
        )
        theme_selector.set(sm.get("theme", "red"))
        theme_selector.grid(row=1, column=0, pady=(20, 10))
        reset_size = customtkinter.CTkButton(
            self,
            text="Reset Window Size",
            command=lambda : self.app.geometry(default_config.get("window_size", "640x480"))
        )
        reset_size.grid(row=2, column=0, pady=(20, 10))