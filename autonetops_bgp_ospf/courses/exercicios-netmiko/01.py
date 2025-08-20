from netmiko import ConnectHandler
from rich import print as rprint
import ipdb


device = {
    "host": "r2",
    "username": "admin",
    "password": "autonetops",
    "device_type": "cisco_ios",
}

with ConnectHandler(**device) as conn:
    output = conn.send_command("show ip route", use_textfsm=True)

rotas_ospf = [
    {"network": route["network"], "nexthop_ip": route["nexthop_ip"]}
    for route in output
    if route["protocol"] == "O"
]
rprint(rotas_ospf)
