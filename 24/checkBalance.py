class BinaryNode:
    def __init__(self):
        self.left = None
        self.right = None

def checkBalance(root):
    if root == None:
        return True,0

    else:
        isBalance,heightLeft = checkBalance(root.left)

        if not isBalance:
            return False,0

        isBalance,heightRight = checkBalance(root.right)
        if not isBalance:
            return False,0
        if abs(heightLeft-heightRight)>1:
            return False,0

        else:
            return True,heightLeft+1 if heightLeft>heightRight else heightRight + 1




