# 选择list的末端作为栈顶

'''
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push (self, item):
        self.items.append(item)



    '''



class Fraction:
    '''
    This is called constructor, which is necssary for a class.
    To create an instance of this class, we must invoke, that is to say,
    pass actual values to the necessary states(here are top and bottom)
    Like myf = Fraction(3,4)
    self must be the first parameter to refer back to the object itself.
    num and den are two states of this class
    '''
    def __init__ (self, top, bottom):   
        self.num = top                 
        self.den = bottom

    # This is a method which is overrided
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    
    def __eq__(self, other): #This could change the deep equality  to shallow equality
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n



f1 = Fraction(1,2)
f2 = Fraction(2,4)
f3 = f1 + f2
print(f3)
print(f1 == f2)