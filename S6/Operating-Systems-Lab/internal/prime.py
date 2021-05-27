# Sidhant Unnithan
# CSE B     89
# OS Lab Internal

import os

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def isPrime(x):
    if isInt(x):
        x = int(x)
    else:
        return False

    if(x < 2):
        return False
    
    i = 2
    while(x % i != 0):
        i += 1
    if(x == i):
        return True
    return False


def main():
    r, w = os.pipe()
    pid = os.fork()

    if pid:
        os.close(r)
        w = os.fdopen(w, 'w')
        n = int(input("Enter value of n : "))
        num = ""
        for i in range(0, n):
            temp = int(input("Enter number : "))
            num += str(temp) + " "
        w.write(num)
        w.close()

    else:
        os.close(w)
        r = os.fdopen(r)
        num = r.read()
        num = num.split(' ')

        for i in num:
            if isPrime(i):
                print(i)

        r.close()
        exit()


if __name__ == "__main__":
    main()