def fib_last(n):
    

    current = 0
    next  = 1

    for i in range(0,n):
        

        current, next = next, current + next

    return current%10

sum=0

input = input()
from_, to = map(int, input.split())

num = [0] * 60

for i in range(0,60):
    num[i] = fib_last(i)



print((num[(to+2)%60] - num[(from_+1)%60])%10) 