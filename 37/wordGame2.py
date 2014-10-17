import array
class Node:
    def __init__(self,char):
        self.char = char
        self.isEnd = False
        self.leaves = array.array('b',(0 for i in range(26)))

def doInitTrieTree(root,word):
    if len(word)==0:
        root.isEnd = True
        return
    char = word[0]
    charInt = int(char)-int('a')
    if root.leaves[charInt]==0:
        root.leaves[charInt]=Node(char)

    return doInitTreeTree(root.leaves[charInt],word[1:])
        


def initTrieTree(words):
    root = Node('')
    for word in words:
        doInitTrieTree(root,word)
    return root


def findWords(grid,words):
    root = initTrieTree(words)
    
