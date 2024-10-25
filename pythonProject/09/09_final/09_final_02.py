#2. Напишите программу, в которой есть класс с переопределенными методами
#  для приведения к разным типам. В частности, у объекта должны быть поля 
# с целочисленным значением, текстом и действительным числовым значением. 
# При приведении объекта к целочисленному, текстовому или действительному 
# числовому типу возвращается значение соответствующего поля.
print("Задание 2")
class Main:
    def __init__(self, num, txt, fl_num):
        self.number = num
        self.text= txt
        self.fl_number = fl_num
    def __int__(self):
        return self.number
    def __str__(self):
        return self.text
    def __float__(self):
        return self.fl_number
A=Main(123, "Text", 1.2)
print("ToFloat:", float(A))
print("ToInt", int(A))
print("ToStr", str(A))