#!/usr/bin/python3          
import socket, select         # Import networking modules

def clean_message(msgbytes):
    ''' clean up any messages recieved with the recv() function, decoding and removing newlines '''

    return msgbytes.decode('utf-8').strip('\r\n')

def prepare_message(msg):
    ''' prepare any message so that it can be sent with the send() function, encoding and adding newlines '''

    msgbytes += '\r\n'
    return msgbytes.encode('utf-8')

class Chat:
    def __init__(self, port=12345):
        self.connections = []
        self.port = port

        self.server = socket.socket()         # Create a server socket
        self.server.bind(('', port))          # Bind to the port
        self.server.listen(5)                 # Now wait for client connections

    def shutdown(self):
        ''' shutdown the chat server '''

        for c in self.connections:
            c.close()

        self.server.shutdown(1)
        self.server.close()

    def poll(self):
        ''' see if there is anything for the server to do and do it. call poll() reguarly '''

        read, write, error = select.select( self.connections+[self.server], self.connections, self.connections, 0 )

        for conn in read:
            if conn is self.server:                 # new client connecting
                c, addr = conn.accept()
                self.connections.append(c)            # add to list of open self.connections

                print('Got connection from {}'.format(addr) )

            else:
                msgbytes = conn.recv(1024)

                if not msgbytes:                     # treat empty message as a disconnection
                    print('Disconnected')

                else:                                 # not empty so treat as normal message
                    print('Message: {}'.format( clean_message(msgbytes) ) )

if __name__ == '__main__':
    c = Chat()

    try:
        print( "Server is running on port {}".format( c.port ) )

        while True:
            c.poll()

    except KeyboardInterrupt:
        pass

    finally:                                        # make certain everthing gets closed down properly
        print( "Shutdown" )
        c.shutdown()
                            