import subprocess
import re
import getpass

PACKETS_DUMP = 'packets.pcap'
interface = ''
ifconfigData = ''

def getIPv4():
    ifconfigData = open(IFCONFIG_DUMP).read()
    s = re.search( r'inet addr:([.,\d]*)', ifconfigData, re.M|re.I)
    ipv4 = '0'
    if s:
    	ipv4 = s.group(1)
    	print(ipv4)
    	return ipv4
    else:
    	print(interface+': Not connected');
    	ipConfigDump('usb0')
    	return getIPv4()

def startSniffing(ip):
	proc = subprocess.Popen(['sudo','tcpdump','host',ip,'-w',PACKETS_DUMP],stdin=subprocess.PIPE)
	print('\n Press ENTER to stop sniffing packets')
	x = input()
	proc.kill()

def main():
	ipConfigDump('wlan0')
	ip = getIPv4()
	if(ip != '0'):
		startSniffing(ip)
	print('...ending')