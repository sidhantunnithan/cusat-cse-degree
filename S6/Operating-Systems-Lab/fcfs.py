# import sys
# sys.stdin = open("fcfs.txt", 'r')

process = []
n = int(input("Enter no of process: "))
for i in range(n):
	process.append([])
	process[i].append(int(input("Enter pid: ")))
	process[i].append(int(input("Enter arrival time: ")))
	process[i].append(int(input("Enter burst time: ")))
	print(' ')

process.sort(key=lambda process: process[1])

ctime = process[0][1]
print('pid\tat\tbt\tct\ttat\twt')
atat = 0
awt = 0
for i in range(n):
    ctime = ctime +  process[i][2]
    tat = ctime-process[i][1]
    wt = tat-process[i][2]
    atat = atat + tat
    awt = awt + wt
    print(process[i][0],'\t',process[i][1],'\t',process[i][2],'\t',ctime,'\t',tat,'\t',wt)

print("")
print("Average Waiting Time : ", (awt/n))
print("Average Turn-around Time : ", (atat/n))
