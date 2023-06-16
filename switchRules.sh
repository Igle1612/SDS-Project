sudo ovs-ofctl add-flow s0 "priority=50,actions=output:7" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "priority=100,ip,tcp,tp_dst=443,actions=normal" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "priority=100,ip,tcp,tp_dst=80,actions=normal" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "table=0, priority=100, dl_type=0x0806, actions=normal" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "table=0, priority=200, dl_type=0x0800, nw_src=192.168.1.2, actions=output:normal" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "table=0, priority=200, dl_type=0x0800, nw_src=192.168.1.201, actions=output:normal" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "table=0, priority=200, dl_type=0x0800, nw_src=192.168.1.202, actions=output:normal" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "table=0, priority=200, dl_type=0x0800, nw_src=192.168.1.203, actions=output:normal" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "table=0, priority=200, dl_type=0x0800, nw_src=192.168.1.204, actions=output:normal" -O OpenFlow13
sudo ovs-ofctl add-flow s0 "table=0, priority=200, dl_type=0x0800, nw_src=192.168.1.205, actions=output:normal" -O OpenFlow13
sudo ovs-ofctl dump-flows s0 -O OpenFlow13
