# 找到递归的重点：问题的最小部分；然后调用自身

#  also 整数任意进制转换
# def toStr(n,base):
#     convertString = '0123456789ABCDEF'
#     if n < base:
#         return convertString[n]
#     else:
#         return toStr(n//base,base) + convertString[n%base]

# print(toStr(1453,16))

# 递归可视化：turtle 画图
# import turtle
# def tree(branch_len):
#     if branch_len > 5:
#         t.forward(branch_len) # 树干
#         t.right(20) # 右边的树枝
#         tree(branch_len - 15) 
#         t.left(40) # 左边的树枝
#         tree(branch_len - 15)
#         t.right(20) # 摆正
#         t.backward(branch_len) # 回到原位

# t = turtle.Turtle()
# t.left(90)
# t.penup()
# t.backward(100)
# t.pendown()
# t.pencolor('green')
# t.pensize(2)
# tree(75)
# t.hideturtle()
# turtle.done()


# sierpinski triangle : 当维度比上一个大一的时候，会多三个当前定点为定点，长度为上一个的长度的一半
import  turtle

def sierpinski(degree, points):
    colormap = ['blue', 'red', 'green','white', 'yellow', 'orange']
    drawTriangle(points, colormap[degree])
    if degree > 0:
        sierpinski(degree - 1,  # 先画左下角的三角
            {'left':points['left'], 
            'top':getMid(points['left'],points['top']),
            'right':getMid(points['left'],points['right'])})
        sierpinski(degree - 1, # 然后是中间上面的
            {'left':getMid(points['left'],points['top']),
            'top':points['top'],
            'right':getMid(points['top'],points['right'])})
        sierpinski(degree - 1,  # 最后是右下角的
        {'left':getMid(points['left'],points['right']),
        'top':getMid(points['top'],points['right']),
        'right':points['right']})

def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

t = turtle.Turtle()

points = {'left':(-200, -100),
            'top':(0, 200),'right':(200, -100)}

sierpinski(5, points)
turtle.done()








