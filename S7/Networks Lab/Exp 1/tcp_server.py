import socket
s = socket.socket()

print("Sidhant's Server Starting")

port = 3000
s.bind((socket.gethostname(),port))
s.listen(5)

while True:
    k,a = s.accept()
    print(f"Connection from {a} has been established!")
    k.send(bytes("Connected to Server successfully!","utf-8"))
    k.close()


   