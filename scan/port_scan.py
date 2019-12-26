#!/usr/bin/env python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

#host = "xxx.xxx.xxx.xxx" # IP address
#port = 443
host = input("[*] Enter the host to scan: ")
#port = int(input("[*] Enter the port to scan: "))
"""  """
def portscanner(port):
    if sock.connect_ex((host, port)):
        print (colored("[!]Port %d is closed" %(port), 'red'))
    else:
        print(colored("[+]Port %d is opened" %(port), 'blue'))
""" Port for scannig """
for port in range(1, 1000):
    portscanner(port)
