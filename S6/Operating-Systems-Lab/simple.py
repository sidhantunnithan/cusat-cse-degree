# import sys
# sys.stdin = open("simple.txt", 'r')

def avg():
    n = int(input("Enter value of n : "))
    avg = 0
    for i in range(n):
        avg += int(input("Enter value of number " + str(i+1) + " :"))
    print()
    print("Average : ", avg/n)

def rev():
    n = int(input("Enter number to be reversed : "))
    newn = 0
    while(n > 0):
        newn = newn*10 + (n % 10)
        n = int(n/10)
    print("Reversed Number : ", newn)

def li():
    n = int(input("Enter number of elements in list : "))
    li = [0]*n

    for i in range(n):
        li[i] = int(input("Enter value of element i=" + str(i) + " : "))

    print("Enter 1 to insert into a position in the list")
    print("Enter 2 to append element")
    print("Enter 3 to remove from list")
    print("Enter 4 to view list")
    print("Enter any other number to exit")
    print()
    choice = 0
    while(choice != -1):
        choice = int(input("Enter choice : "))
        if(choice == 1):
            index = int(input("Enter index : "))
            val = int(input("Enter value to be inserted : "))
            li.insert(index, val)
        elif(choice == 2):
            val = int(input("Enter value to be appended : "))
            li.append(val)
        elif(choice == 3):
            index = int(input("Enter index : "))
            li.pop(index)
        elif(choice == 4):
            print("List : ", li)
        else:
            choice = -1
        print()

choice = int(input("Enter 1 for average, 2 for reversing, 3 for list operations, any other number to exit: "))
if(choice == 1):
    avg()
elif(choice == 2):
    rev()
elif(choice == 3):
    li()
else:
    exit(0)