import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler

#Shopping list
shoppingList = ['Wheat','Flour','Cooking oil']

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/shoppinglist'):
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Shopping List</h1>'
            output += '<h3><a href="/shoppinglist/new">Add New Item</a></h3>'
            for shopping in shoppingList:
                output +=shopping
                # output += '<a href="/tasklist/%s/remove"> X </a>' % shopping
                output += '</br>'
            output += '</body></html>'
            self.wfile.write(output.encode())


def main():
    PORT = 9000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, Server)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()