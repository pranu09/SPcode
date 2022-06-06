inputFile = open('input.txt', 'r')

process = []
GanttChartFCFS = []
burst = 0
arrival_time = []
wt = []
Tt = []

# FCFS
for line in inputFile:
    process = line.split()

    burst = burst + int(process[2])

    arrival_time.append(int(process[1]))

    GanttChartFCFS.append([str(process[0]), burst])


print(GanttChartFCFS)
print(arrival_time)
print()

# Waiting Time
for i in range(len(GanttChartFCFS)):
    if GanttChartFCFS[i][0] == 'p1':
        wt.append(0)
        print('Waiting Time (' + str(GanttChartFCFS[i][0]) + ') = 0')
    else:
        wt.append(GanttChartFCFS[i-1][1] - arrival_time[i])
        print(
            'Waiting Time (' + str(GanttChartFCFS[i][0]) + ') = ' + str(wt[i]))
print('Average Waiting Time = ' + str(sum(wt)/len(wt)))
print()

# Turnaround Time
for i in range(len(GanttChartFCFS)):
    Tt.append(GanttChartFCFS[i][1] - arrival_time[i])
    print(
        'Turnaround Time (' + str(GanttChartFCFS[i][0]) + ') = ' + str(Tt[i]))

print('Average Turnaround Time = ' + str(sum(Tt)/len(Tt)))


# SJF
