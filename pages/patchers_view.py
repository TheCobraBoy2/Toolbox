import customtkinter

from patchers import get_all_patchers
import generic


def run_patcher(patcher):
    patcher.patch({})


class PatcherView(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(
            self,
            text="Patchers",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        title.grid(row=0, column=0, pady=(20, 10))

        self.button_grid = generic.ButtonGrid(
            self,
            items_per_row=3
        )

        self.button_grid.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=20
        )
        for patcher in get_all_patchers():
            def make_command(p):
                return lambda: run_patcher(p)
            self.button_grid.add_button(
                text=patcher.display_name,
                command=make_command(patcher),
            )

