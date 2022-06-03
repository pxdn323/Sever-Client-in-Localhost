from socket import *
import time
def main():
    servername_port = ('127.0.0.1',8080)
    print('The client is ready to send')
    

    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect(servername_port)

    clientSocket.send(b'GET /index.html HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nConnection: keep-alive\r\n\n')
    response = clientSocket.recv(1024)
    print(response.decode())
    response = clientSocket.recv(1024)
    print(response.decode())
    clientSocket.send('ack'.encode())
    clientSocket.close()
        
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect(servername_port)

    clientSocket.send(b'GET /bio.txt HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nConnection: keep-alive\r\n\n')
    response = clientSocket.recv(1024)
    print(response.decode())
    response = clientSocket.recv(1024)
    print(response.decode())
    clientSocket.send('ack'.encode())
    clientSocket.close()

    time.sleep(1000)

if __name__ == '__main__':
    main()
