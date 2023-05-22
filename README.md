# SDS-Project

To execute and create the topo we must use `sudo python2 createFullTopo.py`

LoadBalancer:
In other console execute `ryu-manager --ofp-tcp-listen-port 6634 load_balancer.py`
Then, in he mininet:
`xterm h1 h2 h3 h4 h5 `
And for each server:
`python3 -m http.server 80`

To test: `hout2 curl 192.168.1.100`

Monitor:
In other console execute `ryu-manager --ofp-tcp-listen-port 6633 monitor_telegraf.py`

Snort:

To execute snort we must execute `sudo snort -i s0-snort -A unsock -l /tmp -c /etc/snort/snort.conf`

First we create the interface: `sudo ip link add name s0-snort type dummy`
`sudo ip link set s0-snort up`
`sudo ovs-vsctl add-port s0 s0-snort`

To check the port number: `sudo ovs-ofctl show s0`

Then to execute ryu we use: `sudo ryu-manager ../../ryu/ryu/app/simple_switch_snort.py`

To attack it then we use: `hping3 -c 10000 -d 120 -S -w 64 -p 80 --faster --rand-source 10.0.1.1`
`hping3 -V -1 -d 1400 --faster 10.0.1.1`

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
