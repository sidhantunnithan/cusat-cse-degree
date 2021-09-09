import socket

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    checkword = tmp
    return checkword

def decodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    return remainder

print('Sidhant server starting')
s = socket.socket()
port = 9999
s.bind(('', port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Conection request from : ', addr)
    data = c.recv(1024).decode()
    print(data)
    if not data:
        break
    key = "1001"
    ans = decodeData(data, key)
    print("Remainder after decoding is : " + ans)
    temp = "0" * (len(key) - 1)
    if ans == temp:
        c.send(bytes("Received data with no error : " + data,'utf-8'))
    else:
        c.send(bytes("Error occured for data : " + data ,'utf-8'))
    c.close()