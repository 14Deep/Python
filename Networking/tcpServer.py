import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print '[*] Listening on %s:%d' % (bind_ip, bind_port)


#this is the client-handling thread
def handle_client(client_socket):
    
    #print what is sent by the client
    request = client_socket.recv(1024)
    
    print '[*] Recieved: %s' % request
    
    #send back a packet
    client_socket.send('TEST')
    
    client_socket.close()
    
while True:
    
    client, addr = server.accept()
    
    print '[*]Accepted connection from %s:%d' % (addr[0], addr[1])
    
    #client thread to handle data
    
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
    
    
