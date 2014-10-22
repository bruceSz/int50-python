class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def trans(root):
    if root == None:
        return None,None

    l_left,l_right = trans(root.left)
    if l_left==None:
        l_left = root
        
    r_left,r_right = trans(root.right)
    if r_right == None:
        r_right = root

    if not l_right==None:
        l_right.right = root
        root.left = l_right
        
    if not r_left == None:

        r_left.left = root
        root.right = r_left

    return l_left,r_right


        
        



