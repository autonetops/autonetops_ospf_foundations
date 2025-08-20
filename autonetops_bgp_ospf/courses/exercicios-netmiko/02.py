from netmiko import ConnectHandler
from rich import print as rprint
import ipdb


device = {
    "host": "r1",
    "username": "admin",
    "password": "autonetops",
    "device_type": "cisco_ios",
}

with ConnectHandler(**device) as conn:
    output = conn.send_command("show bgp all summary", use_genie=True)


def send_alert():
    rprint("[red]Alerta[/red]")


neighbor_list = []

for neighbor, neighbor_data in output["vrf"]["default"]["neighbor"].items():
    neighbor_state = neighbor_data["address_family"]["ipv4 unicast"]["state_pfxrcd"]

    if not neighbor_state.isdigit():
        send_alert()
    else:
        neighbor_state = "Sessao Estabelecida"

    neighbor_list.append({neighbor: neighbor_state})


rprint(neighbor_list)
