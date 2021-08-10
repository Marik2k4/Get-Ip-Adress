import socket
hostname = socket.gethostname()
IPADR = socket.gethostbyname(hostname)
print(IPADR)