from netmiko import ConnectHandler
from rich import print as rprint
import ipdb
import json


devices = [
    {
        "host": "r1",
        "username": "admin",
        "password": "autonetops",
        "device_type": "cisco_ios",
    },
    {
        "host": "r2",
        "username": "admin",
        "password": "autonetops",
        "device_type": "cisco_ios",
    },
    {
        "host": "r3",
        "username": "admin",
        "password": "autonetops",
        "device_type": "cisco_ios",
    },
]

resultados_autitoria = []

for device in devices:
    with ConnectHandler(**device) as conn:
        output_version = conn.send_command("show version", use_genie=True)
        output_ip_int_br = conn.send_command("show ip int brief", use_textfsm=True)
        output_ip_ospf = conn.send_command("show ip ospf", use_genie=True)

        resultados_autitoria.append(
            {
                "device": device["host"],
                "output_version": output_version,
                "output_ip_int_br": output_ip_int_br,
                "output_ip_ospf": output_ip_ospf,
            }
        )

with open("auditoria_rede.json", "w") as file:
    json.dump(resultados_autitoria, file, indent=4)
