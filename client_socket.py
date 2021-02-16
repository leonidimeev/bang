import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #
t0 = time.time()
i = 0
while True:
    if (time.time() - t0 > 1):
    # sock.sendto('broadcast!', ('255.255.255.255', 80))
        sock.sendto(('[' + str(i) + '] broadcast!').encode(), ('255.255.255.255', 80))
        print('sended [' + str(i) + ']')
        i += 1
        t0 = time.time()