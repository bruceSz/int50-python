def next_permutation(l):
    if len(l) == 0:
        return False
    r_ordered = True
    for x in xrange(1,len(l)):
        if l[x]<l[x-1]:
            r_ordered = False
    if r_ordered:
        return false

    for x in range(len(l)-1,0,-1):
        # as it is not reverse ordered,
        # it must break out the the loop.
        if l[x]>l[x-1]:
            break
    start = x

    # guard value
    next_val = l[start]
    next_val_pos= start
    
    for x in range(start,len(l)-1):
        # it must be larger than l[start-1]
        # so there the l[x]>l[start-1] is just a 
        # secure program.
        if l[x]>l[start-1] and l[x]<next_val:
            next_val = l[x]
            next_val_pos = x

    l[start-1],l[next_val_pos] = l[next_val_pos],l[start-1]
    sort(l,start,len(l)-1)
    return True

        
def sort(l,begin,end):
    # use random quick sort
    from random import randint
    pivot = randint(begin,end)
    for x in range(begin,end+1):
        if x== pivot:
            continue
        if l[x] > l[pivot]:
            if not first_larger:
                first_larger = x
                second_larger = x
            else:
                if first_larger == second_larger:
                    second_larger = x
        else:

            l[first_larger],l[x] = l[x],l[first_larger] 

            if first_larger == second_larger:
                first_larger = x
                second_larger = x
            else:
                first_larger = second_larger
                for tmp in (second_larger+1,x):
                    if l[tmp]>l[pivot]:
                        second_larger = tmp
                        break

