#3. Напишите программу, в которой для объектов класса определена операция сложения.
# У каждого объекта есть поле-список, и при сложении объектов получается новый объект
#  того же класса. Его поле-список получается объединением полей-списков исходных объектов.
print("Задание 3")
class Main:
    def __init__(self, val):
        if type(val)==list: self.value = val
        else: print("Значение не является списком!")
    def __add__(self, obj):
        self.result = self.value + obj.value
        return self.result
A=Main([1,2,3,4,5])
B=Main([10,20,30,40])
print("A+B =", A+B)
print("B+A =", B+A)
C=Main("Text")