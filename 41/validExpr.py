def Node:
    def __init__(self,val):
        self.inp = val
        self.movMap = {}
        self.number = 1
        self.callbacks = {}

    def numberInc(self):
        self.number += 1

    def numberDesc(self):
        self.number -= 1

def initStateMachine(numbers,operator,parenthesis):
    start = Node('')
    l_paren = Node('(')
    operator = Node('+-*/')
    numbers = Node('0123456789')

    start.movMap[')']=None
    for char in '0123456789':
        start.movMap[char] = numbers

    start.movMap['('] = l_paren
    for char in '+-*/':
        start.movMap[char]=None

    l_paren.movMap['(']=l_paren
    l_paren.callbacks['(']= lambda x:x.numberInc()
    for char in '0123456789':
        l_paren.movMap[char] = numbers
    for char in '+-*/':
        l_paren.movMap[char]=None

    l_paren.movMap[')']
    l_paren.callbacks[')'] = lambda x:x.numberDesc()

    numbers.movMap['('] = None
    for char in '0123456789':
        numbers.movMap[char] = numbers
    for char in '+-*/':
        l_paren.movMap[char]=operator

    numbers.mov[')']=l_paren
    numbers.callbacks[')']=lambda x:x.movMap[')'].numberDesc()

    operator.movMap[')']=None
    for char in '0123456789':
        operator.movMap[char] = numbers
    for char in '+-*/':
        operator.movMap[char]= None

    operator.movMap['(']=l_paren
    operator.callbacks['(']=lambda x:x.movMap['('].numberDesc()

    
    return start

def isValid(sm,expr):
    node = sm 
    for i in expr:
        if node.movMao[i]== None:
            return False

        else:
            if node.callbacks[i]:
                node.callbacks[i]()
            node = node.movMap[i]

    return True
        
    
    
def isValidExpr(expr):
    numbers = '0123456789'
    operator = '+-*/'
    parenthesis = '()'
    sm = initStateMachine(numbers,operator,parenthesis)
    return isValid(expr,sm)
