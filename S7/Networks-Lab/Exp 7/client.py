import socket
import json

PORT = 3000
SOCKER_ADDRESS = (socket.gethostbyname(socket.gethostname()), PORT)
DISCONNECT_MSG = ":q"

client = socket.socket()
client.connect(SOCKER_ADDRESS)

def communicate(msg):
    msg = msg.encode('utf-8')
    client.send(msg)
    msg = client.recv(1024).decode('utf-8')
    msg = json.loads(msg)
    print(f'cipher text : {msg["ciphertext"]}')
    print()

plaintext = input("Enter the plaintext: ")
keyword = input("Enter the keyword: ")
msg = {
    "plaintext": plaintext,
    "keyword": keyword
}
communicate(json.dumps(msg))

client.close()    