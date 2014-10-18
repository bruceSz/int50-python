import array
def countPathNumber(grid,n,m,blocked):
    visited = array.array('b',(0 for i in range(n*m))) 

    for i in range(n):
        for j in range(m):
            if blocked[i][j]:
                visited[i*m+j]=1

    return doCountPathNumber(grid,n,m,visited,0,0):

def generateNext(n,m,visited,row,column):
    if row<n-1:
        if visited[row+1][column]==0:
            yield (row+1,column)

    if column < m-1:
        if visited[row][column+1]==0:
            yield (row,column+1)
    
def doCountPathNumber(grid,n,m,visited,row,column):
    if row == n-1 and column == m-1:
        return 1
    number = 0
    for c_row,c_col in generateNext(n,m,visited,row,column):
        visited[c_row][c_col]=1
        number += doCountPathNumber(grid,n,m,visited,c_row,c_col)

    return number
        

    
    
    
