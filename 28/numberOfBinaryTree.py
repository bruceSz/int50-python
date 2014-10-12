# asssume we are dealing with postorder
def numberOfBianryTree(treeStr,begin,end):
    assert(begin<=end)
    if begin==end:
        return 1
    if begin==end-1:
        return 2

    ret = 0

    for i in range(begin,end-1):
        left = numberOfBinaryTree(treeStr,begin,i)
        right = numberOfBinaryTree(treeStr,i+1,end-1)
        ret += left * right * 2

    single = numberOfBinaryTree(treeStr,begin,end-1)

    ret += single*2

    return ret


        

    
