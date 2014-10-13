def doBinarySearchVar(L,begin,end):
    middle = -1
    assert(begin<=end)
    while L[begin]>L[end]:
        middle = (begin+end)/2
        if L[middle] > L[begin]:
            begin = middle+1

        if L[middle]<L[end]:
            end = middle-1

    if begin < end:
        return begin-1
    else:
        return end
        

def BinarySearchVar(L):
    if len(L)==0 or len(L)==1:
       return -1 
    if L[len(L)-1]>L[0]:
        return len(L)-1

    return doBinarySearchVar(L,0,len(L)-1)
    
        
def findNumber(L):
    ind = BinarySearchVar(L)

