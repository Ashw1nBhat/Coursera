

def gcd(a, b):
    if a==0 or b==0:
        return 0

    if a==b:
        return a

    if a<b:
        minimum=a
        maximum=b
    else:
        minimum=b
        maximum=a

    while minimum:
        maximum,minimum = minimum,maximum%minimum

    return maximum
    
    


a, b = map(int, input().split())
print(gcd(a, b))    
