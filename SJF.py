from numpy import*
from array import *

chart=[]

class Process:
    def __init__(self,pid,AT,BT):
        self.pid = pid
        self.arrival = AT
        self.burst = BT



def SJF(check,num,nump):
    global chart
    queue=[]
    time = 0
    ap=0
    rp=0
    done=0

    if nump:
        while (done < num):
            for i in range(ap, num):
                if time >= check[i].arrival:
                    queue.append(check[i])
                    ap += 1
                    rp += 1

            if rp < 1:
                time += 1
                chart.append(0)
                continue

            queue.sort(key=lambda x: (x.burst))
            for i in range(0,1):
                print(queue[i].burst,queue[i].arrival)
                print("ruk")

            if queue[0].burst > 0:
                    chart.append(queue[0].pid)
                    time += 1
                    queue[0].burst -=1
                    if(queue[0].burst<1):
                        queue[0].burst = 99
                        done += 1
                        rp -= 1




ct=[]
plist=[]







print('Enter Number of Process')
process_no = int(input())
ar = []

for i in range(0,process_no):
    ar.append([])

for i in range(0,process_no):
    for j in range(0,3):

        ar[i].append(j)
        ar[i][j] =0

for i in range(0,process_no):
    print('Enter Arrival Time : ')
    ar[i][1]= int(input())
    ar[i][0]= i +1


for i in range(0,process_no):
    print('Enter Brust Time : ')
    ar[i][2] = int(input())



for i in range(0,process_no):
    plist.append(Process(ar[i][0],ar[i][1],ar[i][2]))





SJF(plist,len(plist),1)
print(chart)















for i in range(0,process_no):
    ct.append([])



for i in range(0,5):
    for j in range(0,len(chart)):
        if(i+1==chart[j]):
            ct[i]=j+1

print('CT')
print(ct)
P="Process"
AT="Arrival Time"
BT="Brust Time"
CT="Calculated Time"
TAT="Turned Arround Time"
WT="Waiting Time"
h=0

print("%-15s %-15s %-15s %-15s %-15s %-15s " %(P,AT,BT,CT,TAT,WT))
for i in range(0,process_no):
    print("P%-17s %-17s %-17s %-17s %-17s %-17s" %(ar[i][0],ar[i][1],ar[i][2],ct[i],(ct[i]-ar[i][1]),((ct[i]-ar[i][1])-ar[i][2])))
print("Gantt Chart")
print(chart)






