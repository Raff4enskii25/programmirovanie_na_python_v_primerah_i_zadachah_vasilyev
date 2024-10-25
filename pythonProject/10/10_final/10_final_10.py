#10. Напишите программу, в которой создается три дочерних потока. 
#В первом потоке вычисляется факториал числа (произведение натуральных чисел).
#Во втором потоке вычисляется двойной факториал числа (произведение чисел через одно).
#  В третьем потоке вычисляется число из последовательности Фибоначчи (первые два числа равны единице, 
#а каждое следующее равно сумме двух предыдущих).
print("Задание 10")
from threading import *
from time import sleep

def fac(n):
    print("Первый поток:")
    num=1
    if n!=0:
        for i in range(1,n+1):
            num*=i
    sleep(1)
    print(f"Факториал {n} = {num}")

def double_fac(n):
    print("Второй поток:")
    num=1
    if n!=0:
        if n%2==0:
            for i in range(2,n+1):
                if i%2==0:
                    num*=i
                    i+=1
                else: continue
        else:
            for i in range(1,n+1):
                if i%2!=0:
                    num*=i
                    i+=1
                else:continue
    sleep(1)
    print(f"Двойной факториал: числа {n} = {num}")

def fibonacci(n):
    print("Третий поток:")
    a,b=1,1
    l=[a,b]
    for i in range(5):
        a,b=b,a+b
        l.append(b)
    sleep(1)
    print(f"Вычисление последовательности Фибоначчи:", end=" ")
    for i in l:
        print(i, end=" ")
        sleep(0.1)

F=Thread(target=fac, args=[10])
S=Thread(target=double_fac, args=[10])
T=Thread(target=fibonacci, args=[10])

L = [F,S,T]
for i in L:
    i.start()
    i.join()
