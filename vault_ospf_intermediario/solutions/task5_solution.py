
from helpers import load_yaml, send_config_netmiko, send_show_netmiko
from netmiko import ConnectHandler

topology = load_yaml("topology.yaml")
device_name = input('Digite os nomes dos roteadores separados por vírgula (ou deixe em branco para todos): ') #r2,r1
config_commands = input('Comandos de configuracao separados por virgula: ')
# device_name: r1, r2
# config_commands: int et1, ip ospf authentication,ip ospf authentication key 0 ospf123

# device_name: r3, r4
# config_commands: int et1, ip ospf authentication message-digest, ip ospf message-digest-key 1 md5 0 md5ospf


match device_name:
	case '':
		filter_topology = topology
	case _:
		device_names = [name.strip().lower() for name in device_name.split(',')]
		filter_topology = list(filter(lambda device: device["name"] in device_names, topology))

#filter_topology = [device for device in topology if device["name"] == device_name]
config_commands = [config.strip().lower() for config in config_commands.split(',')]

for device in filter_topology:

	net_connect = ConnectHandler(**device["netmiko"])
	send_config_netmiko(net_connect, config_commands)
	
	show_result = send_show_netmiko(net_connect, 'sh ip ospf interface')
	print(show_result)

	net_connect.disconnect()