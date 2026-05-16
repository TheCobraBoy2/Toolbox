import customtkinter
from patchers import get_all_patchers
from generic import Downloadable

def install_patchers():
    for patcher in get_all_patchers():
        if isinstance(patcher, Downloadable):
            patcher.install()

class HomeView(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(
            self,
            text="Dashboard",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        title.grid(row=0, column=0, pady=(20, 10))

        button = customtkinter.CTkButton(
            self,
            text="Install All Patchers",
            font=customtkinter.CTkFont(size=15, weight="bold"),
            command=lambda : install_patchers()
        )
        button.grid(row=1, column=0, pady=20)