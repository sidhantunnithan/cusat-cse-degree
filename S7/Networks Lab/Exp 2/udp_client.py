import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


print("Sidhant's Client Starting")

port = 3000
addr = (socket.gethostname(),port)

data = "Hello from the Client Side"
data = data.encode("utf-8")
s.sendto(data,addr)

data,addr = s.recvfrom(1024)
data = data.decode("utf-8")
print(f"Server : {data}")

s.close()