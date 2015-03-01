import dumper
import re


def getHWAddr():
	ifconfigData = dumper.readIFConfigDump()
	s = re.search( r'HWaddr ([:,\w,\d]*)', ifconfigData, re.M|re.I)
	HWaddr = ''
	if s:
		HWaddr = s.group(1)
	return HWaddr


def getIPv4():
    ifconfigData = dumper.readIFConfigDump()
    s = re.search( r'inet addr:([.,\d]*)', ifconfigData, re.M|re.I)
    ipv4 = '0'
    if s:
    	ipv4 = s.group(1)
    	return ipv4
    else:
    	print(interface+': Not connected');
    	ipConfigDump('usb0')
    	return getIPv4()
    ifconfigData = dumper.readIFConfigDump()
    s = re.search( r'inet addr:([.,\d]*)', ifconfigData, re.M|re.I)
    ipv4 = '0'
    if s:
    	ipv4 = s.group(1)
    	return ipv4
    else:
    	print(interface+': Not connected');
    	#ipConfigDump('usb0')
    return 0


def getClass():
	ip = getIPv4()
	s = re.search(r'([\d]*).*', ip, re.M|re.I)
	if s:
		x = int(s.group(1))
		if x<128:
			return 'A'
    	if x<192:
    		return 'B'
    	if x<224:
    		return 'C'
    	if x<240:
    		return 'D'
    	if x<256:
			return 'E'   
	print('none')


def getPrefixLength(c):
	if c=='a':
		return 8
	elif c=='b':
		return 16
	elif c=='c':
		return 24
	elif c=='d':
		return 28

	
	