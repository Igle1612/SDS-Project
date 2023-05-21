# SDS-Project

To execute and create the topo we must use `sudo python2 createFullTopo.py`

LoadBalancer:
In other console execute `ryu-manager load_balancer.py`
Then, in he mininet:
`xterm h1 h2 h3 h4 h5 `
And for each server:
`python3 -m http.server 80`

To test: `hout2 curl 192.168.1.100`

TODO:



Arnau Gris Garcia:
- Traffic Simulator
- Attacks

Sergi Ger Roca:
- load balancer
- Network Topology

Marc Igle:
- Honeypot
- Mininet setup

Pau:
- influxdb
- router with firewall
- grafana
