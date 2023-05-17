from mininet.net import Mininet
from mininet.cli import CLI
net = Mininet(topo = None)
s1 = net.addSwitch('s1')
h1 = net.addHost('h1', ip = '10.0.0.1')
h2 = net.addHost('h2', ip = '10.0.0.2')
net.addLink(s1, h1)
net.addLink(s1, h2)

h1.cmd('route add -net 10.0.0.0/24 gw 10.0.0.1 dev h1-eth0')
h2.cmd('route add -net 10.0.0.0/24 gw 10.0.0.2 dev h2-eth0')

net.start()
CLI(net)
net.stop()
