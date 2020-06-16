def GetChange(m):
    a,b,c,count = 1,5,10,0

    if(m<=0):
        return 0
    
    while(m!=0):
        if(m>=c):
            m-=c
            count = count+1
        elif(m>=b):
            m-=b
            count = count+1
        elif(m>=a):
            m-=a
            count = count+1

    
    
    return count
    

input = int(input())
print(GetChange(input))  
