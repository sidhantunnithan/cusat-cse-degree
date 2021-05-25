# Sidhant Unnithan
# CSE B 
# 89
# Write a program to send 'n' numbers from a parent process to a child process and display the even numbers and odd numbers separately.

import os

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

r, w = os.pipe()
pid = os.fork()

if pid:
    os.close(r)
    w = os.fdopen(w, 'w')
    n = int(input("Enter the value of n: "))

    num = []
    print("Enter the " + str(n) + " numbers: ")
    
    i = 0
    while i < n:
        x = input()
        if isInt(x):
            num += [x]
            i += 1
        else:
            print("Invalid input! Enter again: ")
    num = ' '.join(num)

    w.write(num)
    w.close()

else:
    os.close(w)
    r = os.fdopen(r)
    num = r.read()
    num = num.split(' ')
    even = []
    odd = []

    for i in num:
        if int(i)%2 :
            odd += [i]
        else:
            even += [i]
    
    print("Even numbers: ")
    print(even)
    print("Odd numbers: ")
    print(odd)

    r.close()


    