# queue: first in first out :从队尾进去，从队首出去
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    # 热土豆/约瑟夫问题
    # def hotPotato(namelist,num):
    #     simqueue = Queue()
    #     for name in namelist:
    #         simqueue.enqueue(name)
        
    #     while not simqueue.isEmpty():
    #         for i in range(num):
    #             simqueue.enqueue(simqueue.dequeue())

    #         simqueue.dequeue()
        
    #     return simqueue.dequeue()
    
    # def hotPotato(namelist, num):
    #     simqueue = Queue()
    #     for name in namelist:
    #         simqueue.enqueue(name)

    #     while simqueue.size() > 1:
    #         for i in range(num):
    #             simqueue.enqueue(simqueue.dequeue())

    #         simqueue.dequeue()

    #     return simqueue.dequeue()

    # print(hotPotato(['1','2','3','4','5','6','7'],7))

    # 打印机任务太难了，暂时先搁置，回头来做

    #双向队列: 定义list的0是队尾，-1是队首
