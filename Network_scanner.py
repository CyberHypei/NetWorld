#!/usr/bin/env python

import scapy.all as scapy
import optparse

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

	clients_list = []
	for element in answered_list:
		clients_dict = {"ip":element[1].psrc,"mac":element[1].hwsrc}
		clients_list.append(clients_dict)
		#print(element[1].hwsrc+ "\t\t" +element[1].psrc)
		#print("The associated MAC Address is "element[1].hwsrc)
		#print("---------------------------------------------------------------------------------------------------------------------------------------------")

def print_result(results_list):
	print("MAC Address \t\t\t at IP Address\n--------------------------------------------------------------------------- ")
	for client in results_list:
		print(client[ip] +\t\t+ client[mac])


def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-r","--range",dest="range",help="Range of IP address to be scanned")
	#parser.add_option("-i","--",dest="",help="")
	(options,arguments) = parser.parse_args()
	if not options.range
		parser.error("[-] Error!!!!! Please specify the range that has to be scanned")
	return options

options = get_arguments()
scanned_output = scan(options.range)
print_result(scanned_output)
