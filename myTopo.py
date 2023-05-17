from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSKernelSwitch, RemoteController

class Topo_SFC(Topo):
    def __init__(self):
        Topo.__init__(self)

        s1 = self.addSwitch('s1', dpid="0000000000000001")
        s2 = self.addSwitch('s2', dpid="0000000000000002")

        self.addLink(s1, s2, port1=1, port2=1)

        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        server1 = self.addHost('server1', ip='10.0.0.11/24')
        server2 = self.addHost('server2', ip='10.0.0.12/24')
        server3 = self.addHost('server3', ip='10.0.0.13/24')
        server4 = self.addHost('server4', ip='10.0.0.14/24')
        server5 = self.addHost('server5', ip='10.0.0.15/24')

        honeyPot = self.addHost('honeyPot', ip='10.0.0.16/24')

        self.addLink(s1, honeyPot, port1=16)
        self.addLink(s1, h1, port1=11)
        self.addLink(s1, h2, port1=12)

        self.addLink(s2, server1, port1=11)
        self.addLink(s2, server2, port1=12)
        self.addLink(s2, server3, port1=13)
        self.addLink(s2, server4, port1=14)
        self.addLink(s2, server5, port1=15)


def setup():
    topo = Topo_SFC()

    net = Mininet(topo=topo, switch=OVSKernelSwitch, controller=RemoteController)

    net.start()

    s1 = net.get('s1')

    #s1.cmd('ovs-ofctl add-flow s1 "table=0, priority=100, dl_dst=00:00:00:00:00:01, in_port=16, actions=CONTROLLER"')
    #s1.cmd('ovs-ofctl add-flow s1 "table=0, priority=100, dl_type=0x0800, nw_proto=6, in_port=16, tp_dst=80, actions=output:CONTROLLER"')
    #s1.cmd('ovs-ofctl add-flow s1 "table=0, priority=100, dl_type=0x0800, nw_proto=6, in_port=16, tp_dst=443, actions=output:CONTROLLER"')
    #s1.cmd('ovs-ofctl add-flow s1 "table=0, priority=0, actions=output:16"')

    net.interact()

    net.stop()



if __name__ == '__main__':
    setup()
