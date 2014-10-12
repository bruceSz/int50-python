class BinarySearchTree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

import sys
def checkSearchTree(root):
    
    if root == None:
        return True,-sys.maxint,sys.maxint

    else:
        isSearchTree,lminV,lmaxV = checkSearchTree(root.left)
        if not isSearchTree:
            return False,0,0

        isSearchTree,rminV,rmaxV = checkSearchTree(root.left)

        if not isSearchTree:
            return False,0,0
        if not (root.val >= lmaxV and root.val =< r.minV):
            return False,0,0

        return True,lminV,rmaxV


        
