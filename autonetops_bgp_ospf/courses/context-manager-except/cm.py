from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

r1 = {
    "host": "r1",
    "username": "admin",
    "password": "autonetops",
    "device_type": "cisco_ios",
}

try:
    with ConnectHandler(**r1) as conn:
        output = conn.send_command("show ip int brief")
        print(output)

except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
    print(f"Erro conhecido: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")