import socket
import json

PORT = 3000
SOCKET_ADDRESS = (socket.gethostbyname(socket.gethostname()), PORT)
server = socket.socket()
server.bind(SOCKET_ADDRESS)

def setCipherBox(keyword):
    alphabet = [1 for i in range(26)]
    i, j = 0, 0
    cipherbox = [[0 for i in range(5)] for j in range(5)]
    for k in keyword:
        if j == 5:
            i += 1
            j = 0
        if k == 'j':
            k = 'i'
        idx = ord(k) - ord('a')
        if alphabet[idx] == 1:
            cipherbox[i][j] = k
            alphabet[idx] = 0
            j += 1
    for k in range(ord('a'), ord('z')+1):
        if(chr(k) == 'j'):
            continue
        idx = k - ord('a')
        if(alphabet[idx] == 1):
            if j == 5:
                i += 1
                j = 0
            cipherbox[i][j] = chr(k)
            j += 1
    return cipherbox

def setCipherDict(cipherbox):
    cipherDict = {}
    for i in range(len(cipherbox)):
        for j in range(len(cipherbox[i])):
            ch = cipherbox[i][j]
            cipherDict[ch] = [i, j]
    return cipherDict

def setPlaintext(plaintext):
    i, j = 0, 1
    plaintext = plaintext.lower().replace('j', 'i')
    while j < len(plaintext):
        if plaintext[i] == plaintext[j]:
            if plaintext[i] != 'z':
                plaintext = plaintext[:j] + 'z' + plaintext[j:]
            else:
                plaintext = plaintext[:j] + 'y' + plaintext[j:]
        i += 2
        j += 2
    if i < len(plaintext):
        if plaintext[-1] != 'z':
            plaintext += 'z'
        else:
            plaintext += 'y'
    return plaintext

def encrypt(plaintext, keyword):
    if(not plaintext or not keyword):
        return ("plaintext or keyword invalid")
    plaintext = setPlaintext(plaintext)
    keyword = keyword.lower()
    ciphertext = ""
    cipherbox = setCipherBox(keyword)
    cipherDict = setCipherDict(cipherbox)
    i, j = 0, 1
    while i < len(plaintext):
        ch1 = {
            "x": cipherDict[plaintext[i]][0],
            "y": cipherDict[plaintext[i]][1]
        }
        ch2 = {
            "x": cipherDict[plaintext[j]][0],
            "y": cipherDict[plaintext[j]][1]
        }
        if ch1["x"] == ch2["x"]:
            ciphertext += cipherbox[ch1["x"]][(ch1["y"] + 1) % 5]
            ciphertext += cipherbox[ch2["x"]][(ch2["y"] + 1) % 5]
        elif ch1["y"] == ch2["y"]:
            ciphertext += cipherbox[(ch1["x"] + 1) % 5][ch1["y"]]
            ciphertext += cipherbox[(ch2["x"] + 1) % 5][ch2["y"]]
        else:
            ciphertext += cipherbox[ch1["x"]][ch2["y"]]
            ciphertext += cipherbox[ch2["x"]][ch1["y"]]
        i += 2
        j += 2
    return ciphertext

server.listen()
print(f"Server is listening on port {PORT}")
conn, addr = server.accept()

msg = conn.recv(1024).decode('utf-8')
msg = json.loads(msg)
try:
    plaintext = msg["plaintext"]
    keyword = msg["keyword"]
    ciphertext = encrypt(plaintext, keyword)
    msg = {
        "ciphertext": ciphertext
    }
    msg = json.dumps(msg)
except:
    msg = "an error occurred\n"
finally:
    conn.send(msg.encode('utf-8'))

print("Bye")
conn.close()
