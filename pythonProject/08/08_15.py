class MyClass:
    def __init__(self, name, n=1):
        self.name = name
        if n==1:
            self.next=None
        else:
            self.next=MyClass(self.name,n-1)
        self.set()
    def __del__(self):
        print("Удаление:", self.code)
    def set(self, num=1):
        self.code=self.name+"["+str(num)+"]"
        if self.next!=None:
            self.next.set(num+1)
    def show(self):
        print(self.code)
        if self.next!=None:
            self.next.show()
print("Один объект:")
A=MyClass("Alpha")
A.show()
print("Цепочка из 5 объектов:")
B=MyClass("Bravo",5)
B.show()
print("Начиная с третьего объекта:")
B.next.next.show()
print("Удаление объектов")
del A
del B