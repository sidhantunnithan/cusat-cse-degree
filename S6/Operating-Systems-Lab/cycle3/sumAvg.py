# Write a program to send 'n' numbers from a parent process to a child process. 
# Calculate the sum and average of 'n' numbers and display it in the child process.

import os

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def sum(num):
    total = 0
    for i in num:
        total += int(i)

    return total


def avg(num):
    total = sum(num)
    return total / len(num)


def main():
    r,w = os.pipe()
    pid = os.fork()

    if pid:
        os.close(r)
        w = os.fdopen(w, 'w')
        n = int(input("Enter the value of n: "))

        print("Enter the " + str(n) + " numbers : ")
        i = 0
        num = ''
        while i < n:
            x = input()
            if isInt(x):
                num += (x + ' ')
                i += 1
            else:
                print("Invalid input! Enter again: ")

        num = num[ :-1]
        w.write(num)
        w.close()

    else:
        os.close(w)
        r = os.fdopen(r)
        num = r.read()
        num = num.split(' ')        
        r.close()

        print("Sum : " + str(sum(num)))
        print("Average: " + str(avg(num)))


if __name__ == "__main__":
    main()