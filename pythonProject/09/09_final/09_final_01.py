#1. Напишите программу, в которой создается цепочка наследования 
#из трех классов. У объекта исходного класса имеется поле, и у каждого 
#следующего класса добавляется по одному полю. Опишите методы, 
#переопределяемые в производных классах, которые позволяют присваивать
#значения полям и отображать значения полей.
print("Задание 1")
class Main:
    def __init__(self,num):
        self.number = num
    def show(self):
        print("number =", self.number)

class Continue(Main):
    def __init__(self,num=1, txt='txt'):
        super().__init__(num)
        self.text = txt
    def show(self):
        super().show()
        print("text =",self.text)

class Finish(Continue):
    def __init__(self, num=1, txt="Text", val=[1,2,3]):
        super().__init__(num,txt)
        self.value = val
    def show(self):
        super().show()
        print("value =",self.value)

M=Main(123)
M.show()
print("-"*15)
C=Continue(456, "Hello!")
C.show()
print("-"*15)
F=Finish(789, "Hi!", [1,2,3])
F.show()
print("-"*15)

