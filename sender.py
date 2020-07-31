import telnetlib
#ip_1 = str(input('Another computer IP_1: '))
#ip_2 = str(input('Another computer IP_2: '))
print('я карта я карта я карта\n\n')
telnet = telnetlib.Telnet('192.168.0.106', 10000)
telnet = telnetlib.Telnet('192.168.0.107', 10000)

telnet.write(b's\n')