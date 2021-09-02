import socket
import threading

s = socket.socket()
print("Sidhant's Client Starting")
port  = 3000
s.connect((socket.gethostname(),port))
s.settimeout(1)

name = input("Enter name : ")
running = True

def handle_message_receive(s):
    while running:
        try:
            res = s.recv(1024).decode('utf-8')
            print(res)
        except Exception as e:
            continue

client_thread = threading.Thread(target=handle_message_receive, args=(s,))
client_thread.start()
s.send(bytes(f"{name}","utf-8"))

while True:
    msg = input()
    s.send(bytes(f"{msg}","utf-8"))
    if(msg == "exit"):
        running = False
        client_thread.join()
        s.close()
        quit()
