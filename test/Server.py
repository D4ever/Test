import socket
import http.server
import socketserver

# Address
HOST = ''
PORT = 8000

# Prepare HTTP response
text_content = '''HTTP/1.x 200 OK  
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
<form name='input' action='/' method='post'>
First name :<input type='text' name='firstname'><br>
<input type='submit' value='Submit'>
</form>
</html>
'''

# Read picture, put into HTTP format
f = open('test.jpg','rb')
pic_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
pic_content = pic_content.encode() + f.read()
f.close()

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        request   = self.request.recv(1024).decode()   
        print ('Connected by', self.client_address[0])
        print ('Request is:', request)

        method    = request.split(' ')[0]
        src       = request.split(' ')[1]

        if method == 'GET':
            if src == '/test.jpg':
                content = pic_content
            else: content = text_content.encode()
            self.request.sendall(content)

        if method == 'POST':
            form = request.split('\r\n')
            idx = form.index('')
            entry = form[idx:]

            value = entry[-1].split('=')[-1]
            value = text_content + '\n <p>' + value + '<p>'
            self.request.sendall(value.encode())

# Configure socket
server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)

server.serve_forever()