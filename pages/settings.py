import customtkinter

class SettingsView(customtkinter.CTkFrame):
    def __init__(self, master, on_theme_change):
        super().__init__(master)

        self.on_theme_change = on_theme_change
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(
            self,
            text="Options",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        title.grid(row=0, column=0, pady=(20, 10))

        theme_selector = customtkinter.CTkOptionMenu(
            self,
            values=["red", "breeze", "coffee", "metal"],
            command=self.on_theme_change,
        )

        theme_selector.grid(row=1, column=0, pady=(20, 10))