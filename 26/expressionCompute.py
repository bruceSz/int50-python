def findNextOperand(expr,pos):
    if isinstance(expr,str):
        assert(pos<len(expr))
        ind = pos
        ret = ''
        while not expr[ind].isdigit():
            ret += expr[ind]
            ind +=1
        assert(ret!='')

        return int(ret),ind
    # only support str or list expr
    else:
        assert(pos<len(expr))
        return expr[pos],pos+1
        
def findNextOperator(expr,pos):
    assert(pos<len(expr))
    return expr[pos],pos+1
        
def expressionCompute(expression,pos):
    assert(pos<len(expression))
    loperand,next_pos = findNextOperand(expression,pos)

    # should be == len(x),> here is just for uncertainty coding
    if next_post >= len(expression):
        return loperand

    operator,next_pos = findNextOperator(expression,next_pos)
    while operator=='*':
        roperand,next_pos = findNextOperand(expression,next_pos)
        # assume the expression is in list data structure.
        loperand=loperand*roperand

        operator,next_pos = findNextOperator(expression,next_pos)

    return apply(generate(operator),[loperand,expressionCompute(expression,next_pos)])




