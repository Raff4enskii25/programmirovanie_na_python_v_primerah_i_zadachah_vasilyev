#4. Напишите программу, в которой для объектов предусмотрены операции
#  сложения с числом, вычитания числа и вычитания из числа, а также 
#умножения на число и деления на число. У объекта должно быть поле 
#с числовым значением, и при выполнении указанных операций они должны 
# выполняться с полем объекта.
print("Задание 4")
class Main:
    def __init__(self,num):
        if type(num)==int: self.number=num
        else: print("Объект не является числом!")
    def __add__(self, num):
        return self.number+num
    def __sub__(self,num):
        return self.number-num
    def __rsub__(self,num):
        return num-self.number
    def __mul__(self, num):
        return self.number*num
    def __truediv__(self,num):
        return self.number/num
    def __call__(self):
        return self.number
A=Main(25)
print("A =", A())
print("A+5=",A+5)
print("A-5=", A-5)
print("10-A=",10-A)
print("A*2=",A*2)
print("A/5=",int(A/5))