def findPrime(N):
    
    ret = [True for i in range(N+1)]
    ret[0]=False
    ret[1]=False

    for i in range(len(ret)):
        if ret[i]:
            for j in range(i,N/i+1):
                ret[i*j]=False

    ret2 = []
    for i in range(N):
        if ret[i]:
            ret2.append(i)
    return ret2


def test_findPrime():
    ret = findPrime(50)
    assert(ret==[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])

        
        
