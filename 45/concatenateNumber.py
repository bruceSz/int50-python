def findFit(numberList,start):
    i=start+1

    while i < min(numberList,key = lambda x:len(x)):
        num = max(numberList,key=lambda x:x[i])
        # count number of num if no is 1 return index of it
        count = 0
        for number in numberList:
            if number[i]==num:
                ind = i
                count +=1

        if count == 1:
            return number

        else:
            endList = filter(lambda x:len(x)-1==i,numberList)
            leftList = filter(lambda x:x[i]==num,numberList)


            if endList:
                if endList[0][start] >= max(leftList,key = lambda x:x[i+1]):
                    return endList[0]

            numberList = leftList

    # TODO:

            
            
            


    
def doConNumbers(numberList,pre):
    if len(numberList)==0:
        return pre
    num = numberList[-1][0]
    sameBegins = filter(lambda x:x[0]==num,numberList[:])
    lesser = filter(lambda x:x[0]<num,numberList[:])
    firstLesser = sorted(lesser,key = lambda x:x[0])[-1][0]
    # assume the order will be reserved.
    if len(sameBegins) == 1:
        # it must be the last one
        pre += numberList[-1]
        return doConNumbers(numberList[:-1],pre)

    else :
        fit = 



    
def concatenateNumbers(numberList):
    numberList = filter(lambda x:len(x)>0,numberList)
    numberList = sorted(numberList,key=lambda x:x[0])
    ret = doConNumbers(numberList,'')
    return ret
    
    
