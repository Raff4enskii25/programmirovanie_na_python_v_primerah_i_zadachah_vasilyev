#1. Напишите программу, в которой описывается класс со следующими 
#характеристиками. У класса есть конструктор, которому (кроме ссылки 
#на объект вызова) передаются два значения. Эти значения присваиваются полям объекта класса.
# В классе должен быть описан метод, при вызове которого отображаются значения полей класса.
# Проверьте функциональность класса, создав на его основе несколько объектов.
print("Задание 1")
class MyClass:
    def __init__(self, val1="Empty", val2="Empty"):
        self.val1 = val1
        self.val2 = val2
    def show(self):
        print("Значение val1:", self.val1)
        print("Значение val2:", self.val2)
A=MyClass()
B=MyClass(666, 777)
A.show()
B.show()