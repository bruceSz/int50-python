def genResult(visited,target):
    ret = []
    ret.insert(0,visited[target])
    while ret[0]!='':
        target = ret[0]
        ret.insert(0,visited[target])

    return ret[1:]
        
def findTransformPath(dict_list,from_str,to_str):
    queue = []

    dict_set = set(dict_list)
    assert(from_str in dict_set)
    assert(to_str in dict_set)
    
    visited = {}
    visited[from_str]=""
    answer = []
    queue.append(from_str)
    
    while len(queue)!=0:
        cur = queue.pop(0)
        for i in range(len(to_str)):
            for char in string.lowercase:
                tmp = cur[:i]+char+cur[i+1:]
                if tmp == to_str:
                    # to return earlier
                    visited[tmp]=cur
                    answer=genResult(visited,to) 
                    return answer
                if tmp in dict_set:
                    if not tmp in visited:
                        visited[tmp]=cur
                        queue.append(tmp)

    return answer


                
                
            
