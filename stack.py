# here is the defination of class Stack
# last in first out 
# the end of list is the end of stack
class Stack:  #堆栈的列表构造
    def __init__(self):
        self.items = []  # use a list to build a stack
    
    def isEmpty(self):
        return self.items == [] 
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

# # after defining, the following codes are testing codes:
# # s = Stack()
# # print(s.isEmpty())
# # s.push('dog')
# # print(s.peek())
# # s.push(True)
# # print(s.size())
# # print(s.isEmpty())
# # s.push(8.4)
# # print(s.pop())
# # print(s.pop())
# # print(s.size())

# # test is ok

# 接下来用链表实现堆栈功能：
# the definition of node
class Node: # node is the element of an unorderedlist
    def __init__(self, initdata):
        self.data = initdata
        self.next = None   #默认是none
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext
    
class Stack2:
    def __init__(self):
        self.head = None


# # brackets matching:
# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced == 1:
#         symbol = symbolString[index]
#         if symbol == '(' :
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 s.pop()
#         index += 1

#     if s.isEmpty() == 1 and balanced == True:
#         return True
#     else:
#         return False

# print(parChecker('((()((()))))'))
# print(parChecker('((()'))

# more kinds of brackets ()[]{}
# my method:
# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced == 1:
#         symbol = symbolString[index]
#         if symbol in  '([{' :
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 top = s.pop()
#                 if not matches(top, symbolString):
#                     balanced = False
#         index += 1

#     if s.isEmpty() == 1 and balanced == True:
#         return True
#     else:
#         return False

# def matches(left,right):
#     opens = "([{"
#     closers = ")]}"
#     return opens.index(left) == closers.index(right)

# decimal convert to binary
# the firt solution of dividing is the last number of answer
# so we use a stack
# def divideBy2 (decNumber) :
#     remstack = Stack()

#     while decNumber > 0:
#          rem = decNumber % 2
#          remstack.push(rem)
#          decNumber // 2

#     decsting = ''
#     while not remstack.isEmpty() :
#         decsting = decsting + str(remstack.pop())

#     return decsting


# print(divideBy2(12))


# def infixtoPostfix (infixexpr):
#     prec = {}
#     prec['*'] = 3
#     prec['/'] = 3
#     prec['+'] = 2
#     prec['-'] = 2
#     prec['('] = 1
#     opStack = Stack()
#     postfixList = []
#     tokenList = infixexpr.split()

#     for token in tokenList:
#         if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
#             postfixList.append(token)
#         elif token == '(':
#             opStack.push(token)
#         elif token == ')':
#             topToken = opStack.pop()
#             while topToken != '(':
#                 postfixList.append(topToken)
#                 topToken = opStack.pop()
#         else:
#             while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
#                 postfixList.append(opStack.pop())
#             opStack.push(token)

#     while not opStack.isEmpty():
#         postfixList.append(opStack.pop())
    
#     return ''.join(postfixList)

# print(infixtoPostfix("A * B + C * D"))
# print(infixtoPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
        


# def postfixEval (postfixExpr):
#     operandStack = Stack()
#     tokenList = postfixExpr.split()

#     for token in tokenList:
#         if token in '0123456789':
#             operandStack.push(token)
#         else:
#             operation2 = operandStack.pop()
#             operation1 = operandStack.pop()
#             result = doMath(token,operation1,operation2)
#             operandStack.push(result)
    
#     return operandStack.pop()

# def doMath(op, op1,op2):
#     if op == "*":
#         return op1 * op2
#     elif op == "/":
#         return op1 / op2
#     elif op == "+":
#         return op1 + op2
#     else:
#         return op1 - op2

# print(postfixEval('7 8 + 3 2 + /'))

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token)) #pay attention to this int()
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
        
print(postfixEval('7 8 + 3 2 + /'))
