## Tarefas

Neste diretório possuimos o arquivo **topology.yaml** que servirá como referencia para realizarmos nossas atividades de automação.

1. **Configuração Inicial do OSPF**
    
    * Ative o OSPF em todos os roteadores usando o processo ID 1.
    * Todas as redes inicialmente devem estar na **Área 0**, exceto onde especificado.
    * Garanta que qualquer IP possa ser pingado de qualquer roteador.

    > python3 solutions/task1_solution.py
        
2. **Personalização do Router-ID**
    
    * Defina manualmente o Router-ID de R1 como **11.11.11.11** via script Netmiko.
    * Verifique em R2 e R4 (usando show ip ospf neighbor) se o Router-ID foi atualizado. Obs: **clear ip ospf process**

    > python3 solutions/task2_solution.py
        
3. **Controle do Designated Router (DR)**
    
    * Configure R3 como o **Designated Router (DR)** no segmento entre R2 e R3 (link eth2 de R2 e eth1 de R3). Ajuste a prioridade OSPF para garantir isso.

    > python3 solutions/task3_solution.py
        
4. **Manipulação de Métricas**
    
    * Altere a métrica no enlace entre R1 e R2 (eth1) **sem usar ip ospf cost**. Use a largura de banda da interface para influenciar a métrica.
    * Ajuste a largura de banda de referência (reference bandwidth) em todos os roteadores para **1500** via automação.
        
    > python3 solutions/task4_solution.py

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
   