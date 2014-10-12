def add(str1,str2):
    ret = ''
    curry = 0
    length = len(str1) if len(str1)>len(str2) else len(str2)
    for i in range(length):
        if i<len(str1):
            number1 = str1[len(str1)-1-i] 
        else:
            number1 = 0

        if i<len(str2):
            number2 = str2[len(str2)-1-i]

        ret = (number1 +number2 + curry)%10+ret
        curry = (number1+number2+curry)/10

    if curry != 0:
        assert(curry==1)
        return 1+ret

    else:
        return ret

