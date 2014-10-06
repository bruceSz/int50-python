def maxSubArrSum(l):
    curr_sum = 0
    max_sum = 0
    for i in range(len(l)):
        curr_sum = max(curr_sum+l[i],0)
        max_sum = max(max_sum,curr_sum)

    return max_sum
