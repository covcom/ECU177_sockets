#!/usr/bin/python3 
import socket

client = socket.socket()
port = 12345
client.connect(('localhost', port))

try:
    while True:
        msg = input('>')
        client.send( msg.encode('utf-8') )

except KeyboardInterrupt:
    print('Shutdown')
    client.shutdown(1)
    client.close()
