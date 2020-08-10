def ValidMove(set):
    currQueenPos = len(set)-1
    for i in range(currQueenPos):
        if (currQueenPos-i) == abs(set[currQueenPos] - set[i]):
            return False
    return True

def IsSolution(set,n):
    if(len(set)==n):
        print(set)
        return

    for i in range(n):
        if i not in set:
            set.append(i)

            if(ValidMove(set)):
                IsSolution(set,n)

            set.pop()
    


IsSolution([],int(input()))