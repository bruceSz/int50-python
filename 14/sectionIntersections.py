class section:
    def __init__(self,b,e):
        self.begin = b
        self.end = e

def binarySearch(val,sections,begin,end):
    assert(begin>=0)
    assert(end<len(sections))
    while begin<end:
        middle = (begin+end)/2
        if sections[middle]<val:
            begin=middle+1
        elif sections[middle]>val:
            end = middle-1
        else:
            return middle

    assert(begin==end)
    if sections[begin]!=val
        return -1
    return begin

def bSearchHere(val,secs,begin,end):
    tmp = [sec.begin for sec in secs]
    index = -1
    index = binarySearch(val,tmp,begin,end)
    return index
    
    
def findIntersections(l):
    def cmpAccorToBegin(s1,s2):
        return cmp(s1.begin,s2.begin)

    so = sorted(l,cmpAccorToBegin)
    isIntersected = [False for i in so]
    for i in range(len(so)):
        if not isIntersected[i]:
            end = so[i].end
            index = bSearchHere(end,so,i+1,len(so)-1)
            if index != -1:
                isIntersected[i]=True
                isIntersected[index]=True
            
            
    return isIntersected
            
        
