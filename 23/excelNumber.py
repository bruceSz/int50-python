def excelToDec(Enumber):
    chrSeq = [chr(i).upper for i in range(97,123)]
    numSeq = [i for i in range(1,27)]
    charNumMap=dict(zip(chrSeq,numSeq))
    ret = 0

    for ch in Enumber:
        ret = ret*26
        dec = charNumMap[ch]
        ret = ret + dec

    return ret

def decToExcel(Dnumber):
    
    chrSeq = [chr(i).upper for i in range(97,123)]
    numSeq = [i for i in range(1,27)]
    charNumMap=dict(zip(numSeq,chrSeq))
    ret=[]
    while Dnumber!=0:
        Dnumber,rem = divmod(Dnumber,26)
        if rem==0:
            rem==26
            Dnumber-=1
        ret.insert(0,charNumMap[rem])

    return reduce(lambda x,y:str(x)+str(y),ret)



