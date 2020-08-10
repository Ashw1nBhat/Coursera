import sys

def OptimalSequence(n):
   minOps = MinOperations(n)
   return GetSeq(minOps,n)

def GetSeq(seq,n):
    result = []

    while n>0:
        result.append(n)
        if n%2!=0 and n%3!=0:
            n = n-1
        elif n%2 == 0 and n%3 == 0:
            n = n//3
        elif n%2 == 0:
            if seq[n-1] < seq[n//2]:
                n = n-1
            else:
                n = n//2
        elif n%3 == 0:
            if seq[n-1] < seq[n//3]:
                n = n-1
            else:
                n = n//3
    return reversed(result)


def MinOperations(n):
    result = [0 for i in range(n+1)]

    for i in range(2,n+1):
        r1 = result[i-1]
        r2 = sys.maxsize
        r3 = sys.maxsize
        if i%2 == 0:
            r2 = result[int(i/2)]
        if i%3 == 0:
            r3 = result[int(i/3)]
        subRes = min(r1,r2,r3)

        result[i] = subRes + 1

    return result

n = int(input())
sequence = list(OptimalSequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
