def checkValid(str_):
    return True
def multiply(str1,str2):
    assert(checkValid(str1))
    assert(checkValid(str2))

    # assume str1 and str2 are well formatted number 
    # they are just too big!

    sign = ''
    if (str1[0]=='-' and str2[0]=='-') or (str1[0]!='-' and str2[0]!='-'):
        sign = ''
    else:
        sign='-'

    if str1[0]=='-':
        str1=str1[1:]
    if str2[0]=='-':
        str2=str2[1:]
    tmpret = []
    ret = [0 for i in range(len(str1)+len(str2))]

    for i in range(len(str1)-1,-1,-1):
        curry = 0
        for j in range(len(str2)-1,-1,-1):
            t = str2[j]*str1[i]+curry
            number,rem = divmod(t,10)
            tmpret.insert(0,rem)
            curry = number
        if curry!=0:
            tmpret.insert(0,curry)

        curry  = 0
        indStr2 = len(tmpret)-1
        for ind in range(i,i+len(tmpret)):
            t=ret[i]+tmpret[indStr2]+curry
            num,rem = divmod(t,10)
            num = curry
            ret[i]=rem
            indStr2-=1

        if curry != 0:
            # assume curry equals to 1
            assert(curry==1)
            ret[ind+1]=curry

    return ret.reverse()
