
from http.server import HTTPServer, BaseHTTPRequestHandler

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        result = """
        <html>
        <body>
        <h1>Calculator Application</h1>
        <h3>Addition: 30</h3>
        <h3>Subtraction: 10</h3>
        <h3>Multiplication: 20</h3>
        <p>Application deployed using Kubernetes!</p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), MyHandler)
    print("Calculator running on port 8000")
    server.serve_forever()

