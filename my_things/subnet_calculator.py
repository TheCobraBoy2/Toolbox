import generic
from multiprocessing import Process
import customtkinter as ctk
import ipaddress
import math


def calculate_ip_with_prefix(ip_with_prefix):
    ip = ipaddress.IPv4Interface(ip_with_prefix)
    network = ip.network
    return {
        "IP": str(ip.ip),
        "Network": str(network.network_address),
        "Broadcast": str(network.broadcast_address),
        "Netmask": str(network.netmask),
        "Wildcard": str(network.hostmask),
        "Usable Hosts": [str(h) for h in network.hosts()],
        "Total Hosts": network.num_addresses - 2 if network.num_addresses > 2 else network.num_addresses
    }

def calculate_nearest_subnet(ip_address, required_hosts):
    prefix = 32 - math.ceil(math.log2(required_hosts + 2))
    network = ipaddress.IPv4Network(f"{ip_address}/{prefix}", strict=False)
    return {
        "Network": str(network.network_address),
        "Broadcast": str(network.broadcast_address),
        "Netmask": str(network.netmask),
        "Prefix": prefix,
        "Usable Hosts": [str(h) for h in network.hosts()],
        "Total Hosts": network.num_addresses - 2
    }


def create_entry(parent, placeholder="", width=250):
    return ctk.CTkEntry(parent, placeholder_text=placeholder, width=width)


def create_button(parent, text, command, width=150):
    return ctk.CTkButton(parent, text=text, command=command, width=width)


def create_frame(parent, **kwargs):
    return ctk.CTkFrame(parent, fg_color="transparent", **kwargs)


def create_result_field(parent, field_name, width=250, row=0):
    lbl = ctk.CTkLabel(parent, text=field_name + ":")
    lbl.grid(row=row, column=0, sticky="w", padx=(0, 10), pady=2)
    ent = ctk.CTkEntry(parent, width=width)
    ent.grid(row=row, column=1, sticky="w", pady=2)
    ent.configure(state="readonly")
    return ent


def update_entry(entry, value):
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, value)
    entry.configure(state="readonly")


def run_app():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.title("Subnet Calculator")
    app.geometry("600x450")

    title_label = ctk.CTkLabel(app, text="Subnet Calculator", font=ctk.CTkFont(size=16))
    title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)

    # IP + Hosts
    parent_frame = create_frame(app)
    parent_frame.grid(row=1, column=0, columnspan=2, pady=10)

    left_frame = create_frame(parent_frame)
    left_frame.grid(row=0, column=0, padx=(0,10), sticky="n")
    left_frame.grid_columnconfigure(0, weight=1)

    entry_ip = create_entry(left_frame, "Enter IP address (e.g., 192.168.1.0)")
    entry_ip.grid(row=0, column=0, pady=(0,5), sticky="ew")

    entry_hosts = create_entry(left_frame, "Number of hosts")
    entry_hosts.grid(row=1, column=0, pady=(0,5), sticky="ew")

    right_frame = create_frame(parent_frame)
    right_frame.grid(row=0, column=1, sticky="n")

    # CIDR
    parent_frame_cidr = create_frame(app)
    parent_frame_cidr.grid(row=2, column=0, columnspan=2, pady=10)

    left_frame_cidr = create_frame(parent_frame_cidr)
    left_frame_cidr.grid(row=0, column=0, padx=(0,10), sticky="n")
    left_frame_cidr.grid_columnconfigure(0, weight=1)

    entry_cidr = create_entry(left_frame_cidr, "Enter IP/CIDR (e.g., 192.168.1.10/24)")
    entry_cidr.grid(row=0, column=0, pady=(0,5), sticky="ew")

    right_frame_cidr = create_frame(parent_frame_cidr)
    right_frame_cidr.grid(row=0, column=1, sticky="n")

    # Result
    result_frame = create_frame(app)
    result_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky="n")
    result_frame.grid_columnconfigure(0, weight=1)
    result_frame.grid_columnconfigure(1, weight=1)

    # Define result fields dynamically
    fields = ["Network", "Broadcast", "Netmask", "Total Hosts", "Prefix"]
    entries = {}
    for i, field in enumerate(fields):
        entries[field] = create_result_field(result_frame, field, row=i)

    # Callbacks
    def calculate_hosts_subnet():
        ip = entry_ip.get()
        try:
            hosts = int(entry_hosts.get())
            if hosts <= 0:
                raise ValueError
            res = calculate_nearest_subnet(ip, hosts)

            update_entry(entries["Network"], res["Network"])
            update_entry(entries["Broadcast"], res["Broadcast"])
            update_entry(entries["Netmask"], res["Netmask"])
            update_entry(entries["Total Hosts"], res["Total Hosts"])
            update_entry(entries["Prefix"], str(res["Prefix"]))

        except ValueError:
            for f in entries:
                update_entry(entries[f], "Invalid IP or # of hosts")

    button_hosts = create_button(right_frame, "Calculate Subnet", calculate_hosts_subnet)
    button_hosts.grid(row=0, column=0, pady=(0,0), sticky="n")

    def calculate_cidr_subnet():
        ip = entry_cidr.get()
        try:
            res = calculate_ip_with_prefix(ip)
            update_entry(entries["Network"], res["Network"])
            update_entry(entries["Broadcast"], res["Broadcast"])
            update_entry(entries["Netmask"], res["Netmask"])
            update_entry(entries["Total Hosts"], res["Total Hosts"])
            prefix = ip.split("/")[-1] if "/" in ip else "N/A"
            update_entry(entries["Prefix"], f"/{prefix}")
        except ValueError:
            for f in entries:
                update_entry(entries[f], "Invalid CIDR subnet")

    button_cidr = create_button(right_frame_cidr, "Calculate CIDR", calculate_cidr_subnet)
    button_cidr.grid(row=0, column=0, pady=(0,0), sticky="n")

    app.mainloop()


class SubnetCalculator(generic.MyType):
    display_name = 'Subnet Calculator'

    def execute(self):
        p = Process(target=run_app)
        p.daemon = False
        p.start()