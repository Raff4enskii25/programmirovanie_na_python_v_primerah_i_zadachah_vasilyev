class Alpha:
    def __init__(self,num) -> None:
        self.code=num
    def show(self):
        print("Class Alpha:",self.code)
class Bravo(Alpha):
    def show(self):
        print("Class Bravo:", self.code)
        super().show()
class Charlie(Alpha):
    def show(self):
        print("Class Charlie:",self.code)
        super(Charlie,self).show()
class Delta(Bravo,Charlie):
    def show(self):
        print("Class Delta:", self.code)
        super().show()
        Charlie.show(self)
        super(Bravo,self).show()
def display(MyClass):
    print("Наследование для", MyClass.__name__)
    k=1
    for s in MyClass.__mro__:
        print(f"[{k}] {s.__name__}")
        k+=1
display(Alpha)
A=Alpha(100)
A.show()
display(Bravo)
B=Bravo(200)
B.show()
display(Charlie)
C=Charlie(300)
C.show()
display(Delta)
D=Delta(400)
D.show()