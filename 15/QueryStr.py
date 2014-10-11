class TrieNode():
    def __init__(self,character):
        self.cha = character
        self.nextCha = None
        self.search_dict = {}
class StrQueryMac(object):
    def __init__(self):
        self.TrieTree = None

    def initWithString(string):
        pre = None
        for cha in string:
            
            node = TrieNode(cha)
            if pre==None:
                pre = node
                self.TrieTree = node
            else:
                pre.nextCha = node
                pre = node
            if not cha in self.search_dict:
                self.search_dict[cha]=[node]
            else:
                self.search_dict[cha].add(node)

    def existSubString(query):
        if len(query)==0:
            return False

        beginChar = query[0]
        begin_nodes = self.search_dict[beginChar]
        for bNodes in begin_nodes:
            curNode = bNodes
            isSub = True
            for qChar in query:
                if curNode == None or qChar != curNode.cha:
                    isSub = False
                curNode=curNode.nextCha

            if not isSub:
                return False
            else:
                return True
        return False
                    

                
            
        
        
            
