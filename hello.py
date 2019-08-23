class Demo:
    __x = 0
    def __init__(self, i):
        self.__i = i
        Demo.__x += 1
    def hello(self):
        print("hello", self.__i)

a = Demo("Tom")
a.hello()
#print(“Demo.x =”, Demo.__x) #受保護而不能存取