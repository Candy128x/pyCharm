class Test:
    def fun(self):
        print('Hello')

obj = Test()
obj.fun()
'''
OutPut:
Hello
'''

class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Hey My Name is name', self.name)

p = Person('Dev Kumar')
p.sayHi()
'''
OutPut:
Hey My Name is name Dev Kumar
'''