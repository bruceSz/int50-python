import array
class Node:
    def __init__(self,char):
        self.char = char
        self.isEnd = False
        #self.leaves = array.array('b',(0 for i in range(26)))
        self.leaves = [None for i in range(26)]

def doInitTrieTree(root,word):
    if len(word)==0:
        root.isEnd = True
        return
    char = word[0]
    charInt = int(char)-int('a')
    if root.leaves[charInt]==None:
        root.leaves[charInt]=Node(char)

    return doInitTreeTree(root.leaves[charInt],word[1:])


def initTrieTree(words):
    root = Node('')
    for word in words:
        doInitTrieTree(root,word)
    return root


# copied from 36
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


#copied from  36
def initWithGrid(grid,n,m):
    ret = {}
    for i in range(n):
        for j in range(m):
            if not grid[n][m] in ret:
                ret[grid[n][m]]=[(i,j)]
            else:
                ret[grid[n][m]].append((i,j))
    return ret


def initWithGrid(grid,n,m):
    ret = {}
    for i in range(n):
        for j in range(m):
            if not grid[n][m] in ret:
                ret[grid[n][m]]=[(i,j)]
            else:
                ret[grid[n][m]].append((i,j))
    return ret

def doFindWords(grid,n,m,root,visited,row,column):
    if root.isEnd:
        return True
    for c_row,c_column in generateNext(row,column,visited): 
        c_char =  grid[c_row][c_column]
        ind = int(c_char)-int('a')
        if root.leaves[ind]==None:
            return continue
        visited[c_row*m+c_column]=1
        ret = doFindWords(grid,n,m,root.leaves[ind],visited,c_row,c_column)
        if ret:
            return True
        visited[c_row*m+c_column]=0


def findWords(grid,n,m,words):
    root = initTrieTree(words)
    chrMap = initWithGrid(grid,n,m)
    visited = array.array('b',(0 for i in range(n*m)))
    for left in root.leaves:
        if left != None:
            for row,column in chrMap[left.char]:
                visited[row*m+column] = 1
                ret = doFindWords(grid,n,m,left,visited,row,column)
                if ret:
                    return ret
                visited[row*m+column] = 0
                
