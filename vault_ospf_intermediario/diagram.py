from N2G import drawio_diagram

# Criar objeto de diagrama Draw.io
diagram = drawio_diagram()

# Adicionar página ao diagrama
diagram.add_diagram("OSPF Multiárea Lab")

# Estilos personalizados para nós e links
router_style = "shape=mxgraph.cisco.routers.router;html=1;fillColor=#036897;strokeColor=#ffffff;strokeWidth=2;"
link_style = "endArrow=block;html=1;strokeWidth=2;strokeColor=#FF3399;dashed=0;"

# Adicionar nós (roteadores) com IPs de gerenciamento e estilo
diagram.add_node(id="R1", label="R1\n172.20.20.11", style=router_style, width=80, height=80)
diagram.add_node(id="R2", label="R2\n172.20.20.12", style=router_style, width=80, height=80)
diagram.add_node(id="R3", label="R3\n172.20.20.13", style=router_style, width=80, height=80)
diagram.add_node(id="R4", label="R4\n172.20.20.14", style=router_style, width=80, height=80)

# Adicionar links baseados na topologia do Containerlab
diagram.add_link(source="R1", target="R2", label="eth1-eth1\nArea 1 (NSSA)", style=link_style)
diagram.add_link(source="R2", target="R3", label="eth2-eth1\nArea 0", style=link_style)
diagram.add_link(source="R3", target="R4", label="eth2-eth1\nArea 0", style=link_style)
diagram.add_link(source="R1", target="R4", label="eth2-eth2\nArea 0", style=link_style)

# Adicionar dados extras (exemplo: autenticação e temporizadores)
diagram.add_node(id="R2-R4", label="Auth: Cleartext\nHello: 10s, Dead: 60s", style="shape=ellipse;fillColor=#f8cecc;strokeColor=#FF3399;", width=60, height=40)
diagram.add_link(source="R2", target="R2-R4", style="dashed=1;strokeColor=#000000;")
diagram.add_link(source="R2-R4", target="R4", style="dashed=1;strokeColor=#000000;")

diagram.add_node(id="R3-R4", label="Auth: MD5", style="shape=ellipse;fillColor=#f8cecc;strokeColor=#FF3399;", width=60, height=40)
diagram.add_link(source="R3", target="R3-R4", style="dashed=1;strokeColor=#000000;")
diagram.add_link(source="R3-R4", target="R4", style="dashed=1;strokeColor=#000000;")

# Adicionar loopbacks de R4 como nós adicionais (Área 2 e sumarização)
diagram.add_node(id="R4-LB", label="Loopbacks R4\n172.16.0.0/22 (Area 2)", style="shape=rectangle;fillColor=#FFD700;strokeColor=#000000;", width=100, height=60)
diagram.add_link(source="R4", target="R4-LB", label="Area 2", style=link_style)

# Adicionar Loopback14 (não anunciada no OSPF)
diagram.add_node(id="R4-LB14", label="Loopback14\n172.16.4.1/24\n(Rota Estática)", style="shape=rectangle;fillColor=#FFD700;strokeColor=#000000;", width=100, height=60)
diagram.add_link(source="R4", target="R4-LB14", label="Static", style="dashed=1;strokeColor=#000000;")

# Aplicar layout automático (opcional, ajustável no Draw.io)
diagram.layout(algo="kk")

# Exportar o arquivo Draw.io
diagram.dump_file(filename="ospf_multiarea_lab.drawio", folder="./")
print("Topologia gerada com sucesso! Arquivo salvo como 'ospf_multiarea_lab.drawio'")