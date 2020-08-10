def EditDistance(str1, str2, l1, l2): 
    
    lookup = [[0 for i in range(l2 + 1)] for i in range(l1 + 1)] 
  
    
    for i in range(l1 + 1): 

        for j in range(l2 + 1): 
  
            if i == 0: 
                lookup[i][j] = j    
  
            elif j == 0: 
                lookup[i][j] = i    
  
            elif str1[i-1] == str2[j-1]: 
                lookup[i][j] = lookup[i-1][j-1] 
  
            else: 
                lookup[i][j] = 1 + min(lookup[i][j-1], lookup[i-1][j], lookup[i-1][j-1])   
  
    return lookup[l1][l2] 
  
str1 = input()
str2 = input()
print(EditDistance(str1,str2,len(str1),len(str2)))
