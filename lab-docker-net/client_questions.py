#!/usr/bin/env python3
# Client puts yes/no questions to server

from socket import *
import helpers, sys

def client(address, make_error=False):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)
    if make_error:
        sock.sendall(b'This is without the delimiter')
        return
    go = input("continue? ")
    while go == 'y':
        for q in helpers.example_questions: 
            sock.sendall(q)
            print(helpers.recv_upto(sock, b'.').decode())  # print as plain string
        go = input("continue? ")
    sock.close()

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    error = False
    if (len(sys.argv) == 4):
        error = True if sys.argv[3] == '-e' else False
    address = (host, port)
    client(address, error)
