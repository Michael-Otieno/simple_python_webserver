import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler

#Shopping list
shoppinglist = ['Wheat','Flour','Cooking oil']

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
            for shopping in shoppinglist:
                output +=shopping
                output += '<a href="/shoppinglist/%s/remove"> Del </a>' % shopping
                output += '</br>'
            output += '</body></html>'
            self.wfile.write(output.encode())

        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Add New Item</h1>'
            
            output += '<form method="POST" enctype="multipart/form-data" action="/shoppinglist/new">'
            output += '<input name="item" type="test" placeholder="Add new item">'
            output += '<input type="submit" value="Add Item">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(output.encode())

        
        if self.path.endswith('/remove'):
            listIDpath = self.path.split('/')[2]
            print(listIDpath)
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Remove item: %s</h1>' % listIDpath.replace('%20', ' ')
            output += '<form method="POST" enctype="multipart/form-data" action="/shoppinglist/%s/remove">' % listIDpath
            output += '<input type="Submit" value="Remove"></form>'
            output +=  '<a href="/shoppinglist">Cancel</a>'

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