#2. Напишите программу, в которой описан класс со следующими свойствами. В классе описан конструктор, 
#которому в качестве аргументов (помимо первой ссылки на создаваемый объект) передаются текст и целое число, 
# причем в произвольном порядке. Число и текст присваиваются как значения определенным полям.
#  Если переданы два текстовых значения, то создается только текстовое поле со значением, 
# получающимся объединением значений аргументов. Если аргументами переданы два числовых поля, 
# то у объекта будет только поле с целочисленным значением, равным сумме значений аргументов. В иных случаях поля 
#для объекта не создаются. Создать на основе класса объекты и проверить функциональность кода.
print("Задание 2")
class MyClass:
    def __init__(self, txt=None, num=None):
        #Если оба аргумента строки
        if type(txt)==str and type(num)==str:
            self.text = txt+num
        #Если оба аргумента числа
        elif (type(num)==int and type(txt)==int) or (type(num)==float and type(txt)==float):
            self.value = num+txt
        #Если аргумент txt - строка, а num - число
        elif type(txt)==str and (type(num)==int or type(num)==float):
            self.text = txt
            self.value = num
        #Если аргумент txt - число, а num - строка
        elif type(txt)==int and type(num)==str:
            self.text = num
            self.value = txt
        #Если не подходит ни под один критерий
        else:
            print("Значения не соответствуют требованиям!")
    
    def show(self):
        if hasattr(self, "text"):
            print("Значение Text:", self.text)
        if hasattr(self, "value"):
            print("Значение Value:", self.value)

print("Объект А: текст, цифра")
A=MyClass("Текст", 123)
A.show()
print("Объект В: цифра, текст")
B=MyClass(321, "Text")
B.show()
print("Объект С: цифра, цифра")
C=MyClass(666,777)
C.show()
print("Объект D: текст, текст")
D=MyClass("Text","Текст")
D.show()
print("Объект Е: нету одного аргумента")
E=MyClass("Text")
E.show()