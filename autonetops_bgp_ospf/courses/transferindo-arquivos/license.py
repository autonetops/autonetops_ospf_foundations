from netmiko import ConnectHandler, file_transfer
import yaml
from rich import print as rprint
import ipdb

with open('inv.yaml', 'r') as file:
    data = yaml.safe_load(file)


for device, device_data in data.items():
    rprint(f"#### Conectando no [green]{device}[/green]")
    with ConnectHandler(**device_data["conn"]) as conn:
        print("Verificando Flash:")
        output_flash = conn.send_command('dir')
        rprint(output_flash)

        try:
            tranfer_result = file_transfer(
                conn,
                source_file="license.lic",
                dest_file="license.lic",
                file_system="unix:/",
                direction="get",
                overwrite_file=True
            )
        except Exception as e:
            print(e)

        if tranfer_result["file_verified"]:
            print("Arquivo transferido e verificado com sucesso")
        else:
            print("Erro na verificacao do arquivo")

        #conn.send_command("license install ...")

        ipdb.set_trace()