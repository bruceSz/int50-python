def findMinAllOne(a):
    if a==0:
        return -1
    else :
        end = 0
        l=[False for i in range(1,a)]
        numberOne = 1

        while True:
        end = (end*10+1)%a
        if end(end==0):
            return numberOne
        if l[end]:
            break
        l[end]=True
        numberOne += 1

    return -1
            
