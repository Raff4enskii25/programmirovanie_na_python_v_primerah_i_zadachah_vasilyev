#Напишите программу, в которой пользователь вводит целое число, 
#а программа формирует кортеж, который состоит из цифр,
#входящих в это число. Предложите способы создания кортежа, при котором
#цифры, формирующие число, включаются в кортеж в прямом и обратном порядке.
import sys
print("Задание 2")
try:
    num = int(input("Введите число: "))
    yesOrNo = input("Вы хотите сформировать кортеж в обратном порядке? (д/н): ")
    tup = tuple(str(num))
    if yesOrNo =="д":
        tup = tup[::-1]
    print(tup)
  
except:
    print("Вы ввели не целое число!")
    sys.exit(0)