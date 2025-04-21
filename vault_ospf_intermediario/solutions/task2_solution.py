
from helpers import load_yaml, send_config_netmiko
from netmiko import ConnectHandler

topology = load_yaml("topology.yaml")
device_name = input('Digite o nome do roteador: ') #r1

#filter_topology = [device for device in topology if device["name"] == device_name]
filter_topology = list(filter(lambda device: device["name"] == device_name, topology))

for device in filter_topology:
	config_commands = [
		'router ospf 1',
		'router-id 11.11.11.11'
	]

	net_connect = ConnectHandler(**device["netmiko"])
	send_config_netmiko(net_connect, config_commands)
	net_connect.disconnect()

### SEND SHOW COMMANDS