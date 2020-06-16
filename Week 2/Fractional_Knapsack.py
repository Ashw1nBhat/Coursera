import sys

def MergeSort(inputList,inputList2):
    if(len(inputList)>1):

        mid = len(inputList)//2
        left = inputList[:mid]
        right = inputList[mid:]
        left2 = inputList2[:mid]
        right2 = inputList2[mid:]

        MergeSort(left,left2)
        MergeSort(right,right2)

        i,j,k = 0,0,0

        while i<len(left) and j<len(right):
            if(left[i]>right[j]):
                inputList[k] = left[i]
                inputList2[k] = left2[i]
                i += 1
            else:
                inputList[k] = right[j]
                inputList2[k] = right2[j]
                j += 1
            k += 1
        
        while i<len(left):
            inputList[k] = left[i]
            inputList2[k] = left2[i]
            i += 1
            k +=1
        while j<len(right):
            inputList[k] = right[j]
            inputList2[k] = right2[j]
            j += 1
            k +=1


def get_optimal_value(capacity, weights, values):
    valueByWeight = []

    for i in range(len(weights)):
        valueByWeight.append(values[i]/weights[i])

    MergeSort(valueByWeight,weights)
    
    

    x = 0
    totalValue = 0

    for i in range(len(weights)):
        if capacity == 0:
            return totalValue
        if(weights[i]>0):
            if(weights[i]<=capacity):
                a = weights[i]
            else:
                a = capacity
        totalValue += (a * valueByWeight[i])
        weights[i] -= a
        capacity -= a
        

        

    return totalValue



data = list(map(int, sys.stdin.read().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))
