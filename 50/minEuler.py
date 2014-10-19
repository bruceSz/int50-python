import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def minEular(points):
    # here points is x sorted.
    length = len(points)
    distances = [[0.0 for i in range(length)] for i in range(length) ]


    for i in range(length):
        distances[i][i] = 0
        for j in range(i+1,length):
            distances[i][j] = math.sqrt(pow((points[i].x-points[j].x),2)+pow((points[i].y-points[j].y),2))


    accumulateDistance = [0.0 for i in range(length)]
    accumulateDistance[0]=0
    for i in range(1,length):
        # the distances matrix is sysmetric along with diagonal '\'
        accumulateDistance[i] = distances[i-1][i]+accumulateDistance[i-1]

    dp = [[0.0 for i in range(length)] for i in range(length)]
    # the distances matrix is sysmetric along with diagonal '\'
    for i in range(length-1,-1,-1):
        dp[length-1][i]= distances[i][length-1]

    for i in range(length-2,0,-1):
        # compute i => i-1
        # enumerate all next
        for j in range(i+1,length):
            if dp[i][i-1]==0:
                if not j-1 > i:
                    dp[i][i-1]= 
            
            
            
        
        

