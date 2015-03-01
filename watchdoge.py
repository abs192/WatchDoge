import utilities
import dumper
from dumper import Dumper
from threading import Thread

threads = []

def main():
	dump = Dumper();
	dump.arpDump();
	print('\n Reading ARPDump: '+dumper.readARPDump())
	dump.arpDump();
	dump.ipConfigDump('wlan0');
	print('\n Reading IFConfigDump: '+dumper.readIFConfigDump())

	startScanning();
	dump.arpDump();	


def startScanning():
	ip = utilities.getIPv4()
	c = utilities.getClass()
	hw = utilities.getHWAddr()
	print('[~] '+ip+' | Class '+c+' | '+hw+'\n')
	return

if __name__ == '__main__':

	print('~\nInitilaizing..')
	
	main()
	while True:
		inp = raw_input(".:")
		if inp == "exit":
			break
		else:
			print("Invalid command")
	print('..Shutdown\n~')