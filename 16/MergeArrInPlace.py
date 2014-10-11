class FixLengthArray:
    def __init__(self,length):
        import sys
        self.innerL = [sys.maxint for i in range(length)]
    #TODO: magic method should be implemented here.
        
def mergeArrayInPlace(source, dest):

    
    # to simulate fix length array and the problem
    assert(isinstance(source,FixLengthArray))
    assert(isinstance(dest,FixLengthArray))
    import sys
    assert(dest.count(sys.maxint)==len(source))

    arr1,index1 = source,0
    arr2,index2 = dest,0
    moved = 0
    # as list is just
    while moved<len(source)+len(dest):
        if arr2[index2]<=arr1[index1] and arr2==dest:
            index2+=1
        elif arr2[index2]<=arr1[index1] and arr2 == source:
            # reuse vriable moved
            dest[moved],arr2[index2]=arr2[index2],dest[moved]

        elif arr2[index2]>arr1[index1] and arr2 ==dest:
            arr1[index1],arr2[index2]=arr2[index2],arr1[index1]
            arr2=source
            index2=index1
            index1+=1
        else:
            assert(arr2[index2]>arr1[index1])
            assert(arr2 == source)
            dest[moved],arr1[index1]= dest[moved],arr1[index1]
            index1+=1

        moved+=1

    return dest
            


