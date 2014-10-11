# assume the list l is already sorted.
def valueInArr(l,begin,end,value):
    # test it!
    while begin<=end:
        middle = (begin+end)/2
        if l[middle]==value:
            return middle
        elif l[middle]>value:
            end = middle-1
        else:
            begin=middle+1
        
    
def findTwoSum(l,begin,end,sumVal):
    import sys
    if l[begin]>=sumVal:
        return sys.maxint,sys.maxint
    else:
        while begin<end and l[begin]==l[begin+1]:
            begin+=1

        while begin<end:
            if l[begin]+l[end]>sumVal:
                end-=1
            elif l[begin]+l[end]<sumVal:
                begin+=1
            else:
                return begin,end

        if begin==end:
            return sys.maxint,sys.maxint

def findTreeSumZero(l):
    import sys
    ret = []
    length = len(l)
    for i in range(length):
        if i!=0 and l[i]==l[i-1]:
            continue
        b,e = findTwoSum(l,i+1,length-1,-l[i])
        if b!=sys.maxint:
            ret.append((l[i],b,e))

