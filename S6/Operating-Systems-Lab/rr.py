# import sys
# sys.stdin = open("rr.txt", 'r')

process=[]
n=int(input("Enter no of process: "))
q=int(input("Enter time quantum: "))

for i in range(n):
	process.append([])
	process[i].append(int(input("Enter pid: ")))
	process[i].append(int(input("Enter arrival time: ")))
	process[i].append(int(input("Enter burst time: ")))
	process[i].append(process[i][2])
	print()
print()

process.sort(key = lambda process:process[1])

for i in range(n):
    process[i].append(i)

t=0
ct = [0]*n
completed = 0
tim = 0

while(completed < n):
    for p in process:
        if p[1] > tim or p[3] == 0:
            continue
        else:
            index = p[4]
            if p[3] > q:
                process[index][3] -= q
                tim += q
            else:
                tim += p[3]
                process[index][3] -= p[3]
                completed += 1
                ct[index] = tim    

wt = []
tat = []
awt = 0
atat = 0
for i in range(n):
    tat.append(ct[i]-process[i][1])
    wt.append(tat[i]-process[i][2])
    atat += tat[i]
    awt += wt[i]

print('PID\tAT\tBT\tCT\tTAT\tWT')
for i in range(n):
	print(process[i][0],'\t',process[i][1],'\t',process[i][2],'\t', ct[i], '\t', tat[i], '\t', wt[i])
print("Average Waiting Time : ", awt/n)
print("Average Turn Around Time : ", atat/n)