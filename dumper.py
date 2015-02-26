import subprocess
import os

DUMP_FOLDER = os.getcwd()+"/dump"
ARP_DUMP = os.getcwd()+'/dump/arpDump'
IFCONFIG_DUMP = os.getcwd()+'/dump/ifconfigDump'

def checkDumpFiles():
	open(ARP_DUMP, "a").close()
	open(IFCONFIG_DUMP, "a").close()

class Dumper(object):

	def __init__(self):
		if not os.path.exists(DUMP_FOLDER):
			os.makedirs(DUMP_FOLDER)
		checkDumpFiles()

	def arpDump(this):
		subprocess.call('rm '+ARP_DUMP, shell=True)
		subprocess.call('arp -a >> '+ARP_DUMP, shell=True)

	def ipConfigDump(this,i):
		subprocess.call('rm '+IFCONFIG_DUMP, shell=True)
		subprocess.call('ifconfig '+i+' >> '+IFCONFIG_DUMP, shell=True)