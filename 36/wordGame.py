def generateNext(n,m,row,column,visited):
    ret = []
    if row > 0:
        if not visited[row-1][column]==1:
            ret.append((row-1,column))
    if row < n:
        if not visited[row+1][column]==1:
            ret.append((row+1,column))
    if column >0:
        if not visited[row][column-1]==1:
            ret.append((row,column-1))
    if column < m:
        if not visited[row][column+1]==1:
            ret.append((row,column+1))

    return ret
        
        
def doFindWord(grid,n,m,word,visited):
    if len(word)==0:
        return True
    for c_row,c_column in generateNext(n,m,row,column,visited):
        if grid[c_row][c_column]==word[0]:
            visited[c_row][c_column]=1
            ret = doFindword(grid,n,m,word[1:],visited)
            if ret :
                return True
            visited[c_row][c_column]=0
        
    
def initWithGrid(grid,n,m):
    ret = {}
    for i in range(n):
        for j in range(m):
            if not grid[n][m] in ret:
                ret[grid[n][m]]=[(i,j)]
            else:
                ret[grid[n][m]].append((i,j))
    return ret

def findWord(grid,n,m,word):
    ret = False
    chrMap = initWithGrid(grid,n,m)
    visited= [[ 0 for j in range(m)] for i in range(n) ]
    for row,column in chrMap[word[0]]:
        visited[row][column]=1
        ret = doFindWord(grid,n,m,word[1:],visited,row,column)
        if ret :
            return ret
        visited[row][column]=0

