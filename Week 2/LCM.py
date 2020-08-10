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


def lcm(a,b):
    if a==0 or b==0:
        return 0
    return int((a*b)/gcd(a,b))

    

a, b = map(int, input().split())
print(lcm(a, b))
