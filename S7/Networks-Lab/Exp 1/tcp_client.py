import socket
s = socket.socket()

print("Sidhant's Client Starting")
port  = 3000
s.connect((socket.gethostname(),port))
msg = s.recv(1024)
print(msg.decode("utf-8"))
s.close()
