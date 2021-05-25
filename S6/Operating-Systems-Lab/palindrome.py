import os

def reverseString(s):
    return s[ : : -1]

def isPalindrome(s):
    if s == reverseString(s):
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
        s = input("Enter a string : ")
        w1.write(s)
        w1.close()

        r2 = os.fdopen(r2)
        result = r2.read()
        print(result)

    else:
        os.close(w1)
        os.close(r2)
        r1 = os.fdopen(r1)
        s = r1.read()
        r1.close()

        w2 = os.fdopen(w2, 'w')
        if isPalindrome(s):
            w2.write("The given string is a palindrome")
        else:
            w2.write("The given string is not a palindrome")

        w2.close()


if __name__ == "__main__":
    main()