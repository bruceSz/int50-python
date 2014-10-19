class Area:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        
        self.x2 = y2
        self.y2 = y2


def minOverlapArea(H,W,rects):
    canx = []
    cany = []
    canx.append(0)
    canx.append(H-h)
    cany.append(0)
    cany.append(W-w)
    for rect in rects:
        if rect.x1-h >= 0:
            canx.append(x1)

        if rect.y1-w >=0:
            cany.append(y1)

        if rect.x2+h<=H:
            canx.append(x2)

        if rect.y2+w <= W:
            cany.append(y2)

    # bound
    result = h*w
    for i in canx:
        for j in cany:
            may = 0
            for rect in rects:
                x1 = max(i,rect.x1)
                y1 = max(j,rect.y1)
                x2 = min(i+h,rect.x2)
                y2 = min(j+w,rect.y2)

                if x2>x1 and y2>y1:
                    may+=(x2-x1)*(y2-y1)

            result = min(result,may)

    return result
