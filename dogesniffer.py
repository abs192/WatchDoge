import subprocess
import getpass
import dumper

PACKETS_DUMP = 'packets.pcap'
interface = ''
ifconfigData = ''

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