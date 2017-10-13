# Payam Katoozian
# CMPE 150L
# 12/8/2016
# Final Project
# finalcontroller.py
# controller file

# Final Skeleton
#
# Hints/Reminders from Lab 4:
# 
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the 
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. The following modifications have 
    # been made from Lab 4:
    #   - port_on_switch represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)

    # Goals:
    # All hosts able to communicate, EXCEPT:
    #   Untrusted host cannot send ICMP traffic to host 10,20,30, or Server 1
    #   Untrusted host cannot sent any IP traffic to Server 1
	msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)
    msg.idle_timeout = 30
    msg.hard_timeout = 60
    msg.data = packet_in 
    self.connection.send(msg)
    ipv4 = packet.find('ipv4')
    icmp = packet.find('icmp')

    if icmp: # icmp handler
    	if ipv4.srcip == '123.45.67.89': # if the data is coming from the untrusted host, drop it
    		print "Dropping ICMP packet"
    	else: # the data is from the internal network
    		if switch_id == 4: # if the switch is the core switch
    			if ipv4.dstip == '10.1.1.10':
    				msg.actions.append(of.ofp_action_output(port = 1))
                if ipv4.dstip == '10.2.2.20':
                    msg.actions.append(of.ofp_action_output(port = 2))
                if ipv4.dstip == '10.3.3.30':
                    msg.actions.append(of.ofp_action_output(port = 3))
                if ipv4.dstip == '10.5.5.50':
                    msg.actions.append(of.ofp_action_output(port = 4))
                if ipv4.dstip == '123.45.67.89':
                    msg.actions.append(of.ofp_action_output(port = 2))
            elif switch_id != 4: # if the switch is not the core switch
                if port_on_switch == 9:     
                    msg.actions.append(of.ofp_action_output(port = 8))
                else:
                    msg.actions.append(of.ofp_action_output(port = 9))
                        
    else: # IPv4 handler
            # if the untrusted host is sending data to server 1, drop it
        if ipv4.srcip == '172.16.10.100' and ipv4.dstip == '10.0.4.10':
        	print "Dropping IPv4 packet"
        else: # route everything else properly
        	if switch_id == 4: # if the switch is the core switch
    			if ipv4.dstip == '10.1.1.10':
    				msg.actions.append(of.ofp_action_output(port = 1))
                if ipv4.dstip == '10.2.2.20':
                    msg.actions.append(of.ofp_action_output(port = 2))
                if ipv4.dstip == '10.3.3.30':
                    msg.actions.append(of.ofp_action_output(port = 3))
                if ipv4.dstip == '10.5.5.50':
                    msg.actions.append(of.ofp_action_output(port = 4))
                if ipv4.dstip == '123.45.67.89':
                    msg.actions.append(of.ofp_action_output(port = 2))
            elif switch_id != 4: # if the switch is not the core switch
                if port_on_switch == 9:     
                    msg.actions.append(of.ofp_action_output(port = 8))
                else:
                    msg.actions.append(of.ofp_action_output(port = 9))
   
  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
