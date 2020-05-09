'''
采用链表实现无序表
无序表本身不包含数据项，数据项都在链表的节点中
无序表包含的head起到指向第一个节点的作用
'''
# the definition of node
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext


class UnorderedList():
    def __init__(self):
        self.head = None
    
    def add(self, item): #加在表头
        temp = Node(item)
        temp.setNext(self.head)  # 注意这里的顺序，先把原表头的信息复制过来，然后再更新表头信息
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found  = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
    def append(self, item):
        end = False
        current = self.head
        while not end:
            if current.getNext() == None:
                end  = True
            else:
                current = current.getNext()
        temp = Node(item)
        temp.setData(item)
        current.setNext(temp)

    def isEmpty(self):
        current = self.head
        if current.getNext() == None:
            return True
        else:
            return False
    
    def index(self, item):
        current = self.head
        found = False
        count = 0
        while not found:
            count = count + 1
            if current.getData() == item:
                found = True
                return count
            else:
                current = current.getNext()
        if not found:
            return False
        
    def insert(self, pos, item):
        previous = None
        current = self.head
        flag = 1
        while flag != pos:
            flag = flag +1
            previous = current
            current = current.getNext()
        if previous == None:
            self.add(item)
        else:
            temp = Node(item)
            temp.setNext(current.getNext())
            previous.setNext(temp.getNext())
        
    def pop(self):
        end = False
        previous = None
        current = self.head
        while not end:
            if current.getNext() == None:
                end = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = None
            return current.getData()
        else:
            previous.setNext(None)
            return current.getData()
        
    def popp(self, pos):
        previous = None
        current = self.head
        flag = 1
        while flag != pos:
            flag = flag + 1
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = current.getNext()
            return current.getData()
        else:
            previous.setNext(current.getNext())
            return current.getData()
            
        


        




               
