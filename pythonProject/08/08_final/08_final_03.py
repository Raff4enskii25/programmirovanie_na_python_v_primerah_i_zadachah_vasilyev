#3. Напишите программу, в которой описан класс. У объектов класса должно быть поле,
#  представляющее собой числовой список. Этот список формируется на основе списка,
#  переданного конструктору в качестве аргумента. При этом из списка-аргумента в
#  список-поле включаются только числовые элементы (элементы других типов игнорируются). 
# Необходимо также описать метод, отображающий содержимое поля-списка, а также метод,
#  вычисляющий среднее значение элементов поля-списка (сумма значений элементов, деленная на их количество).
print("Задание 3")
class MyClass:
    def __init__(self, l=["Пустой список"]):
        new_list = []
        for i in l:
            if type(i)==int or type(i)==float:
                new_list.append(i)
        if len(new_list)>0:
            self.list = new_list
    def show(self):
        if hasattr(self, "list"):
            print("Список:", self.list)
    def calculate(self):
        if hasattr(self, "list"):
            print("Среднее значение списка:", sum(self.list)/len(self.list))
        else:
            print("Список не содержит числовых значений!")

print("A - тип int")
A = MyClass([1,2,3,4,5])
A.show()
A.calculate()
print("B - тип float")
B = MyClass([1.5, 2.5, 3.5, 4.5, 5.5])
B.show()
B.calculate()
print("C - int и float")
C = MyClass([1,2,3, 4.5, 5.5])
C.show()
C.calculate()
print("D - int и str")
D = MyClass(["1", 2, "3", 4, "5"])
D.show()
D.calculate()
print("E - str")
E = MyClass(["1","2","3","4","5"])
E.show()
E.calculate()