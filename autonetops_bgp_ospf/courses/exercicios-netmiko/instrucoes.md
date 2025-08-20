1. **Exercício 1 (TextFSM):** Conecte-se a `r2` e use TextFSM para parsear a saída de `show ip route`. Crie um script que imprima apenas as rotas OSPF (`O`) e seus respectivos `next_hop`.

2. **Exercício 2 (Genie):** Use Genie em `r1` para obter as informações de BGP (`show bgp all summary`). Escreva um código que itere sobre os vizinhos e imprima uma mensagem de alerta se o estado de alguma sessão não for `Established`.

3. **Exercicio Final:** Crie um script de "Auditoria de Rede". O script deve:

    * Conectar-se a `r1`, `r2` e `r3`.

    * Para cada roteador, executar os seguintes comandos e parsear a saída usando a ferramenta mais apropriada:

        * `show version` (Use Genie)

        * `show ip interface brief` (Use TextFSM)

        * `show ip ospf` (Use Genie)

    * Armazenar todos os dados coletados em uma única estrutura de dados Python

    * No final, salvar em um arquivo chamado `auditoria_rede.json`.