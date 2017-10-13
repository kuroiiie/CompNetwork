#a!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

# Payam Katoozian
# 12/8/2016
# CMPE 150L
# Final Project
# final.py
# Topology file

class final_topo(Topo):
  def build(self):
    
    # Examples!
    # Create a host with a default route of the ethernet interface. You'll need to set the
    # default gateway like this for every host you make on this assignment to make sure all 
    # packets are sent out that port. Make sure to change the h# in the defaultRoute area
    # and the MAC address when you add more hosts!

    #Add 5 hosts: h10-h30, untrusted host, and server
    h1 = self.addHost('h1',mac='00:00:00:00:00:10',ip='10.0.1.10/24', defaultRoute="h1-eth0")

    h2 = self.addHost('h2',mac='00:00:00:00:00:20',ip='10.0.2.20/24', defaultRoute="h2-eth0")

    h3 = self.addHost('h3',mac='00:00:00:00:00:30',ip='10.0.3.30/24', defaultRoute="h3-eth0")

    h4 = self.addHost('h4',mac='00:00:00:00:00:40',ip='10.0.4.10/24', defaultRoute="h4-eth0")

    h5 = self.addHost('h5',mac='00:00:00:00:00:50',ip='172.16.10.100/24', defaultRoute="h5-eth0")

    # Create a switch. No changes here from Lab 1.5 switches total.
    s1 = self.addSwitch('s1') # floor 1

    s2 = self.addSwitch('s2') # floor 2

    s3 = self.addSwitch('s3') # floor 3

    s4 = self.addSwitch('s4') # data center switch

    s5 = self.addSwitch('s5') # core switch

    # Connect Port 8 on the Switch to Port 0 on Host 1 and Port 9 on the Switch to Port 0 on 
    # Host 2. This is representing the physical port on the switch or host that you are 
    # connecting to.
    self.addLink(s1,h1, port1=8, port2=0) #switch 1 --> host 1

    self.addLink(s2,h2, port1=8, port2=0) #switch 2 --> host 2

    self.addLink(s3,h3, port1=8, port2=0) #switch 3 --> host 3

    self.addLink(s5,s1, port1=1, port2=9) #core switch --> switch 1

    self.addLink(s5,s2, port1=2, port2=9) #core switch --> switch 2

    self.addLink(s5,s3, port1=3, port2=9) #core switch --> switch 3

    self.addLink(s5,s4, port1=4, port2=9) #core switch --> data center switch

    self.addLink(s5,h5, port1=5, port2=0) #core switch --> untrusted host

    self.addLink(s4,h4, port1=8, port2=0) #data center switch --> server

def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()

  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
