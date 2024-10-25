#Напишите программу, в которой создается два списка одинакового размера. 
# На основе этих списков поочередной вставкой элементов 
#из первого и второго списка формируется новый список.
import random
random.seed(228)
print("Задание 10")
l1=[random.randint(0,9) for i in range(10)]
print("1 список:", l1)
l2 = ['c++', 'java', 'python', 'golang', 'c#', 'c', 'Kotlin', 'Pascal', '1c', 'JavaScript']
print("2 список:", l2)
l3=[]
for i in range(len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])
print("3 список:", l3)