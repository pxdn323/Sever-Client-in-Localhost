from socket import *

def REQUEST(conn):
    request = conn.recv(1024).decode()
    print(request)

    if 'bio.txt' in request:
        f = open('bio.txt',mode = 'rb')
        data = f.read()
        f.close()
        conn.send(data)

    else:
        
        f = open('index.html',mode = 'rb')
        data = f.read()
        f.close()
        conn.send(data)


def main():    
    servername_port = ('127.0.0.1',8080)
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(servername_port)
    print('The server is ready to receive')
    while True:
        serverSocket.listen(1)
        conn,addr = serverSocket.accept()
        conn.send(bytes("HTTP/1.1 \r\n\r\n", encoding = 'utf-8'))
        REQUEST(conn)
        conn.close()
    
    
if __name__ == '__main__':
    main()
