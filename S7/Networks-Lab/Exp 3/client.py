import socket
s = socket.socket()

print("Sidhant's Client Starting")
port  = 3000
s.connect((socket.gethostname(),port))

while True:
    number = int(input("enter a number to be checked (enter negative to exit): "))
    if(number < 0):
        s.close()
        quit()
    print("sending number to server")
    s.send(bytes(f"{number}","utf-8"))
    res = s.recv(1024).decode('utf-8')
    print(f"response received : {res}")
