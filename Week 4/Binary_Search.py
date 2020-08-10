import sys

def BinarySearch(a,x):
    left = 0
    right = len(a)-1

    while left<=right:
        mid = (left+right)//2
 
        if(x == a[mid]):
            return mid
        elif(x < a[mid]):
            right = mid -1
        elif(x > a[mid]):
            left = mid+1

    return -1


a = [int(i) for i in input().split()]
search = [int(i) for i in input().split()]
n = a[0]
a = a[1:]

solution = list()
for i in search[1:]:
    ans = BinarySearch(a, i)
    solution.append(ans)
print(' '.join([str(i) for i in solution]))
