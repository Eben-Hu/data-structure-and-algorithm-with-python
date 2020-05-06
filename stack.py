# here is the defination of class Stack
# last in first out 
# the end of list is the end of stack
class Stack:
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

# 全括号中缀表达式

