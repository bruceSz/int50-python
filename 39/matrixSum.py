def matrixSum(matrix,n,m):
    assert(n>0 and m>0)
    result = [[0 for i in range(m)] for i in range(n)]
    result[0][0] = matrix[0][0]

    matrixSums = [[0 for i in range(m)] for i in range(n)]

    for i in range(1,n):
        matrixSums[i][0]=matrix[i][0]

    for i in range(1,m):
        matrixSums[0][i]=matrix[0][i]

    for i in range(1,n):
        rowSum = matrix[i][0]
        for j in range(1,m):
            matrixSums[i][j]= matrix[i][j]+matrixSums[i-1][j]+rowSum
            rowSum += matrix[i][j]
            
    for i in range(1,n):
        for j in range(1,m):
            max_r = result[i-1][j] if result[i-1][j]>result[i][j-1] else result[i][j-1]

            if matrix[i][j] > max_r:
                max_r = matrix[i][j]
            for k in range(j-1,-1,-1):
                for l in range(i-1,-1,-1):
                    tmp = matrixSums[i][j]-matrixSums[l][j]
                    tmp1 = matrixSums[i][k]-matrixSums[l][k]
                    cur = tmp-tmp1

                    if cur > max_r:
                        b_row=l
                        b_col = k
                        max_r = cur 

            result[i][j]=max_r

    return result[n-1][m-1]
                    
                
            
            
        

    

