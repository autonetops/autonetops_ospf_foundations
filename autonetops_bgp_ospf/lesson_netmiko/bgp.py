from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import yaml
import ipdb
from rich import print as rprint


with open('bgp.yaml', 'r') as yaml_data:
    data = yaml.safe_load(yaml_data)

for device, device_data in data.items():
    print(device)
    # Renderizar configuracao Jinja
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("bgp.j2")

    config = template.render(device_data['bgp'])
    
    # Conexao e envio da configuracao
    print(device_data['conn'])

    conn = ConnectHandler(**device_data['conn'])
    config = config.splitlines()
    conn.send_config_set(config)
    