# Write a program in which parent sends a list of numbers to child process and 
# the child process sends back all prime numbers from the list to the parent process.

import os

PRIME = [True for i in range(1000)]


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def setPrimes():
    p = 2
    while p * p <= 1000:
        if PRIME[p]:
            for i in range(p*p, 1000, p):
                PRIME[i] = False

        p += 1


def isPrime(x):
    if PRIME[x]:
        return True
    else:
        return False


def main():
    r1, w1 = os.pipe()
    r2, w2 = os.pipe()
    pid = os.fork()

    if pid:
        os.close(r1)
        os.close(w2)
        w1 = os.fdopen(w1, 'w')
        n = int(input("Enter the value of n : "))

        print("Enter the " + str(n) + " numbers :")
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
        w1.write(num)
        w1.close()

        r2 = os.fdopen(r2)
        result = r2.read()
        if len(result) > 0:
            print("The prime numbers are: " + result)
        else:
            print("There were no prime numbers.")

    else:
        os.close(w1)
        os.close(r2)
        r1 = os.fdopen(r1)
        num = r1.read()
        num = num.split(' ')
        r1.close()

        w2 = os.fdopen(w2, 'w')
        primes = ""
        for i in num:
            if isPrime(int(i)):
                primes += (i + ' ')

        primes = primes[ : -1]
        w2.write(primes)
        w2.close()


if __name__ == "__main__":
    setPrimes()
    main()