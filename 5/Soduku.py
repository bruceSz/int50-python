def isSudoku(grids):
    # sudoku is 9*9 grids.
    for i in range(9):
        mask = 0
        for j in range(9):
            index = i*9 + j
            # TODO: need more works here.
            if not isinstance(grids[index],int)  or grids[index]<=1 or grids[index]>9 or (mask&grids[index]==0):
                return False
            else:
                mask |= grids[index]
                

                



            
