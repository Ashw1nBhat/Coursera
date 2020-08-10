import sys

def GetChange(m,l,coins):
    
    result = [0 for i in range(m+1)]

    for i in range(1,m+1):
        result[i] = sys.maxsize

    subRes = 0

    for i in range(1,m+1):
        for j in range(l):
            if (coins[j]<=i):
                subRes = result[i-coins[j]]
            if (subRes != sys.maxsize and subRes+1 < result[i]):
                result[i] = subRes + 1

    return result[m]

    

m = int(input())
coins = [1,3,4]
l = len(coins)
print(GetChange(m,l,coins))
