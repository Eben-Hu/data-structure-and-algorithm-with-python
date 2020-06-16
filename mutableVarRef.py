'''
注意到可变类型的变量引用 本质是 变量名称 指向 对象的地址
'''

myList = [1,2,3,4]
A = [myList] * 3
print(A)
print(id(myList))
print(id(A))
myList[1] = 999
print(A)
