class Alpha:
    def __init__(self,num):
        self.code=num
        print("Присвоено значение полю code")
    def show(self):
        print("Поле code:",self.code)
class Bravo(Alpha):
    def __init__(self,num,txt):
        super().__init__(num)
        self.name=txt
    def show(self):
        #вызов метода из базового класса
        super().show()
        print("Поле name:", self.name)
class Charlie(Bravo):
    def __init__(self,num,txt,val):
        #вызов конструктора из базового класса
        super().__init__(num,txt)
        self.value=val
        print("Присвоено значение полю value")
    def show(self):
        super().show() #вызов метода из базового класса
        print("Поле value:", self.value)
print("Object A")
A=Alpha(100)
A.show()
print("Object B")
B=Bravo(200,"B")
B.show()
print("Object C")
C=Charlie(300,"C",[1,2,3])
C.show()