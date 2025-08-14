# eBGP vs. iBGP vs. OSPF

    Utilizado na aula [Context Manager e Exceptions Netmiko](https://autonetops.com/courses/admin/lesson/context-manager-except/)

## Objetivos de Aprendizado

Desafio levantado durante entrevista de emprego. Verificar desempate entre BGP e outros protocolos (OSPF) no cisco.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text"><strong>Pergunta:</strong> Um roteador aprende um prefixo x.x.x.x/x de três formas diferentes (eBGP, iBGP com LP 400 e via OSPF) qual rota será instalada na tabela de roteamento?</div>
</div>

## Topologia

Topologia proposta para validação.
![topologia](https://ubjpcyfllztpftxqaldu.supabase.co/storage/v1/object/sign/img/labs/lab/topologia/autonetops_bgp_ospf.webp?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJpbWcvbGFicy9sYWIvdG9wb2xvZ2lhL2F1dG9uZXRvcHNfYmdwX29zcGYud2VicCIsImlhdCI6MTc0NjM2ODU3MSwiZXhwIjoyMDYxNzI4NTcxfQ.UNYLk165qtJhduoWrgKul_7aBBv5P0h3lX0TPDKhoXw)

## Resposta

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text"><strong>OSPF</strong>: Por que?</div>
</div>