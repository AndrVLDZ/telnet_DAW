import telnetlib
#ip_1 = str(input('Another computer IP_1: '))
#ip_2 = str(input('Another computer IP_2: '))

def print_logo(logo=''):
    LOGO_DAFAULT = """\033[93m

   /\                 /\\
  / \\'._   (\_/)   _.'/ \\
 /_.''._'--('.')--'_.''._\\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
   `      \(/|\)/        `
           " ` "
       Viktor&Cepesh 
\033[0m
"""
    if logo != '':
        print(logo)
    else:
        print(LOGO_DAFAULT)

print_logo()

port = int(input('\nTELL ME THE FUCKING PORT:'))

while True:
    symbol = input('==> ')
    if symbol == 's':
        home_pc = telnetlib.Telnet('192.168.0.106', port)
        notebook = telnetlib.Telnet('192.168.0.107', port)
        home_pc.write(b's')
        notebook.write(b's')