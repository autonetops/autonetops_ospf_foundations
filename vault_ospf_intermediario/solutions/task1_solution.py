import yaml
from netmiko import ConnectHandler

with open('topology.yaml', 'r') as file:
	topology = yaml.safe_load(file)

for device in topology:
	config_commands = [
		'router ospf 1',
		f'router-id {device["netmiko"]["host"]}',
		'network 192.168.0.0/16 area 0',
	]

	net_connect = ConnectHandler(**device["netmiko"])
	net_connect.enable()
	net_connect.send_config_set(config_commands)
	net_connect.disconnect()