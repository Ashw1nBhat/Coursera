import sys


def compute_min_refills(distance, tank, stops):
    n = len(stops)-2
    currRefills = 0
    lastRefills = 0
    counter = 0

    if(tank>=distance):
        return 0

    while(currRefills <= n):
        lastRefills = currRefills
        while(currRefills <= n and 
              stops[currRefills+1] - stops[lastRefills] <= tank):
            currRefills += 1
        
        if(currRefills == lastRefills):
            return -1
        if(currRefills<=n):
            counter += 1
    return counter


d = int(input())
m = int(input())
n = int(input())

stops = [0]
x = list(map(int,input().split()))
stops.extend(x)
stops.append(d)

print(compute_min_refills(d, m, stops))
