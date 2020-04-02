import time
import random

#要注意要求：如果要求了返回位置，可以用i做索引位置；不然直接做元素比较会更好。


alist = []

# def find_min(alist):
#     my_min = alist[0] #暂时记第一个元素是最小的
#     for i in alist:
#         flag = True #最小标记flag指示i是否为alist最小，初始为True
#         for j in alist:
#             if i >j: #如果i>j(存在比i小的数)
#                 flag = False #标记flag为false
#                 break # 为了复杂度的话，这个 break不能要吧
#         #当i为alist最小，my_min=i
#         if flag == 1:
#             my_min = i
#             break
#     return my_min

'''
def getMin(alist):
    min = alist[0]
    for i in range(len(alist)):
        flag = True
        for j in range(len(alist)):
            if alist[i] > alist[j]:
                flag = False
                break
        if flag == 1:
            min = alist[i]
    return min

listlength = 10
a = random.sample(range(1,listlength * 100),listlength)
start = time.time()
# b = find_min(a)
b = getMin(a)
end = time.time()
print(a)
print(f"The minimum element of list a is {b}. The procedure costs {end - start} seconds.")
'''
# def findMin(alist):
#     #初始化当前最小值minsofar=alist[0]
#     minsofar = alist[0]
#     #遍历alist
#     for i in alist:
#         #如果i小于minsofar
#         if i < minsofar:
#             minsofar = i
#     return minsofar

def getmin(alist):
    min = alist[0]
    for i in range(len(alist)):
        if alist[i] < min:
            min = alist[i]
    return min

listlength = 10
a = random.sample(range(1,listlength * 100),listlength) # random.sample(range , 元素个数）
start = time.time()
# b = find_min(a)
b = getmin(a)
end = time.time()
print(a)
print(f"The minimum element of list a is {b}. The procedure costs {end - start} seconds.")

#当list长度为100,000的时候，算法一等了1分多钟没算出来...
#当list长度为100,000*100的时候，算法二只要0.2s...
#当list长度为100,000*1000的时候，算法二python占用了3.2Gb内存，CPU占用30%，等了半分钟，也算不出来了...

'''
listSize = 100000000

alist = [randrange(10000000) for i in range(listSize)]
start = time.time()
print(find_min(alist))
end = time.time()
print('验证:%d'%min(alist))
print("listlength:{0},time:{1},O(n)=n^2".format(listSize,end-start))
print('---------------------------------------------------------------')
'''
'''
alist = [randrange(10000000) for i in range(listSize)]
start = time.time()
print(findMin(alist))
end = time.time()
print('验证:%d'%min(alist))
print("listlength:%d,time:%.30f,O(n)=n"% (listSize,end-start))
print('-------------------ENDENDENDENDENDENDEND-------------------------')
'''



    
