def paisano_length(m):
    prev=0
    curr=1
    for i in range(m*m-1):
        prev,curr = curr,(curr+prev) % m
        if(prev,curr) == (0,1):
            return i+1

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

def modulo_fib(n,m):
    paisanoLength = paisano_length(m)
    fibonacciNum = n % paisanoLength
    return calc_fib(fibonacciNum) % m


input = input()
n,m = map(int,input.split())

print(modulo_fib(n,m))
