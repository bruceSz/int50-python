def findSubSeq(source,pattern):
    ret = []
    if len(source)==0 or len(pattern)==0:
        return ret

    l=[[0 for i in range(len(source))] for j in range(len(pattern))]
    l[0][0]= 1 if pattern[0]==source[0] else 0
    for i in range(1,len(source)):
        if pattern[0]==source[0] or l[0][i-1]==1:
            l[0][i]=1


    for i in range(1,len(pattern)):
        if pattern[i]==source[0] or l[i-1][0] ==1:
            l[i][0]=1

    for i in range(1,len(pattern)):
        for j in range(1,len(source)):
            if pattern[i]==source[j]:
                l[i][j]=l[i-1][i-1]+1
                ret.append(j)
            else:
                l[i][j]=l[i][j-1] if l[i][j-1]>l[i-1][j] else l[i-1][j]

    return ret

def differentSetStr(source,target):
    target_s = set(target)
    result = []
    for i in range(len(source)):
        if not i in target_s:
            result.append(i)

    return result

def differentString(source,target):
    indexs = set(differentSetStr(source,target))
    ret = []
    for i in range(len(source)):
        if i in indexs:
            ret.append(source[i])

    return str(ret)
            
def isInterleavedStr(str1,str2,targetStr):
    if len(targetStr)!=len(str1)+len(str2):
        return False

    subStrInTarget = findSubSeq(targetStr,str1)
    if len(subStrInTarget)!=len(str1):
        return False

    restStr=differentString(targetStr,subStrTarget)
    if restStr != str2:
        return False
    else:
        return True

