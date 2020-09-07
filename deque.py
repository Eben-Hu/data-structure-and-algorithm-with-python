'''
use list to contruct queue
'''
class Deque :
    def __init__(self):
        self.items =[]
    
    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeRear(self):
        return self.items.pop(0)
    
    def removeFront(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# 回文词判定
def palchecker(aString):
    chardeque = Deque()
    stillEqual = True
    for ch in aString:
        chardeque.addRear(ch)
    
    while stillEqual and chardeque.size() > 1:
        front = chardeque.removeFront()
        rear = chardeque.removeRear()
        if front != rear:
            stillEqual = False
        
    return stillEqual

print(palchecker('radar'))
print(palchecker('abcdefg'))
