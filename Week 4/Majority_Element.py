
def get_majority_element(a, left, right):
    if left == right or left+1 == right:
        return a[left]
    

    mid = (left+right)//2 
    x = get_majority_element(a,left,mid)
    y = get_majority_element(a,mid,right)

    leftCount = 0
    for i in range(left,right):
        if(a[i] == x):
            leftCount += 1
    if(leftCount > (right-left)//2 ):
        return x

    rightCount = 0
    for i in range(left,right):
        if(a[i] == y):
            rightCount += 1
    if(rightCount > (right-left)//2 ):
        return y
    return -1


n = int(input())
a = list(map(int,input().split()))

if get_majority_element(a, 0, n) != -1:
    print(1)
else:
    print(0)