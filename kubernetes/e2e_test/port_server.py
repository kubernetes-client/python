#!/usr/bin/env python

import select
import socketserver
import sys
import threading
import time


class PortServer:
    def __init__(self, port):
        self.port = port
        self.server = socketserver.ThreadingTCPServer(('0.0.0.0', port), self.handler)
        self.server.daemon_threads = True
        self.thread = threading.Thread(target=self.server.serve_forever,
                                       name='Port %s Server' % port)
        self.thread.daemon = True
        self.thread.start()


    def handler(self, request, address, server):
        threading.current_thread().name = 'Port %s Handler' % self.port
        rlist = [request]
        echo = b''
        while True:
            r, w, _x = select.select(rlist, [request] if echo else [], [])
            if r:
                data = request.recv(1024)
                if not data:
                    break
                echo += data
            if w:
                echo = echo[request.send(echo):]


if __name__ == '__main__':
    ports = []
    for port in sys.argv[1:]:
        ports.append(PortServer(int(port)))
    time.sleep(10 * 60)

