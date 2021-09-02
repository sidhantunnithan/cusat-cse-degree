import socket
s = socket.socket()

print("Sidhant's Server Starting")

port = 3000
s.bind((socket.gethostname(),port))
s.listen(5)
k,a = s.accept()
print(f"Connection from {a} has been established!")

while True:
    try:
        number = int(k.recv(1024).decode("utf-8"))
        print(f"Received a number from client : {number}")
        res = ""
        if(number & 1):
            res = "odd"
        else:
            res = "even"
        print("Sending response to client")
        k.send(bytes(res, "utf-8"))
    except Exception as e:
        print("client left")
        k.close()
        quit()