from __future__ import print_function

import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Intf
from mininet.node import Controller, RemoteController, OVSSwitch, OVSKernelSwitch

        
# Add controllers
c0 = RemoteController('c0', ip='127.0.0.1', port=6633)
c1 = RemoteController('c1', ip='127.0.0.1', port=6634)

cmap = {'s0': c0, 's1': c1}

class LinuxRouter( Node ):
    # Turns host into IP router
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

class MultiSwitch(OVSSwitch):
    def start(self, controllers):
        return OVSSwitch.start(self, [cmap[self.name]])

class NetworkTopo( Topo ):
    # Class that builds network topology consisting of four hosts, one router, three switches
    def build( self, **_opts ):

        s0 = self.addSwitch( 's0', ip='192.168.1.99', failMode='standalone', protocols='OpenFlow13', cls=MultiSwitch)

        s1 = self.addSwitch( 's1', ip='192.168.1.100', failMode='standalone', protocols='OpenFlow13', cls=MultiSwitch)

        self.addLink( s0, s1, intfName2='s0-s1', port1=6, port2=6 )

        #Add outter hosts
        hout1 = self.addHost( 'hout1', ip='192.168.1.201/24' )
        hout2 = self.addHost( 'hout2', ip='192.168.1.202/24' )
        hout3 = self.addHost( 'hout3', ip='192.168.1.203/24' )
        hout4 = self.addHost( 'hout4', ip='192.168.1.204/24' )
        hout5 = self.addHost( 'hout5', ip='192.168.1.205/24' )
        self.addLink(s0, hout1, port1=1)
        self.addLink(s0, hout2, port1=2)
        self.addLink(s0, hout3, port1=3)
        self.addLink(s0, hout4, port1=4)
        self.addLink(s0, hout5, port1=5)

        # Add honeypot
        honeyPot = self.addHost( 'honeyPot', ip='192.168.1.2/24')
        self.addLink(honeyPot, s0, port2=7)
    
        #Add Hosts
        h1 = self.addHost( 'h1', ip='192.168.1.101/24', mac='00:00:00:00:00:01' )
        h2 = self.addHost( 'h2', ip='192.168.1.102/24', mac='00:00:00:00:00:02' )
        h3 = self.addHost( 'h3', ip='192.168.1.103/24', mac='00:00:00:00:00:03' )
        h4 = self.addHost( 'h4', ip='192.168.1.104/24', mac='00:00:00:00:00:04' )
        h5 = self.addHost( 'h5', ip='192.168.1.105/24', mac='00:00:00:00:00:05' )
        
        self.addLink(s1, h1, port1=1)
        self.addLink(s1, h2, port1=2)
        self.addLink(s1, h3, port1=3)
        self.addLink(s1, h4, port1=4)
        self.addLink(s1, h5, port1=5)

def run():

    topo = NetworkTopo()
    
    net = Mininet( topo=topo, controller=None, switch=MultiSwitch )

    for c in [c0, c1]:
        net.addController(c)
        
    net.start()

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
