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

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

print('Sidhant client starting')
s = socket.socket()
port = 9999
s.connect(('127.0.0.1', port))
input_string = input("Enter string : ")
data = (''.join(format(ord(x), 'b') for x in input_string))
key = "1001"
ans = encodeData(data, key)
print(ans)
# s.send(bytes(ans,'utf-8'))

# sending wrong data
s.send(bytes('110000111000101100011010','utf-8'))
print(s.recv(1024).decode('utf-8'))
s.close()