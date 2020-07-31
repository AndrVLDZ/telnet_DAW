import telnetlib
#ip_1 = str(input('Another computer IP_1: '))
#ip_2 = str(input('Another computer IP_2: '))
print('я карта я карта я карта\n\n')
port = int(input('\nTELL ME THE FUCKING PORT:'))

while True:
    symbol = input('==> ')
    if symbol == 's':
        telnet = telnetlib.Telnet('192.168.0.106', port)
        telnet = telnetlib.Telnet('192.168.0.107', port)
        telnet.write(b's\n')