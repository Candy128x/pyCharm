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


class CSStudent:
    stream = 'cse';

    def __init__(self, roll):
        self.roll = roll

    def setAddrs(self, addrs):
        self.addrs = addrs

    def getAddrs(self):
        return self.addrs

a = CSStudent(101)
b = CSStudent(102)
a.setAddrs('Mumbai, Maharastra.')

print(a.stream)
print(b.stream)
print(a.roll)
print(CSStudent.stream)
print(a.getAddrs())
'''
OutPut:
cse
cse
101
cse
Mumbai, Maharastra.
'''