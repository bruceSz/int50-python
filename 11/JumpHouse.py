class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def isReachable(start,dest):
    assert(isinstance(start,Pos))
    assert(isinstance(dest,Pos))
    left_bound = min(start.x,dest.x)-2
    right_bound = max(start.x,dest.x)+2

    upper_bound = max(start.y,dest.y)+2
    lower_bound = min(start.y,dest.y)-2



    ret = False
    queue = []
    visited=set()
    queue.append(start)
    while len(queue)>0:
        node = queue.pop()
        if node.x == dest.x and node.y == dest.y:
            ret = True
        if node.x < left_bound or node.x > right_bound or node.y > upper_bound or node.y < lower_bound:
            continue
        if not node in visited:
            visited.add(node)
            queue.add(Pos(node.x+1,node.y+2))
            queue.add(Pos(node.x+1,node.y-2))
            queue.add(Pos(node.x-1,node.y+2))
            queue.add(Pos(node.x-1,node.y-2))
            queue.add(Pos(node.x+2,node.y+1))
            queue.add(Pos(node.x+2,node.y-1))
            queue.add(Pos(node.x-2,node.y+1))
            queue.add(Pos(node.x-2,node.y-1))
    

    return ret
