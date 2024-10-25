#5. Напишите программу, в которой создается вложенный список из случайных чисел. В матрице, которая реализуется данным вложенным 
#списком, удаляется строка и столбец. Номер строки и номер столбца, 
#которые нужно удалить, вводятся пользователем.
import random
random.seed(2024)
print("Задание 5")

def removeRowAndColumn(A, r,c):
    A.pop(r-1) #Удалить строку
    for i in range(len(A)):
        A[i].pop(c-1) #удалить столбец
    
    print("Список после удалений")
    for i in range(len(A)):
        print(nums[i])

nums=[[random.randint(0, 9) for i in range(5)] for i in range(5)]
print("Список до удалений:")
for i in range(len(nums)):
    print(nums[i])
row = int(input("Введите строку для удаления: "))
column = int(input("Введите столбец для удаления: "))

removeRowAndColumn(nums, row, column)
