import customtkinter

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
            text="Click Me"
        )
        button.grid(row=1, column=0, pady=10)

        textbox = customtkinter.CTkTextbox(self, width=300, height=150)
        textbox.grid(row=2, column=0, padx=20, pady=20)