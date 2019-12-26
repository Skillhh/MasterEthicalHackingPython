#!/usr/bin/env python3

import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.socket((ip, port))
        banner = s.recv(1024)
        return banner

    except:
        return

def main():
    ip = input("[*] Enter Host: ")
#    port = 22
#    ip = "xxx.xxx.xxx.xxx" #IP Address
#    banner = retBanner(ip, port)
#    if banner:
#        print("[+]" + ip + ": " + banner)
    for port in range(1, 1000):
        banner = retBanner(ip, port)
        if banner:
            print("[+]" + ip + "/" + str(port) +": " + banner.strip('\n'))

    
if __name__ == "__main__":
    main()
