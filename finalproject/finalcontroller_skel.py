# Final Skeleton
#
# Hints/Reminders from Lab 3:
#
# To check the source and destination of an IP packet, you can use
# the header information... For example:
#
# ip_header = packet.find('ipv4')
#
# if ip_header.srcip == "1.1.1.1":
#   print "Packet is from 1.1.1.1"
#
# Important Note: the "is" comparison DOES NOT work for IP address
# comparisons in this way. You must use ==.
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
    # been made from Lab 3:
    #   - port_on_switch: represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet.
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    # You should use these to determine where a packet came from. To figure out where a packet 
    # is going, you can use the IP header information.

    ipv4 = packet.find('ipv4')
    icmp = packet.find('icmp')

    if ipv4:
        if icmp:
            if ipv4.srcip == "123.45.67.89": # if the data is coming from the untrusted host, drops packet
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 60
                self.connection.send(msg)
            else:
                if switch_id == 4:
                    if ipv4.dstip == "10.1.1.10":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 1))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    if ipv4.dstip == "10.2.2.20":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 2))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    if ipv4.dstip == "10.3.3.30":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 3))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    if ipv4.dstip == "10.5.5.50":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 4))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    if ipv4.dstip == "123.45.67.89":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 5))
                        msg.data = packet_in 
                        self.connection.send(msg)   
                elif switch_id != 4:
                    if port_on_switch == 9:     
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 8))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    else:
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 9))
                        msg.data = packet_in
                        self.connection.send(msg)
        else: 
            if ipv4.srcip == "123.45.67.89" and ipv4.dstip == "10.5.5.50": # if the untrusted host is sending data to server 1, drop it
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 60
                self.connection.send(msg)
            else:
                if switch_id == 4:
                    if ipv4.dstip == "10.1.1.10":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 1))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    if ipv4.dstip == "10.2.2.20":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 2))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    if ipv4.dstip == "10.3.3.30":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 3))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    if ipv4.dstip == "10.5.5.50":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 4))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    if ipv4.dstip == "123.45.67.89":
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 5))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                elif switch_id != 4:          
                    if port_on_switch == 9:     
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30 
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 8))
                        msg.data = packet_in 
                        self.connection.send(msg) 
                    else:
                        msg = of.ofp_flow_mod()
                        msg.match = of.ofp_match.from_packet(packet)
                        msg.idle_timeout = 30
                        msg.hard_timeout = 60
                        msg.actions.append(of.ofp_action_output(port = 9))
                        msg.data = packet_in
                        self.connection.send(msg)
    else: 
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 60
        msg.hard_timeout = 60
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
        msg.data = packet_in
        self.connection.send(msg)
    

#  if((ipv4 is None) and (icmp is None)):
#     msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
#    self.connection.send(msg)
#    else:
#      if switch_id is 4:
#        if ipv4.dstip == ("10.1.1.10"):
#          msg.actions.append(of.ofp_action_output(port = 1))
#        elif ipv4.dstip == ("10.2.2.20"):
#          msg.actions.append(of.ofp_action_output(port = 2))
#        elif ipv4.dstip == ("10.3.3.30"):
#          msg.actions.append(of.ofp_action_output(port = 3))
#        elif ipv4.dstip  == "123.45.67.89" and icmp is None:
#          msg.actions.append(of.ofp_action_output(port = 2))
#        elif ipv4.dstip == ("10.5.5.50"):
#          msg.actions.append(of.ofp_action_output(port = 4))
#      if switch_id is 5:
#        if port_on_switch == 9:
#          msg.actions.append(of.ofp_action_output(port = 8))
#        else:
#          msg.actions.append(of.ofp_action_output(port = 9))
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
