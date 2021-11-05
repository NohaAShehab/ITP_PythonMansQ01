# abstraction
class ABC:
    def fun1(self,x,y):
        pass

    def fun2(self):
        pass

    def fun3(self):
        pass


class A:
    pass

    def __init__(self, a=""):
        self.a = a
        print("A constructor called ")


class B:
    def __init__(self, b=""):
        self.b = b
        print("B constructor called ")


class C:
    pass


class Factory(A, B, C, ABC):
    def __init__(self):
        self.a = A()
        self.b = B()

    #overriding
    def fun1(self,x,y):
        print(x,y)


f = Factory()
print("abc")
