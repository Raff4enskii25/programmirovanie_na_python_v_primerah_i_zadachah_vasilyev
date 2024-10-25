#Напишите программу, в которой создается числовой список. 
# Список заполняется случайными числами. 
# Затем между каждой парой элементов этого списка вставляется новый элемент, 
# равный сумме значений соседних элементов.
from copy import deepcopy 
import random
random.seed(777)
print("Задание 9")

l=[random.randint(0, 9) for i in range(10)]
newL = []
print("Начальный список:"+str(l))
for i in range(len(l)-1):
    newL.append(l[i])
    newEl = l[i]+l[i+1]
    newL.append("["+str(newEl)+"]")
newL.append(l[-1])
l.clear; l = deepcopy(newL)
print("Конечный список:"+str(l))
