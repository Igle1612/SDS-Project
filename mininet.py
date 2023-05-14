from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

class MyTopo(Topo):
    def __init__(self, **kwargs):
        Topo.__init__(self, **kwargs)

        # Create hosts
        h1 = self.addHost('h1', ip='10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.2')
        h3 = self.addHost('h3', ip='10.0.0.3')
        h4 = self.addHost('h4', ip='10.0.0.4')

        # Honeypot
        h5 = self.addHost('h5', ip='10.0.0.5')

        # Create switch
        s1 = self.addSwitch('s1')

        # Connect hosts to switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)

        # Create router
        r1 = self.addHost('r1', ip='192.168.1.1')

        # Connect router to switch
        self.addLink(r1, s1)
        self.addLink(r1, h5)

def setup():
    topo = MyTopo()

    net = Mininet(topo=topo, switch=OVSKernelSwitch, controller=RemoteController)

    net.start()

    # Set firewall rules for router
    r1 = net.getNodeByName('r1')
    r1.cmd('iptables -A FORWARD -s 10.0.0.0/24 -d 192.168.1.0/24 -j ACCEPT')
    r1.cmd('iptables -A FORWARD -s 192.168.1.0/24 -d 10.0.0.0/24 -j ACCEPT')
    r1.cmd('iptables -A FORWARD -d 10.0.0.5 -j DROP')
    r1.cmd('iptables -A FORWARD -j DROP')

    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup()