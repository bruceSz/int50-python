data = []
def init(N):
    for i in range(N+1):
        data.append(i)


def removeItem(x):
    tmp = data[x]
    data[x]=x+1

def getNext(x):
    if x==data[x]:
        return x

    else:
        return getNext(x+1)

def query(x):
    if data[x+1] == x+1:
        x+1
    else:
        data[x+1]=getNext(x+1)
        if x+1 == N:
            return -1
        else:
            # here data[x+1]==data[data[x+1]]
            return data[x+1]

        
    
    
