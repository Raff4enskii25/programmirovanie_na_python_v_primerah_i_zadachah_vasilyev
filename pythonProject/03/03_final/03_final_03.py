#Напишите программу с функцией, которая создает вложенный список.
# Размеры списка указываются аргументами функции. 
# Список заполняется случайными буквами.
import random
print("Задание 3")
rows = int(input("Введите количество строк в списке: "))
columns = int(input("Введите количество столбцов в списке: "))

def showList(r, c):
    newList =[]
    for i in range(r):
        row = []
        for j in range(c):
            row.append(chr(random.randint(65,90+1)))
        newList.append(row)
        print(newList[i])

showList(rows, columns)