import customtkinter

import patchers

class ButtonGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, items_per_row=3):
        super().__init__(master)

        self.items_per_row = items_per_row

        for i in range(items_per_row):
            self.grid_columnconfigure(i, weight=1)

    def add_button(self, text, command=None):
        count = len(self.winfo_children())

        row = count // self.items_per_row
        col = count % self.items_per_row

        button = customtkinter.CTkButton(
            self,
            text=text,
            command=command
        )

        button.grid(
            row=row,
            column=col,
            padx=10,
            pady=10,
            sticky="ew"
        )

        return button


# def clicked(patch_name):
#     print(f"Clicked {patch_name}")

p = patchers.TestPatch()

class PatcherView(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = customtkinter.CTkLabel(
            self,
            text="Dashboard",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        title.grid(row=0, column=0, pady=(20, 10))

        self.button_grid = ButtonGrid(
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

        for i in range(50):
            patch_name = f"Patch {i + 1}"

            self.button_grid.add_button(
                text=patch_name,
                command=lambda name=patch_name: p.patch(args={"name": name})
            )

