from __future__ import print_function

import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Intf
from mininet.node import Controller, RemoteController, OVSKernelSwitch

class LinuxRouter( Node ):
    # Turns host into IP router
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

class NetworkTopo( Topo ):
    # Class that builds network topology consisting of four hosts, one router, three switches
    def build( self, **_opts ):

        router = self.addNode( 'r0', ip='192.168.1.1/24', protocols='OpenFlow13', cls=LinuxRouter )

        s0 = self.addSwitch( 's0', ip='192.168.1.99', failMode='standalone', protocols='OpenFlow13' )

        s1 = self.addSwitch( 's1', ip='192.168.1.100', failMode='standalone', protocols='OpenFlow13' )

        self.addLink( s0, router, port1=1, intfName2='r0-eth1', params2={ 'ip' : '192.168.1.1/24' } )
        self.addLink( s0, s1, port1=2, port2=1 )

        #Add outter hosts
        hout1 = self.addHost( 'hout1', ip='10.0.1.10/24', defaultRoute='via 10.0.1.1' )
        hout2 = self.addHost( 'hout2', ip='10.0.2.10/24', defaultRoute='via 10.0.2.1' )
        hout3 = self.addHost( 'hout3', ip='10.0.3.10/24', defaultRoute='via 10.0.3.1' )
        hout4 = self.addHost( 'hout4', ip='10.0.4.10/24', defaultRoute='via 10.0.4.1' )
        hout5 = self.addHost( 'hout5', ip='10.0.5.10/24', defaultRoute='via 10.0.5.1' )
        self.addLink( hout1, router, intfName2='r0-eth2', params2={ 'ip' : '10.0.1.1/24' })
        self.addLink( hout2, router, intfName2='r0-eth3', params2={ 'ip' : '10.0.2.1/24' })
        self.addLink( hout3, router, intfName2='r0-eth4', params2={ 'ip' : '10.0.3.1/24' })
        self.addLink( hout4, router, intfName2='r0-eth5', params2={ 'ip' : '10.0.4.1/24' })
        self.addLink( hout5, router, intfName2='r0-eth6', params2={ 'ip' : '10.0.5.1/24' })

        # Add honeypot
        honeyPot = self.addHost( 'honeyPot', ip='192.168.1.2/24', defaultRoute='via 192.168.1.1')
        self.addLink(honeyPot, s0, port2=3)
    
        #Add Hosts
        h1 = self.addHost( 'h1', ip='192.168.1.101/24', defaultRoute='via 192.168.1.1', mac='00:00:00:00:00:01' )
        h2 = self.addHost( 'h2', ip='192.168.1.102/24', defaultRoute='via 192.168.1.1', mac='00:00:00:00:00:02' )
        h3 = self.addHost( 'h3', ip='192.168.1.103/24', defaultRoute='via 192.168.1.1', mac='00:00:00:00:00:03' )
        h4 = self.addHost( 'h4', ip='192.168.1.104/24', defaultRoute='via 192.168.1.1', mac='00:00:00:00:00:04' )
        h5 = self.addHost( 'h5', ip='192.168.1.105/24', defaultRoute='via 192.168.1.1', mac='00:00:00:00:00:05' )
        
        self.addLink(s1, h1, port1=11)
        self.addLink(s1, h2, port1=12)
        self.addLink(s1, h3, port1=13)
        self.addLink(s1, h4, port1=14)
        self.addLink(s1, h5, port1=15)

def run():

    topo = NetworkTopo()
    
    net = Mininet( topo=topo, controller=RemoteController, switch=OVSKernelSwitch )

    net.start()
    # router = net.getNodeByName('r0')
    # router.cmd('iptables -t nat -A PREROUTING -i r0-eth2 -d 10.0.1.1 -j DNAT --to-destination 192.168.1.1')
    # router.cmd('ip route add default via 192.168.1.1')
    # router.cmd('ip route add 192.168.1.0/24 via 192.168.1.1')

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
