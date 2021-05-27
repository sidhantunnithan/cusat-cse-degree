# import sys
# sys.stdin = open("sjf.txt", 'r')

process=[]
n=int(input("Enter no of process: "))
ct=[0]*n
tat=[]
wt=[]
for i in range(n):
	process.append([])
	process[i].append(int(input("Enter process id: ")))
	process[i].append(int(input("Enter arrival time: ")))
	process[i].append(int(input("Enter burst time: ")))
	print()

process.sort(key = lambda process:process[0])

for i in range(n):
	process[i].append(process[i][2])
	process[i].append(i)

tim = 0
completed = 0

while(completed != n):

    p = list(filter(lambda pr:pr[1] <= tim and len(pr) == 5, process))
    if(p!=[]):
        p.sort(key = lambda p:p[2])
        index = p[0][4]
        process[index].append(1)
        tim += process[index][2]
        completed += 1
        ct[index] = tim
    else:
        tim += 1

atat = 0
awt = 0

for i in range(n):
    tat.append(ct[i]-process[i][1])
    wt.append(tat[i]-process[i][2])
    atat += tat[i]
    awt += wt[i]


print("PID\tAT\tBT\tCT\tTAT\tWt")
for i in range(n):
	print(process[i][0],'\t',process[i][1],'\t',process[i][2],'\t',ct[i],'\t',tat[i],'\t',wt[i])
print("")
print("Average Waiting Time : ", awt/n)
print("Average Turn Around Time : ", atat/n)