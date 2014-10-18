def strConversion(l):
    space_count = 0
    for i in range(len(l)):
        if l[i]==' ':
            space_count += 1

    mov = space_count*2
    for i in range(len(l)-1,-1,-1):
        if l[space_count]>0:
            if l[i]!=' ':
                l[i+space_count]=l[i]
            else:
                l[i+space_count]='0'
                l[i+space_count-1]='2'
                l[i+space_count-2]='%'
                space_count-=2

    return l

        
