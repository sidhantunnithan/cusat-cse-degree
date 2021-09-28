import os

def main():
    r,w = os.pipe()
    pid = os.fork()
    if pid:
        os.close(r)
        w = os.fdopen(w, 'w')
        n = int(input("Enter the value of n: "))

        if(n < 2):
            print("Minimum value of n is 2")
            return

        print("Enter the " + str(n) + " numbers : ")
        i = 0
        num = ''
        while i < n:
            x = input()
            num += x + ' '
            i += 1
        num = num[ :-1]
        w.write(num)
        w.close()
    else:
        os.close(w)
        r = os.fdopen(r)
        num = r.read()
        num = [int(n) for n in num.split(' ')]
        r.close()
        num.sort()
        print(f"Largest : {num[-1]}\nSecond Largest : {num[-2]}")

if __name__ == "__main__":
    main()