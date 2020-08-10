def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


    
n = int(input())

num = [0] * 60

for i in range(0,60):
    num[i] = fibonacci_sum_naive(i)

print(num[n%60])

