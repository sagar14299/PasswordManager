#if we pass more or less argument than required than we face error.
#to overcome it we have method overriding method in python

class summation :
    def __init__(self):
        pass
    def adding(self, a=None, b=None, c=None):
        if a != None and b != None and c != None :
            s = a+b+c
            return s
        elif a != None and b != None :
            s = a+b
            return s
        else :
            s = a
            return s

s1 = summation()
print(s1.adding(1))
