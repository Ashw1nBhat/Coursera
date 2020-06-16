import sys

def largest_number(a):
    answer = []
    while(a != []):
        max = 0
        for digit in a:
            if(int(str(digit)+str(max))>=int(str(max)+str(digit))):
                max = digit
        answer.append(max)
        a.remove(max)
        
    return answer

n = int(input())
data = [int(i) for i in input().split()]
print(''.join(str(i) for i in largest_number(data)));
    