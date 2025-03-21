import yaml


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def send_config_netmiko(net_connect, config_commands):
    net_connect.enable()
    net_connect.send_config_set(config_commands)

def send_show_netmiko(net_connect, command):
    output = net_connect.send_command(command)
    return output