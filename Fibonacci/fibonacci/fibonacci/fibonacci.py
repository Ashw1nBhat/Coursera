def calc_fib(n):
    if (n <= 1):
        return n
    num1 = 0
    num2 = 1
    for x in range(1,n):
        number = num1+num2
        num1=num2
        num2=number
    return number

n = int(input())
print(calc_fib(n))