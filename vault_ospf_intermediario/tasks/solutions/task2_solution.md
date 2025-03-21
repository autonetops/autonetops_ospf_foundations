
R2:
route-map MED permit 10
  set metric 100
!
router bgp 200
  neigh 192.168.12.1 route-map MED out
!
clear ip bgp * out