def circleMaxSubArrSum(l):
    cur_sum = 0
    cur_max = 0
    start_pos = 0
    begin_new_sub = False
    for i in range(len(l)):
        cur_sum = max(cur_sum+l[i],0)
        if cur_sum ==0:
            begin_new_sub = True
        else:
            if begin_new_sub:
                begin_new_sub = False
                start_pos = i
        cur_max = max(cur_max,cur_sum)

    for i in range(start_pos):
        cur_sum = max(cur_sum+l[i],0)
        cur_max = max(cur_max,cur_sum)
        # TODO:

# awesome!
# from javaman's solution
def circleMaxSubArrSum(l):
    cur_max_sum = 0
    cur_min_max = 0
    cur_min = 0
    cur_max = 0
    total_sum = 0
    for i in range(len(l)):
        cur_max_sum = max(cur_max_sum+l[i],0)
        cur_min_sum = min(cur_min_sum+l[i],0)
        cur_max = max(cur_max_sum,cur_max)
        cur_min = min(cur_min_sum,cur_min)
        sum += l[i]

    return max(cur_max,sum-cur_min)

