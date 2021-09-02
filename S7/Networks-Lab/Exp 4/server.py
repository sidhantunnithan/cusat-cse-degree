import socket
import threading

s = socket.socket()
print("Sidhant's Server Starting")
port = 3000
s.bind((socket.gethostname(),port))
s.listen(5)

client_list = []

def handle_client(conn, addr):
    conn.send(bytes("Welcome the the chat room! Type exit to leave the chat room", "utf-8"))
    name = conn.recv(1024).decode('utf-8')
    broadcast(f"{name} has joined the chat room", conn)
    client_list.append(conn)
    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if(msg == "exit"):
                remove_connection(conn, name)
                return
            else:
                msg = f"{name} : {msg}"
                broadcast(msg, conn)
        except Exception as e:
            print(e)
            remove_connection(conn, name)
            return

def broadcast(message, conn):
    print(message)
    for client in client_list:
        if(client != conn):
            client.send(bytes(message, "utf-8"))

def remove_connection(conn, name):
    client_list.remove(conn)
    print(f"{name} left the chatroom")

while True:
    k,a = s.accept()
    threading.Thread(target=handle_client, args=(k, a)).start()
