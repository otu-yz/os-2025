#!/usr/bin/env python3
# TCP server receives chunks of data from client, each chunk is prefixed with the length of the data in that chunk.

from socket import *
import sys, pickle

def server(interface, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print('Waiting for incoming connection at', sock.getsockname())
    ss, sockname = sock.accept()
    print('Connection accepted from', sockname)
    ss.shutdown(SHUT_WR)
    f = ss.makefile("rb")
    while True:
        msg = pickle.load(f)
        if not msg:
            break
        print('Received:', repr(msg))
    f.close()
    ss.close()
    sock.close()

def client(host, port):
    cs = socket(AF_INET, SOCK_STREAM)
    cs.connect((host, port))
    cs.shutdown(SHUT_RD)
    f = cs.makefile("wb")
    pickle.dump('Never let truth get in the way of a good story.', f)
    pickle.dump('Eighty percent of success is showing up.', f)
    pickle.dump('Pursue what is meaningful, not what is expedient.', f)
    pickle.dump('', f)
    f.close()
    cs.close()

if __name__ == '__main__':
    functions = {'client': client, 'server': server}
    role = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    function = functions[role]
    function(host, port)
