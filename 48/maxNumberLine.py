class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def zero(f1,f2):
    return f1==f2

def maxNumbersLine(points):
    ret = 0
    for i in range(len(points)):
        same = 0
        vertical = 0
        gratients = []
        for point in points[i+1:]:
            float dx = points[i].x-point.x
            float dy = points[i].y-point.y
            if dx == 0:
                if dy == 0:
                    same+=1

                else:
                    vertical += 1
                    
            else:
                
                gradients.append(dy/dx)

        ret = vertical+same

        gradients.sort()
        length = len(gradients)
        for i in range(length):
            k = i+1
            tmp = 0
            while i<len(gradients) and gradients[i-1]==gradients[i]:
                tmp += 1

            ret = max(tmp+same,ret)

    return ret



            
        
    
    
