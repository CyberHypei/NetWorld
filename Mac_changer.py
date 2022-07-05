#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC Address")
	parser.add_option("-m","--mac",dest="new_mac",help="New MAC Address to be assigned")
	(options,arguments)=parser.parse_args()
	if not options.interface:
		parser.error("[-] Error!!!!! Please specify the interface whose MAC address will be changed, use --help for more information")
	elif not options.new_nac:
		parser.error("[-] Error!!!!! Please specify the new MAC address to be assigned, use --help for more information")
	return options


def change_mac(interface,new_mac):
	print("[+]Changing MAC Address For "+interface+" to "+new_mac)
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig",options.interface])
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("[-] Could not read MAC address")


options = get_argumnets()
current_mac = get_current_mac(options.interface)
change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac==options.new_mac:
	print("[+] MAC Address changed successfully")
else:
	print("[+] MAC Address did not get changed")
