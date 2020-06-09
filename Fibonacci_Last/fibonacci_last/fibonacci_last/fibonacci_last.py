def calc_fib(x):
    if (x <= 1):
        return x
    num1 = 0
    num2 = 1
    for _ in range(1,x):
        number = num1+num2
        num1=num2
        num2=number
    return number%10   
    

n = int(input())

pre = [0] * 60

for i in range(0,60):
    pre[i] = calc_fib(i)

print(pre[n%60])
