from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f"Hello, you requested: {self.path}".encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server is running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
