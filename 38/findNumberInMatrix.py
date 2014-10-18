def findNumber(matrix,n,m,target):
    
    for i in range(n-1,-1,-1):
        if matrix[i][m-1]==target:
            return True

        elif matrix[i][m-1]<target:
            break


    if i==n-1:
        # larger than biggest of the matrix
        return False

    possible_row = i+1
    for i in range(m-1,-1,-1):
        if matrix[possible_row][i]==target:
            return True

    return False



        
