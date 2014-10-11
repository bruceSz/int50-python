class LinkNode:
    def __init__(self):
        self.ne = None
        self.random = None

def copyLinkedList(head):
    tmp = head
    while tmp!=None:
        newNode = LinkNode()
        nextNode = tmp.ne
        tmp.ne = newNode
        newNode.ne = nextNode
        tmp = nextNode

    tmp = head
    while tmp!=None:
        tmp.ne.randome = tmp.randome.ne
        tmp = tmp.ne.ne

    # break this two linked list
    tmp1 = head
    head2 = head.ne
    tmp2 = head2
    if tmp1.ne.ne ==None:
        tmp1.ne=None
        return tmp2

    while tmp1!=None:
        tmp2.ne = tmp1.ne
        tmp2 = tmp2.ne

        tmp1.ne=tmp1.ne.ne
        tmp1 = tmp1.ne

    return tmp2
        

