sudo ip link add name s0-snort type dummy
sudo ip link set s0-snort up
sudo ovs-vsctl add-port s0 s0-snort
