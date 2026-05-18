import customtkinter
import generic

from my_things import get_all_things

def run_thing(thing):
    thing.execute()

class UtilitiesView(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(
            self,
            text="My Utilities",
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

        for thing in get_all_things():
            def make_command(t):
                return lambda: run_thing(t)
            self.button_grid.add_button(
                text=thing.display_name,
                command=make_command(thing),
            )