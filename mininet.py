from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo

# Create a network with a single switch and 4 hosts
net = Mininet(topo=SingleSwitchTopo(4))

# Start the network
net.start()

# Open an xterm window for each host
for host in net.hosts:
    host.cmd('xterm &')

# Wait for the user to close the xterm windows
input('Press enter to shutdown the network...')

# Stop the network
net.stop()

from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo

# Create a network with a single switch and 4 hosts
net = Mininet(topo=SingleSwitchTopo(4))

# Start the network
net.start()

# Open an xterm window for each host
for host in net.hosts:
    host.cmd('xterm &')

# Wait for the user to close the xterm windows
input('Press enter to shutdown the network...')

# Stop the network
net.stop()
