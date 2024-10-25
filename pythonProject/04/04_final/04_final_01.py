#1. Напишите программу, в которой генерируется 15 случайных целых 
# чисел: 5 чисел попадают в диапазон значений от 1 до 10 и 10 чисел 
# попадают в диапазон от 10 до 30.

import random
random.seed(2024)
count = 15
A =set()
while len(A)< count:
    if len(A)<5:
         A.add(random.randint(1,10))
    else:
        A.add(random.randint(10,30))
print("A = ", A)