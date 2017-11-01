#!/usr/bin/env python

import socket
import sys


def parse(s):
    ip, port = s.split(':')
    return ip, int(port)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: udp-mux.py src-ip:port [dst-ip:port]...'
        sys.exit(2)

    addr = [ parse(s) for s in sys.argv[1:] ]
    recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    recv.bind( addr[0] )

    print 'Forwarding UDP packets received on %s:%d to:' % addr[0]
    print '\n'.join(['    - %s:%d' % a for a in addr[1:]])

    while True:
        data = recv.recvfrom(4096)[0]
        for a in addr[1:]:
            send.sendto(data, a)
