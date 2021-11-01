import socket
import json
PORT = 3000
FORMAT = 'utf-8'
ADDR = (socket.gethostbyname(socket.gethostname()), PORT)
server = socket.socket()
server.bind(ADDR)

def updatePlaintext(plaintext, lenKeyword):
    rem = len(plaintext) % lenKeyword
    plaintext += (' ' * (lenKeyword - rem))
    return plaintext

def getArray(plaintext, lenKeyword):
    arr = [[]]
    i, j = 0, 0
    for k in plaintext:
        if j == lenKeyword:
            arr.append([])
            i += 1
            j = 0
        arr[i] += k
        j += 1
    return arr

def getStringsDict(arr, keyword):
    stringDict = {}
    for i in range(len(keyword)):
        if keyword[i] not in stringDict.keys():
            stringDict[keyword[i]] = []
        s = ""
        for j in range(len(arr)):
            s += arr[j][i]
        stringDict[keyword[i]].append(s)
    return stringDict

def getStringDictKeys(stringDict):
    stringDictKeys = []
    for i in stringDict.keys():
        stringDictKeys.append(i)
    stringDictKeys.sort()
    return stringDictKeys 

def encrypt( plaintext, keyword):
    keyword == keyword.lower()
    plaintext = updatePlaintext(plaintext, len(keyword))
    arr = getArray(plaintext, len(keyword))
    ciphertext = ""
    stringDict = getStringsDict(arr, keyword)
    stringDictKeys = getStringDictKeys(stringDict)
    for i in stringDictKeys:
        for j in stringDict[i]:
            ciphertext += j
    return ciphertext

server.listen()
print(f"Server is listening on {socket.gethostbyname(socket.gethostname())}")
conn, addr = server.accept()

print(f"Connection from {addr} has been established!")
msg = conn.recv(1024).decode(FORMAT)
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
    msg = "Send a valid message \n"
finally:
    conn.send(msg.encode(FORMAT))
print("Connection closed!")
conn.close()