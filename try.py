from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.cli import CLI

class MyTopology(Topo):
    def build(self):
        h1 = self.addHost('h1', ip='10.0.0.59')

        # Crear un switch de nivel superior
        switch1 = self.addSwitch('s1', cls=OVSKernelSwitch)

        # Crear un router
        router = self.addNode('r1', cls=OVSKernelSwitch)

        # Crear un switch intermedio
        switch2 = self.addSwitch('s2', cls=OVSKernelSwitch)

        # Conectar el router al switch1
        self.addLink(router, switch1, intfName2='r1-eth1', params2={'ip': '10.0.0.1/24'})

        # Conectar el switch1 al switch2
        self.addLink(switch1, switch2)
        self.addLink(h1, router)

        # Agregar un enlace desde el honeypot al switch1
        honeypot = self.addHost('honeyPot', ip='10.0.0.16/24')
        self.addLink(honeypot, switch1)

        server1 = self.addHost('server1', ip='10.0.0.11')
        self.addLink(server1, switch2)
        server2 = self.addHost('server2', ip='10.0.0.12')
        self.addLink(server2, switch2)
        server3 = self.addHost('server3', ip='10.0.0.13')
        self.addLink(server3, switch2)
        server4 = self.addHost('server4', ip='10.0.0.14')
        self.addLink(server4, switch2)
        server5 = self.addHost('server5', ip='10.0.0.15')
        self.addLink(server5, switch2)

topo = MyTopology()
net = Mininet(topo=topo, link=TCLink, controller=None)
net.start()

switch2 = net.getNodeByName('s2')

switch2.cmd('ovs-vsctl set bridge s2 protocols=OpenFlow13')
switch2.cmd('ovs-ofctl add-flow s2 "priority=100,dl_type=0x800,nw_proto=6,tp_dst=80,action=mod_dl_dst=00:00:00:00:00:0{1},output:2"')
switch2.cmd('ovs-ofctl add-flow s2 "priority=100,dl_type=0x800,nw_proto=6,tp_dst=80,action=mod_dl_dst=00:00:00:00:00:0{2},output:3"')
switch2.cmd('ovs-ofctl add-flow s2 "priority=100,dl_type=0x800,nw_proto=6,tp_dst=80,action=mod_dl_dst=00:00:00:00:00:0{3},output:4"')
switch2.cmd('ovs-ofctl add-flow s2 "priority=100,dl_type=0x800,nw_proto=6,tp_dst=80,action=mod_dl_dst=00:00:00:00:00:0{4},output:5"')
switch2.cmd('ovs-ofctl add-flow s2 "priority=100,dl_type=0x800,nw_proto=6,tp_dst=80,action=mod_dl_dst=00:00:00:00:00:0{5},output:6"')

CLI(net)
net.stop()

