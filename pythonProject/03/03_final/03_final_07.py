#7. Напишите программу с функцией, которая для списка, переданного 
#аргументом, возвращает список из двух элементов: значение наибольшего элемента в списке и индекс этого элемента в списке (если таких 
#элементов несколько, то индекс первого из таких элементов).

import random
random.seed(2024)
print("Задание 7")

l=[random.randint(0, 9) for i in range(9)]
print(l)

def showList(A):
    maxArg = max(A)
    maxArgIndex = A.index(maxArg)
    newL = [maxArg, maxArgIndex]
    return newL

print(str(showList(l)))