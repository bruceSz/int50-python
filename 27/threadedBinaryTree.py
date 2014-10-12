class TreeNode:
    def __init__(self):
        self.isLeftThread = False
        self.isRightThread = False
        self.left = None
        self.right = None

def makeThreadedBinaryTree(root):
    if root == None:
        return None,None
    retFirst = None
    retLast = None
    first,last = makeThreadedBinaryTree(root.left)
    if first==None:
        retFirst = root
    else:
        if last != None:
            assert(last.right == None)
            last.right = root
            last.isRightThread = True

    first,last = makeThreadedBinaryTree(root.right)
    if last== None:
        retLast = last

    else:
        if first!= None:
            assert(first.left == None)
            first.left = root
            first.isLeftThread = True
    return retfirst,retLast

