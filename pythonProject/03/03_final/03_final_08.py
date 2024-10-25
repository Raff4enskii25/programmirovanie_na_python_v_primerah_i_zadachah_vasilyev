#. Напишите программу, в которой создается числовой список. 
#Список заполняется случайными числами. 
# Затем элементы с четными индексами сортируются в порядке возрастания,
#  а элементы с нечетными индексами сортируются в порядке убывания.
import random
random.seed(666)
print("Задание 8")

l=[random.randint(0, 9) for i in range(9)]
print("Начальный список:"+str(l))
evenL = []; oddL = []
for i in range(len(l)):
    if i%2==0: evenL.append(l[i])
    else: oddL.append(l[i])
evenL.sort()
oddL.sort(reverse=True)
l = evenL + oddL
print("Финальный список:"+ str(l))