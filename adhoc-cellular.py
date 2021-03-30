#!/usr/bin/python

"""
This example shows on how to enable the adhoc mode
Alternatively, you can use the manet routing protocol of your choice
"""

import sys

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology(args):
    "Create a network."
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    kwargs = dict()
    if '-a' in args:
        kwargs['range'] = 100

    sta1 = net.addStation('sta1', ip='10.0.0.1', position='-70,121,0', **kwargs)
    sta2 = net.addStation('sta2', ip='10.0.0.2', position='0,121,0', **kwargs)
    sta3 = net.addStation('sta3', ip='10.0.0.3', position='70,121,0', **kwargs)
    sta4 = net.addStation('sta4', ip='10.0.0.4', position='-105,61,0', **kwargs)
    sta5 = net.addStation('sta5', ip='10.0.0.5', position='-35,61,0', **kwargs)
    sta6 = net.addStation('sta6', ip='10.0.0.6', position='35,61,0', **kwargs)
    sta7 = net.addStation('sta7', ip='10.0.0.7', position='105,61,0', **kwargs)
    sta8 = net.addStation('sta8', ip='10.0.0.8', position='-140,0,0', **kwargs)
    sta9 = net.addStation('sta9', ip='10.0.0.9', position='-70,0,0', **kwargs)
    sta10 = net.addStation('sta10', ip='10.0.0.10', position='0,0,0', **kwargs)
    sta11 = net.addStation('sta11', ip='10.0.0.11', position='70,0,0', **kwargs)
    sta12 = net.addStation('sta12', ip='10.0.0.12', position='140,0,0', **kwargs)
    sta13 = net.addStation('sta13', ip='10.0.0.13', position='-105,-61,0', **kwargs)
    sta14 = net.addStation('sta14', ip='10.0.0.14', position='-35,-61,0', **kwargs)
    sta15 = net.addStation('sta15', ip='10.0.0.15', position='35,-61,0', **kwargs)
    sta16 = net.addStation('sta16', ip='10.0.0.16', position='105,-61,0', **kwargs)
    sta17 = net.addStation('sta17', ip='10.0.0.17', position='-70,-121,0', **kwargs)
    sta18 = net.addStation('sta18', ip='10.0.0.18', position='0,-121,0', **kwargs)
    sta19 = net.addStation('sta19', ip='10.0.0.19', position='70,-121,0', **kwargs)

    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    protocols = ['olsr']
    kwargs = dict()
    for proto in args:
        if proto in protocols:
            kwargs['proto'] = proto

    net.addLink(sta1, cls=adhoc, intf='sta1-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta2, cls=adhoc, intf='sta2-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta3, cls=adhoc, intf='sta3-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta4, cls=adhoc, intf='sta4-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta5, cls=adhoc, intf='sta5-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta6, cls=adhoc, intf='sta6-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta7, cls=adhoc, intf='sta7-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta8, cls=adhoc, intf='sta8-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta9, cls=adhoc, intf='sta9-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta10, cls=adhoc, intf='sta10-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta11, cls=adhoc, intf='sta11-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta12, cls=adhoc, intf='sta12-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta13, cls=adhoc, intf='sta13-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta14, cls=adhoc, intf='sta14-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta15, cls=adhoc, intf='sta15-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta16, cls=adhoc, intf='sta16-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta17, cls=adhoc, intf='sta17-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta18, cls=adhoc, intf='sta18-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta19, cls=adhoc, intf='sta19-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)

    net.plotGraph(max_x=250, min_x=-250, max_y=250, min_y=-250)
    info("*** Starting network\n")
    net.build()

    info("\n*** Addressing...\n")

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
