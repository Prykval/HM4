from http.server import HTTPServer, BaseHTTPRequestHandler


class Homeworkfork(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        pass

def run_server():
    address = ('localhost', 3000)
    http_server = HTTPServer(address, Homeworkfork)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == '__main__':
    run_server()
    