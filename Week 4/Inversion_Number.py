


def InversionNumber(a,left,right):
    inversions = 0
    if right - left == 1 and a[left] > a[right]:
        return 1
    elif right - left <= 1:
        return inversions
    mid = (left + right) // 2
    inversions += InversionNumber(a,left,mid)
    inversions += InversionNumber(a,mid+1,right)
    
    L = a[:mid]
    R = a[mid:]
    (i,j,k) = (0,0,0)

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
            inversions += 1
        k += 1

    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1
    print(a)
    return inversions

n = int(input())
a = list(map(int,input().split()))
print(InversionNumber(a,0,n-1))