import logging
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handle(BaseHTTPRequestHandler):
    # noinspection PyPep8Naming
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
        else:
            self.send_error(404)


class SimpleServer:
    def __init__(self, host, port):
        self.srv = HTTPServer((host, port), Handle)

    def run(self):
        self.srv.serve_forever()

    def close(self):
        self.srv.server_close()
