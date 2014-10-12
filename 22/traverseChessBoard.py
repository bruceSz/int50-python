def dfs(visitedIndex,start,sameY,sameX,xindexs,yindexs):
    visitedIndex.add(start)
    if len(visitedIndex)==len(xindexs):
        return True
    lx = sameX[xindexs[start]]
    ly = sameY[yindexs[start]]
    for ind in lx:
        if not ind in visitedIndex:
            if dfs(visitedIndex,ind,sameY,sameX,xindexs,yindexs):
                return True
    for ind in ly:
        if not ind in visitedIndex:
            if dfs(visitedIndex,ind,sameY,sameX,xindexs,yindexs)
                return True

    return False


def existPath(xindexs,yindexs,n,m):
    check = all(map(lambda x:x>=0 and x<n,xindex))
    assert(check==True)
    check = all(map(lambda y:y>=0 and y<m,yindexs))
    assert(check==True)

    visitedIndex = set()
    sameY = {}
    sameX = {}
    for i in range(len(xindexs)):
        if sameY[yindexs[i]]==None:
            sameY[yindexs[i]]=[i]
        else:
            sameY[yindexs[i]].append(i)

        if sameX[xindexs[i]]==None:
            sameX[xindexs[i]]=[i]
        else:
            sameX[xindexs[i]].append(i)

    ret = dfs(visitedIndex,xindexs,yindexs,sameY,sameX)
    return ret




    

