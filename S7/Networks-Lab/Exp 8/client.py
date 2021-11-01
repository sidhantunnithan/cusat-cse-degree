import socket
import json
PORT = 3000
FORMAT = 'utf-8'
ADDR = (socket.gethostbyname(socket.gethostname()), PORT)
client = socket.socket()
client.connect(ADDR)

def send(msg):
    msg = msg.encode(FORMAT)
    client.send(msg)
    msg = client.recv(1024).decode(FORMAT)
    msg = json.loads(msg)
    if(msg["ciphertext"] != "Goodbye"):
        print("Ciphertext: " + msg["ciphertext"])
    else:
        print(msg["ciphertext"])
    print()

plaintext = input("Enter the plaintext: ")
keyword = input("Enter the keyword: ")
msg = {
    "plaintext": plaintext,
    "keyword": keyword
}
send(json.dumps(msg))
client.close()