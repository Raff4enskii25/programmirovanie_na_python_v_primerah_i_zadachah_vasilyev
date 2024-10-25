#9. Напишите программу, в которой создается и построчно заполняется двумерный список (список, элементами которого являются списки). 
#Для заполнения каждой строки (каждого внутреннего списка) используется отдельный дочерний поток.
print("Задание 9")
from threading import *
from time import sleep
mylock=Lock()
l=[['-' for i in range(3)] for i in range(5)]
def assign(k):
    mylock.acquire()
    for i in range(len(l[k])):
        l[k][i] = i+1
        print(l[k][i], end=" ")
        sleep(0.1)
    print(" | ", end=" ")
    mylock.release()
print("Список:")
t=[Thread(target=assign, args=[k]) for k in range(len(l))]
for i in t:
    i.start()
for i in t:
    i.join