from N2G import drawio_diagram

# Criar objeto de diagrama Draw.io
diagram = drawio_diagram()

# Adicionar página ao diagrama
diagram.add_diagram("OSPF Multiárea Lab")

# Estilos personalizados para nós e links
router_style = "shape=mxgraph.cisco.routers.router;html=1;fillColor=#036897;strokeColor=#ffffff;strokeWidth=2;"
link_style = "endArrow=block;html=1;strokeWidth=2;strokeColor=#000000;dashed=0;"

# Adicionar nós (roteadores) com IPs de gerenciamento e estilo
diagram.add_node(id="R1", label="\nR1", style=router_style, width=80, height=80)
diagram.add_node(id="R2", label="\nR2", style=router_style, width=80, height=80)
diagram.add_node(id="R3", label="\nR3", style=router_style, width=80, height=80)
diagram.add_node(id="R4", label="\nR4", style=router_style, width=80, height=80)
diagram.add_node(id="Area0", label="\nArea0", style="shape=rectangle;fillColor=#02C1D8;strokeColor=#000000;", width=100, height=60)


# Adicionar links baseados na topologia do Containerlab
diagram.add_link(source="R1", target="R2", label="eth1-eth1\nArea 1 (NSSA)", style=link_style)
diagram.add_link(source="R2", target="R3", label="eth2-eth1\nArea 0", style=link_style)
diagram.add_link(source="R3", target="R4", label="eth2-eth1\nArea 0", style=link_style)
diagram.add_link(source="R1", target="R4", label="eth2-eth2\nArea 0", style=link_style)

# Adicionar dados extras (exemplo: autenticação e temporizadores)
diagram.add_node(id="R2-R3", label="Auth: Cleartext\nHello: 10s, Dead: 60s", style="shape=ellipse;fillColor=#f8cecc;strokeColor=#000000;", width=60, height=40)
diagram.add_link(source="R2", target="R2-R3", style="dashed=1;strokeColor=#000000;")
diagram.add_link(source="R2-R3", target="R3", style="dashed=1;strokeColor=#000000;")

diagram.add_node(id="R3-R4", label="Auth: MD5", style="shape=ellipse;fillColor=#f8cecc;strokeColor=#000000;", width=60, height=40)
diagram.add_link(source="R3", target="R3-R4", style="dashed=1;strokeColor=#000000;")
diagram.add_link(source="R3-R4", target="R4", style="dashed=1;strokeColor=#000000;")

# Adicionar loopbacks de R4 como nós adicionais (Área 2 e sumarização)
diagram.add_node(id="R4-LB", label="Area 2\nLoopbacks\n10.0.30.0/22", style="shape=rectangle;fillColor=#ff7e5f;strokeColor=#000000;", width=100, height=60)

# Adicionar Loopback14 (não anunciada no OSPF)
diagram.add_node(id="R4-LB14", label="Loopback14\n10.0.34.1/24\n(Rota Estática)", style="shape=rectangle;fillColor=#ff7e5f;strokeColor=#000000;", width=100, height=60)
diagram.add_link(source="R4", target="R4-LB14", label="Static", style="dashed=1;strokeColor=#000000;")

# Aplicar layout automático (opcional, ajustável no Draw.io)
diagram.layout(algo="kk")

# Exportar o arquivo Draw.io
diagram.dump_file(filename="ospf_multiarea_lab.drawio", folder="./")
print("Topologia gerada com sucesso! Arquivo salvo como 'ospf_multiarea_lab.drawio'")