## Cenário

Você é um engenheiro de redes familiarizado com OSPF em área única, mas nunca explorou configurações multiárea ou enfrentou desafios avançados como manipulação de métricas, autenticação ou áreas especiais. Além disso, você ouviu falar de automação de redes com ferramentas como **Netmiko**, mas nunca a aplicou em um cenário real. Neste laboratório, você vai ligar seus roteadores usando automação para configurar um ambiente OSPF multiárea, enfrentando situações práticas e avançadas que testarão seu domínio do protocolo.

## Topologia
![topologia-ospf](https://ubjpcyfllztpftxqaldu.supabase.co/storage/v1/object/sign/img/labs/lab/md/dominando-ospf-multiarea-com-automacao.webp?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJpbWcvbGFicy9sYWIvbWQvZG9taW5hbmRvLW9zcGYtbXVsdGlhcmVhLWNvbS1hdXRvbWFjYW8ud2VicCIsImlhdCI6MTc0MjU2MzAyNiwiZXhwIjoxOTAwMjQzMDI2fQ.ZFJbbNiECXBaSoZlekNr_hQYBjt3JRL01ZvIoFznml0)

### Conceitos e Desafios de OSPF Destacados

1. **Multiárea**: Exploração de Área 0, Área 1 (NSSA) e Área 2.
2. **Métricas e Largura de Banda**: Influência indireta na métrica via largura de banda.
3. **Autenticação**: Comparação entre texto claro e MD5.
4. **Temporizadores**: Impacto na estabilidade da adjacência.
5. **Sumarização**: Redução de entradas na tabela de roteamento.
6. **NSSA**: Introdução de rotas externas em áreas restritas.
7. **Resiliência**: Teste de reconvergência após falha de enlace.

## Objetivo

Configure um ambiente OSPF multiárea robusto **usando automação de rede com Netmiko** (biblioteca Python para automação via SSH). Todas as tarefas devem ser realizadas via scripts Python, garantindo conectividade total e explorando conceitos avançados de OSPF. Aqui estão os desafios.


### Ferramentas e Automação

* **Netmiko**: Use esta biblioteca Python para enviar comandos de configuração e validação aos roteadores via SSH. Exemplo básico:
    
``` python
    
    from netmiko import ConnectHandler
    
    device = {
        'device_type': 'arista_eos', # ou 'cisco_ios'
        'host': '172.20.20.11',
        'username': 'admin',
        'password': 'admin'
    }
    
    net_connect = ConnectHandler(**device)
    config_commands = [
        'router ospf 1',
        'router-id 1.1.1.2',
        'network 172.20.20.0 0.0.0.255 area 0'
    ]
    net_connect.send_config_set(config_commands)
    output = net_connect.send_command('show ip ospf neighbor')
    print(output)
```