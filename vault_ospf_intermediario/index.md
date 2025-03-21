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

Configure um ambiente OSPF multiárea robusto **usando automação de rede com Netmiko** (biblioteca Python para automação via SSH). Todas as tarefas devem ser realizadas via scripts Python, garantindo conectividade total e explorando conceitos avançados de OSPF. Aqui estão os desafios:

1. **Configuração Inicial do OSPF**
    
    * Ative o OSPF em todos os roteadores usando o processo ID 1.
    * Todas as redes inicialmente devem estar na **Área 0**, exceto onde especificado.
    * Garanta que qualquer IP possa ser pingado de qualquer roteador.
        
2. **Personalização do Router-ID**
    
    * Defina manualmente o Router-ID de R1 como **1.1.1.2** via script Netmiko.
    * Verifique em R2 e R3 (usando show ip ospf neighbor) se o Router-ID foi atualizado.
        
3. **Controle do Designated Router (DR)**
    
    * Configure R3 como o **Designated Router (DR)** no segmento entre R2 e R3 (link eth2 de R2 e eth1 de R3). Ajuste a prioridade OSPF para garantir isso.
        
4. **Manipulação de Métricas**
    
    * Altere a métrica no enlace entre R1 e R2 (eth1) **sem usar ip ospf cost**. Use a largura de banda da interface para influenciar a métrica.
    * Ajuste a largura de banda de referência (reference bandwidth) em todos os roteadores para **1500** via automação.
        
5. **Autenticação OSPF**
    
    * Habilite autenticação em texto claro entre R2 e R3 com a senha **"ospf123"**.
    * Habilite autenticação MD5 entre R3 e R4 com a chave **1** e senha **"md5ospf"**.
        
6. **Temporizadores OSPF**
    
    * No enlace entre R2 e R3, configure o temporizador **hello** para **10 segundos** e o **dead-interval** para **60 segundos**. Teste a resiliência da adjacência.
        
7. **Roteamento Padrão**
    
    * Insira uma rota padrão (**0.0.0.0/0**) em R3 e propague-a via OSPF para R1, R2 e R4.
        
8. **Simulação de Falha**
    
    * Desative (shutdown) o enlace entre R2 e R3 e verifique como o OSPF reconverge.
        
9. **Área 1 - NSSA**
    
    * Configure o enlace entre R1 e R2 (eth1) e a interface **Loopback0** de R2 como pertencentes à **Área 1**.
        
    * Defina a Área 1 como uma **NSSA (Not So Stubby Area)** e injete uma rota externa (ex.: 10.0.0.0/24) via R2 para demonstrar o conceito.
        
10. **Área 2 - Sumário**
    
    * Configure a interface **Loopback0** de R4 como pertencente à **Área 2**.
    * Crie 4 loopbacks em R3:
        
        * Loopback30: **10.0.30.1 /24**
        * Loopback31: **10.0.31.1 /24**
        * Loopback32: **10.0.32.1 /24**
        * Loopback33: **10.0.33.1 /24**
            
    * Anuncie essas redes na Área 2 e use sumarização para que apenas **10.0.0.0/22** apareça nas tabelas de R1, R2 e R4.
        
11. **Desafio de Roteamento Criativo**
    
    * Crie uma Loopback34 em R3: **10.0.34.0 /24**.
    * **Não anuncie essa rede no OSPF nem use redistribuição.** Configure uma rota estática em R4 e propague-a de forma criativa (ex.: rota condicional ou PBR) para que outros roteadores a alcancem.
        
12. **Validação Automatizada**
    
    * Use Netmiko para executar comandos como show ip ospf database, show ip route, e ping em todos os roteadores, validando automaticamente a conectividade e as configurações.
        

### Ferramentas e Automação

* **Netmiko**: Use esta biblioteca Python para enviar comandos de configuração e validação aos roteadores via SSH. Exemplo básico:
    
``` python
    
    from netmiko import ConnectHandler
    
    device = {
        'device_type': 'arista_eos', # ou 'cisco_ios'
        'ip': '172.20.20.11',
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
    
* Automatize todas as tarefas em um script modular para cada roteador e valide os resultados.
    