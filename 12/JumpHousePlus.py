
class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def isReachable(start,dest,p,q):
    assert(isinstance(start,Pos))
    assert(isinstance(dest,Pos))
    length = p if p>q else q
    width = q if p>q else p

    # need to prove that bount can be compute as below.
    left_bound = min(start.x,dest.x)-length
    right_bound = max(start.x,dest.x)+length

    upper_bound = max(start.y,dest.y)+length
    lower_bound = min(start.y,dest.y)-length

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
            queue.add(Pos(node.x+width,node.y+length))
            queue.add(Pos(node.x+width,node.y-length))
            queue.add(Pos(node.x-width,node.y+length))
            queue.add(Pos(node.x-width,node.y-length))
            queue.add(Pos(node.x+length,node.y+width))
            queue.add(Pos(node.x+length,node.y-width))
            queue.add(Pos(node.x-length,node.y+width))
            queue.add(Pos(node.x-length,node.y-width))

    return ret
