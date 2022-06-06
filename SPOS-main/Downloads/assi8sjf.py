inputFile = open('input1.txt', 'r')

process1 = []
process = []
GanttChartSJF = []
burst = 0
arrival_time1 = []
burst_time1 = []
wt = []
Tt = []

priority = []
flag = []

for line in inputFile:
    process1.append(line.split())
    flag.append(0)

print(process1)
print()

for i in range(len(process1)):
    arrival_time1.append(int(process1[i][1]))
    process.append([process1[i][0], int(process1[i][1])])
    burst_time1.append(int(process1[i][2]))
    flag.append(0)
print(arrival_time1)
print()
print(burst_time1)
print()

for i in range(len(process1)):

    if process1[i][0] == 'p1' and arrival_time1[i] == 0:
        burst = burst + int(process1[i][2])
        GanttChartSJF.append([str(process1[i][0]), burst])
        flag[i] = 1

    else:
        for j in range(len(process1)):
            if arrival_time1[j] <= GanttChartSJF[i-1][1] and flag[j] == 0:
                priority.append(burst_time1[j])

        val = min(priority)

        priority.clear()

        for k in range(len(process1)):
            if process1[k][2] == str(val):
                burst = burst + val
                GanttChartSJF.append([str(process1[k][0]), burst])
                flag[k] = 1

print(GanttChartSJF)

# Waiting Time
for i in range(len(process)):

    if GanttChartSJF[i][0] == 'p1':
        wt.append(0)
        print('Waiting Time (' + str(GanttChartSJF[i][0]) + ') = 0')
    else:
        for j in range(len(process)):
            if process[i][0] == GanttChartSJF[j][0]:
                wt.append(GanttChartSJF[j-1][1] - process[i][1])
                print(
                    'Waiting Time (' + str(GanttChartSJF[i][0]) + ') = ' + str(wt[i]))
print('Average Waiting Time = ' + str(sum(wt)/len(wt)))
print()

# Turnaround Time
for i in range(len(process)):
    for j in range(len(process)):
        if process[i][0] == GanttChartSJF[j][0]:
            Tt.append(GanttChartSJF[j][1] - process[i][1])
            print(
                'Turnaround Time (' + str(GanttChartSJF[i][0]) + ') = ' + str(Tt[i]))
print('Average Turnaround Time = ' + str(sum(Tt)/len(Tt)))
