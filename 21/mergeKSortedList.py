import copy
import sys

class Node:
    def __init__(self,val):
        self.val = val
        self.ne = None


def mergeKSortedList(k,*args):
    heads = list(args)
    numberOfEmptyList = 0
    # init k pointers
    ret = None
    tmps = [heads[i] for i in range(k)]
    while numberOfEmptyList<k-1:
        tmp = min(tmps,key=lambda x:x.val)
        index = tmps.index(tmp)
        if ret==None:
            ret=copy.copy(tmp)
        else:
            ret.ne = copy.copy(tmp)
        if tmp.ne==None:
            # here we don't change those origin link
            # maxint can never be min
            tmps[index]=Node(sys.maxint)
            numberOfEmptyList += 1
        else:
            tmps[index]=tmp.ne

    
    return ret
        
        
