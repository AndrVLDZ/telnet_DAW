import socket
import threading
from typing import *
import key_press
import telnetlib

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
port = int(input('Set the server port: '))
SERVER_ADDR = ('0.0.0.0', port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(SERVER_ADDR)
sock.listen(1)
connections = []
ip = socket.gethostbyname(socket.getfqdn())
print('Host IP: ' + str(ip))

def handle_event_msg(data):
    if str(data, "utf-8") == "s":
        key_press.start_DAW()
        print("\nKeypress event")
    else:
        print("\nJust a msg")
        print(str(data, "utf-8"))


def handler(current_conn: socket.socket, addr):
    global connections
    while True:
        data: bytes = current_conn.recv(1024)
        handle_event_msg(data)
        for c in connections:
            c.send(bytes(str.encode('\n=>> ') + data))
        if not data:
            connections.remove(current_conn)
            current_conn.close()
            break


# Wait for an incoming connection.
while True:
    # new socket representing the connection
    conn: socket.socket
    # address of the client
    # (if IP-socket `new_addr` is a pair -> (hostaddr, port))

    conn, addr = sock.accept()  # Accept new connection
    cThread = threading.Thread(target=handler, args=(conn, addr))
    cThread.daemon = True
    cThread.start()

    connections.append(conn)
    print(connections)
    print()

