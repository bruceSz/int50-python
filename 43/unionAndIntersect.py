def movNext(pos,arr):
    pos+=1
    while pos < len(arr) and arr[pos]==arr[pos-1] 
    return pos


def arrayUnion(arr1,arr2):
    import array
    ret = array.array(arr1.typecode)
    i = 0
    j = 0
    while i< len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            ret.append(arr1[i])
            i = movNext(i,arr1)
        else arr1[i]>arr2[j]:
            ret.append(arr2[j])
            j = movNext(j,arr2)

        else:
            ret.append(arr1[i])
            i = movNext(i,arr1)
            j = movNext(j,arr2)

    if i < len(arr1):
        ret.extend(arr1[i:])
    
    if j < len(arr2):
        ret.extend(arr2[j:])

    return ret
        
        
def arrayIntersect(arr1,arr2):
    from array import array
    ret = array(arr1.typecode)
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i = movNext(i,arr1)
        elif arr1[i]>arr2[j]:
            j = movNext(j,arr2)
        else:
            ret.append(arr1[i])
            i = movNext(i,arr1)
            j = movNext(j,arr2)

    return ret
