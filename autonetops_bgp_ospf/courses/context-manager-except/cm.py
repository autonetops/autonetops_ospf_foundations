from netmiko import ConnectHandler


r1 = {
    "host": "r1",
    "username": "admin",
    "password": "autonetops",
    "device_type": "cisco_ios",
}

with ConnectHandler(**r1) as conn:
    output = conn.send_command("show ip int brief")
    print(output)