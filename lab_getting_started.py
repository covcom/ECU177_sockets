#!/usr/bin/python3          
import socket, time         # Import socket module

s = socket.socket()         # Create a socket object
port = 12345                # Reserve a port for your service.
s.bind(('', port))          # Bind to the port
s.listen(5)                 # Now wait for client connection

print( "Server is running on port {}".format( port ) )

try:
    while True:
        c, addr = s.accept()     # Establish connection with client.

        print('Got connection from', addr)

        msg = 'Thank you for connecting'
        c.send( msg.encode('ascii') ) # send message

        time.sleep(5)            # wait 5s

        print('Disconnected')
        c.close()                # Close the connection

except KeyboardInterrupt:        # catch Ctrl-C signals so that we shutdown nicely
    pass

finally:                        # make certain that the sockets get closed properly
    print('Shutdown')
    s.shutdown(1)
    s.close()