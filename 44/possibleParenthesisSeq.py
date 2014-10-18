def gen(totalPairs, number_l,number_r,tmp,seqs):
    if number_r > number_l:
        return

    if number_l > totalPairs :
        return

    if number_r == n:
        seqs.add(tmp)
        return 

    gen(totalPairs,number_l+1,number_r,tmp+'(',seqs)
    gen(totalPairs,number_l,number_r+1,tmp+')',seqs)

        
def possibleParenthesisSeq(n):
    seqs = set()
    tmp=''
    gen(n,0,0,tmp,seqs)
    return seqs

