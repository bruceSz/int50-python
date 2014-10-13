def candyDistribute(ratings):
    assert(len(ratings)>0)
    if len(ratings)==1:
        return 1
    ret = [0 for i in range(len(ratings))]
    low = []

    for i in range(len(ratings)):
        if i == 0 :
            if ratings[i]<=ratings[i+1]:
                ret[i]=1
                low.append(i)

        if i==len(ratings)-1:
            if ratings[i]<=ratings[i-1]:
                ret[i]=1
                low.append(i)


        if ratings[i]<= ratings[i+1] and ratings[i]<=ratings[i-1]:
            ret[i]=1
            low.append(i)

    for i in range(len(low)):
        if i == 0:
            for j in range(low[i]-1,-1,-1):
                ret[j]=ret[j+1]+1
        else:
            for j in range(low[i]-1,low[i-1],-1):
                    ret[j]=ret[j+1]+1

    for i in range(len(low)):
        met = False
        if i==len(low)-1:
            for j in range(low[i]+1,len(ratings)):
                ret[j] = ret[j-1]+1
        else:
            for j in range(low[i]+1,low[i+1]):
                if met:
                    break

                if ret[j]!=0:
                    met = True 
                    if ret[j-1]+1 > ret[j]:
                        ret[j]=ret[j-1]+1

    return reduce(lambda x,y:x+y,ret)
                
                


            
            
            
