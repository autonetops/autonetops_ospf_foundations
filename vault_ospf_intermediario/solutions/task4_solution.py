
from helpers import load_yaml, send_config_netmiko, send_show_netmiko
from netmiko import ConnectHandler

topology = load_yaml("topology.yaml")
device_name = input('Digite os nomes dos roteadores separados por vírgula (ou deixe em branco para todos): ') #r2,r1

match device_name:
	case '':
		filter_topology = topology
	case _:
		device_names = [name.strip().lower() for name in device_name.split(',')]
		filter_topology = list(filter(lambda device: device["name"] in device_names, topology))

#filter_topology = [device for device in topology if device["name"] == device_name]
for device in filter_topology:
	config_commands = [
		'router ospf 1',
		'auto-cost reference-bandwidth 1500'
	]


	net_connect = ConnectHandler(**device["netmiko"])
	send_config_netmiko(net_connect, config_commands)
	
	#show_result = send_show_netmiko(net_connect, 'sh run')
	#print(show_result)

	net_connect.disconnect()