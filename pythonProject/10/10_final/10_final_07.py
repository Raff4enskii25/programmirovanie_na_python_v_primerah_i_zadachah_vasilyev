#7. Напишите программу, в которой с использованием двух дочерних потоков заполняется список. 
#Первый поток присваивает буквенные значения элементам с четными индексами. 
#Второй поток присваивает числовые значения элементам с нечетными индексами.
print("Задание 7")
from threading import *
myevent=Event()
myevent.set()
l=['-' for i in range(10)]
def assign(n):
    myevent.wait()
    myevent.clear()
    if n<len(l):
        if n%2==0: l[n]=chr(n+65) 
        else: l[n] = n+1   
        myevent.set()
        n+=1
        if n<len(l): assign(n)
        else: return l
t=Thread(target=assign, args=[0])
f=Thread(target=assign, args=[1])
t.start()
f.start()
if t.is_alive():t.join()
if f.is_alive(): f.join()
print("Список:", l)
