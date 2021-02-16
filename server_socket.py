import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # свойство SO_REUSEADDR позволяет нескольким приложениям слушать сокет
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # свойство SO_BROADCAST указывает на то, что пакеты будут широковещательные 
# habr
s.bind(('0.0.0.0', 80))
# bind the socket to a public host, and a well-known port
# s.bind((socket.gethostname(), 80))
while True:
	message = s.recv(128)
	print(message)