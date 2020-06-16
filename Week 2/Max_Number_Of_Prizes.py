# Uses python3
import sys

def optimal_summands(n):
    summands = []
    sum = 1
    totalSum = 0
    diffSum = 0
    original = n
    while n>0:
       n -= sum
       if(n>=0):
           summands.append(sum)
           totalSum += sum
       elif(n<0):
           totalSum+=sum
           diffSum = totalSum - original
           x = sum - diffSum
           summands[len(summands)-1] += x
       sum += 1
    
    return summands


n = int(input())
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')
