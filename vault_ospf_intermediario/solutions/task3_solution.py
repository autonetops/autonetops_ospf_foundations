
from helpers import load_yaml, send_config_netmiko, send_show_netmiko
from netmiko import ConnectHandler

topology = load_yaml("solutions/topology.yaml")
device_name = input('Digite o nome do roteador: ') #r3

#filter_topology = [device for device in topology if device["name"] == device_name]
filter_topology = list(filter(lambda device: device["name"] == device_name, topology))

for device in filter_topology:
	config_commands = [
		'int et0/1',
		'ip ospf priority 100'
	]


	net_connect = ConnectHandler(**device["netmiko"])
	
	send_config_netmiko(net_connect, config_commands)
	show_result = send_show_netmiko(net_connect, 'sh run int et0/1')
	print(show_result)

	net_connect.disconnect()