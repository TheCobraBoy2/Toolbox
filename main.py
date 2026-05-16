import customtkinter
from ctksidebar import CTkSidebarNavigation, CTkSidebar
import pages
import util
from util import command_exists


def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("themes/red.json")
    current_page = "home"

    app = customtkinter.CTk()
    app.title("Toolbox")
    app.geometry("640x480")

    nav : CTkSidebarNavigation | None = None
    side : CTkSidebar | None = None

    def rebuild_ui():
        nonlocal current_page
        current_page = nav._current_id
        for widget in nav.winfo_children():
            widget.destroy()
        nav.destroy()
        build_app()

    def switch_theme(theme_name):
        customtkinter.set_default_color_theme(f"themes/{theme_name}.json")
        rebuild_ui()

    def build_app():
        nonlocal nav, side

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
        side.add_item(id="settings", text="Options")

        home_view = pages.HomeView(nav.view("home"))
        home_view.pack(fill="both", expand=True)

        patcher_view = pages.PatcherView(nav.view("patcher"))
        patcher_view.pack(fill="both", expand=True)

        app_view = pages.AppView(nav.view("apps"))
        app_view.pack(fill="both", expand=True)

        settings_view = pages.SettingsView(nav.view("settings"), switch_theme)
        settings_view.pack(fill="both", expand=True)

        nav.set(current_page)

    build_app()
    app.mainloop()


if __name__ == "__main__":
    main()