#!/usr/bin/env python3

import socket, random, sys

MAX_BYTES = 65535

def server(interface, port):
    sSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sSock.bind((interface, port))
    print('Listening at {}'.format(sSock.getsockname()))
    while True:
        msg, address = sSock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print('Dropped packet from {}'.format(address))
            continue
        sentence = msg.decode('ascii')
        print('Someone from {} said {!r}'.format(address, sentence))
        sentence = 'I received from you a message of {} bytes'.format(len(msg))
        msg = sentence.encode('ascii')
        sSock.sendto(msg, address)
    
if __name__ == '__main__':
    # pass to server the network interface and port number
    server(sys.argv[1], int(sys.argv[2]))
