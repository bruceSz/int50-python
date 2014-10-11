class TreeNode:
    def __init__(self,value):
        self.val = value
        self.children = []
    def addChild(self,childNode):
        if childNode != None:
            self.children.add(childNode)
        
def maxPathValSum(root):
    subMaxVal = 0
    childSums = []
    maxChildSumSum = 0
    subPathSum = 0
    for child in root.children:
        maxVal,sumChild = maxPathValSum(root)
        subMaxVal = maxVal if maxVal > subMaxVal else subMaxVal 
        childSums.add(sumChild)
    for i in range(len(childSums)):
        if childSums[i]>subPathSum:
            subPathSum = childSums[i]
        for j in range(i+1,len(childSums)):
            if childSums[i]+childSums[j]>maxChildSumSum:
                maxChildSumSum = childSums[i]+childSums[j]

    if maxChildSumSum > subMaxVal:
        subMaxVal = maxChildSumSum

    return subMaxVal,subPathSum

