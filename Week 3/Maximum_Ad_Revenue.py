def MergeSort(inputList):
    if(len(inputList)>1):

        mid = len(inputList)//2
        left = inputList[:mid]
        right = inputList[mid:]
        

        MergeSort(left)
        MergeSort(right)

        i,j,k = 0,0,0

        while i<len(left) and j<len(right):
            if(left[i]>right[j]):
                inputList[k] = left[i]
                i += 1
            else:
                inputList[k] = right[j]
                j += 1
            k += 1
        
        while i<len(left):
            inputList[k] = left[i]
            i += 1
            k +=1
        while j<len(right):
            inputList[k] = right[j]
            j += 1
            k +=1



def MaxAdRev(n,a,c):
    max=0
    MergeSort(a)
    a.reverse()
    MergeSort(c)
    c.reverse()
    for i in range(n):
        max += a[i] * b[i]
    return max


n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(MaxAdRev(n,a,b))