from socketserver import StreamRequestHandler, ThreadingTCPServer
from src.core.net.conf import *
import threading


class ThreadedTCPRequestHandler(StreamRequestHandler):
    def handle(self):
        try:
            cur_thread = threading.current_thread()
            print("\nClient [{}]:\n\tPORT: {}\n\tTH: {}\n".format(*self.client_address, cur_thread))
            request = self.rfile.readline()
            request = pickle.loads(request.rstrip())
            print("RX [%s]: %s" % (self.client_address[0], request))
            response = "{}: {}".format(cur_thread.name, request)
            print("TX [%s]: %s" % (self.client_address[0], response))
            self.wfile.write(bytes(response.encode("utf-8")))
        except Exception as e:
            print("ER [%s]: %r" % (self.client_address[0], e))
        print("DC [%s]: disconnected" % (self.client_address[0]))


def run_server():
    server = ThreadingTCPServer(ADDR, ThreadedTCPRequestHandler, bind_and_activate=True)
    ip, port = server.server_address
    # server_thread = threading.Thread(name="MainThread", target=server.serve_forever, daemon=True)
    # server_thread.start()
    # print("Server running...\nIP: {}\nPORT: {}\nMainLoop: {}".format(ip, port, server_thread))
    server.serve_forever()
    server.shutdown()
    server.server_close()
    print("Server stopped...")
