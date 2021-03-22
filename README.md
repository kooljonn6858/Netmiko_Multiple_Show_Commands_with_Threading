# Netmiko_Multiple_Show_Commands

This is a simple Netmiko script to gather multiple show commands output from multiple devices(Cisco in this case). The script allows to login to multiple devices simultaneously and gather the show commands output faster.

The device_list in the example is a txt file with hostnames or IP addresses.\
**Example:**\
R1\
R2\
R3\
10.1.1.1\
10.1.1.2


The show_commands in the example is another txt file with all the show commands. \
**Example:**\
show lldp neighbors\
show mac address-table\
show interfaces trunk\
show ip route\
show ipv6 route\
show ip int brief\
show vlan\
show ip dhcp snooping binding\
show ip arp inspection interface\
show authentication sessions\
show dot1x all\
show aaa servers\
show version\
show inventory\
show env all\
show clock\
show power inline\
show module\
show power detail


Useful to take logs of *prechecks* and *postchecks* before and after a network change.

Source:https://pypi.org/project/netmiko/
