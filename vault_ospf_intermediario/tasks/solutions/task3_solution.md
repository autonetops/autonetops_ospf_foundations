R2:
route-map MED permit 10
  set metric 100
!
route-map MED permit 100
!
clear ip bgp * out


R4:
ip prefix-list NET33 permit 33.3.3.3/32
!
route-map MED permit 10
match ip address prefix-list NET33
set metric 50
!
route-map MED permit 100
set metric 200
! MED 200 para todas as outras redes
!
router bgp 200
neighbor 192.168.14.1 route-map MED out
!
clear ip bgp * out