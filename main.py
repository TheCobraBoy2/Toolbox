import customtkinter
from ctksidebar import CTkSidebarNavigation
import pages

def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.ThemeManager.load_theme("themes/red.json")

    app = customtkinter.CTk()
    app.title("Toolbox")
    app.geometry("640x480")

    nav = CTkSidebarNavigation(master=app, width=185)
    nav.pack(fill="both", expand=True)

    side = nav.sidebar

    header = customtkinter.CTkLabel(
        side,
        text="Toolbox",
        font=customtkinter.CTkFont(size=20, weight="bold"),
        fg_color="transparent",
        anchor="center",
        height=70
    )
    side.add_frame(header)

    side.add_item(id="home", text="Dashboard")
    side.add_item(id="patcher", text="Patchers")
    side.add_item(id="apps", text="Apps")

    home_view = pages.HomeView(nav.view("home"))
    home_view.pack(fill="both", expand=True)

    patcher_view = pages.PatcherView(nav.view("patcher"))
    patcher_view.pack(fill="both", expand=True)

    app_view = pages.AppView(nav.view("apps"))
    app_view.pack(fill="both", expand=True)

    nav.set("home")

    app.mainloop()

if __name__ == '__main__':
    main()