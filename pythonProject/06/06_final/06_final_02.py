#2. Напишите программу с функцией, аргументом которой передается 
#числовой список, а результатом является еще один список, в который 
#включены только нечетные числа из списка-аргумента

print("Задание 2")
def newList(l):
    newL = []
    for i in l:
        if i%2!=0:
            newL.append(i)
    return newL

print("Нечетный список:", newList([1,2,3,4,5,6,7,8,9]))