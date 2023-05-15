import logging
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handle(BaseHTTPRequestHandler):
    # noinspection PyPep8Naming
    def do_GET(self):
        logging.info("handle get: ")
        if self.path == '/health':
            logging.info("NETRO AL HEALTH")
            self.send_response(200)
            self.end_headers()
        else:
            logging.info("NETRO AL EEEEEEEELSE HEALTH")
            self.send_error(404)


class SimpleServer:
    def __init__(self, host, port):
        self.srv = HTTPServer((host, port), Handle)

    def run(self):
        self.srv.serve_forever()

    def close(self):
        self.srv.server_close()
