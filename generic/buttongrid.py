import customtkinter

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
