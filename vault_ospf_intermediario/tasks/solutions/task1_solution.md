R1:
router bgp 100
  network 1.1.1.1 mask 255.255.255.255
  network 11.1.1.1 mask 255.255.255.255
  
  neighbor 192.168.12.2 remote-as 200
  neighbor 192.168.14.4 remote-as 200


R2:
router bgp 200
  neighbor 192.168.12.1 remote-as 100
  neighbor 192.168.23.3 remote-as 200
  neighbor 192.168.23.3 next-hop-self
  neighbor 192.168.34.4 remote-as 200
  neighbor 192.168.34.4 next-hop-self
  
  network 2.2.2.2 mask 255.255.255.255
  network 22.2.2.2 mask 255.255.255.255

R3:
router bgp 200
  neighbor 192.168.23.2 remote-as 200
  neighbor 192.168.23.2 next-hop-self
  neighbor 192.168.34.4 remote-as 200
  neighbor 192.168.34.4 next-hop-self
  
  network 3.3.3.3 mask 255.255.255.255
  network 33.3.3.3 mask 255.255.255.255

R4:
router bgp 200
  neighbor 192.168.14.1 remote-as 100

  neighbor 192.168.23.2 remote-as 200
  neighbor 192.168.23.2 next-hop-self
  neighbor 192.168.34.3 remote-as 200
  neighbor 192.168.34.3 next-hop-self
  
  network 4.4.4.4 mask 255.255.255.255
  network 44.4.4.4 mask 255.255.255.255
