#6. Напишите программу, в которой с использованием потоков, 
# вычисляется сумма квадратов натуральных чисел. Сумма вычисляется 
# определенное время, по аналогии с примером из листинга 10.15.
print("Задание 6")
from threading import *
from time import sleep
s=0
num=int(input("Введите число секунд: "))
def mysum():
    global s
    k=1
    while myevent.is_set():
        s+=k**2
        print(f"{k**2}", end=" ")
        k+=1
        sleep(0.5)
print("Сумма квадратов натуральных чисел:")
myevent = Event()
t=Thread(target=mysum)
myevent.set()
t.start()
sleep(num)
myevent.clear()
if t.is_alive():
    t.join()
print("\nСумма:", s)
