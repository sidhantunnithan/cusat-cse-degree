import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Sidhant's Server Starting")

port = 3000
s.bind((socket.gethostname(),port))

while True:
    data,address = s.recvfrom(1024)
    data = data.decode("utf-8")
    print(f"Client : {data}")

    data = "Hello from the Server side"
    data = data.encode("utf-8")
    s.sendto(data,address)