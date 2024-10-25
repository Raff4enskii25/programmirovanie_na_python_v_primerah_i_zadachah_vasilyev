#6. Напишите программу, в которой описан класс и функция, предназначенная
# для создания списка из объектов. У объектов класса должно быть поле 
#(предназначенное для записи целочисленных значений). При вызове функции 
# аргументом ей передается целое число, определяющее количество объектов в списке.
#  Поля объектов заполняются целыми нечетными числами.
import random
random.seed(2024)
print("Задание 6")
class MyClass:
    def newValue(self, L):
        if(len(L)>0):
            self.value = L[-1].value+2
        else:
            self.value=1
def func(n):
    L = []
    for i in range(n):
        name = chr(random.randint(65,90))
        name = MyClass()
        name.newValue(L)
        L.append(name)
    print("Список:", L)
    return L
n = int(input("Введите целое число: "))
L = func(n)
for i in range(len(L)):
    print(L[i].value)