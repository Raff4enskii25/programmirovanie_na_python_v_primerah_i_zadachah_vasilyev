#4. Напишите программу для вычисления множества чисел (в пределах 
#первой полусотни), которые делятся или на 3, или на 4, но при этом 
#не делятся одновременно на 3 и 4.

print("Задание 4")
A = set(i for i in range(1,50+1) if (i%3 ==0 and i%4 !=0) or (i%4==0 and i%3 !=0))
print("A =", A)
        