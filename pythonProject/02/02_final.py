import sys
import random
#print("Задание 1")
#num = input("Введите целое число: ")
#res=[k*0 for k in range(10)]
#for i in num:
#    number = eval(i)
#    res[number]+=1
#for i in range(9):
#    if res[i]>0:
#        print("Количество цифр "+str(i)+" в числе "+str(num)+" равно "+ str(res[i]))

#print("Задание 2")
#num = input("Введите целое число: ")
#for i in num:
#    number = eval(i)
#    if(number<9): number -=9
#    print(abs(number), end="")

#print("Задание 3")
#num = ""
#nums=[i*random.randint(1,9) for i in range(1,9)]
#print(nums)
#for i in range(len(nums)):
#    num+=str(nums[i])
#print(int(num))

#print("Задание 4")
#list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#count = 0
#if(len(list1) == len(list2)):
#    for i in range(len(list1)):
#        if(list1[i] == list2[i]): 
#            count+=1
#            if count==len(list1): print("Списки равны!")
#        else:
#            print("Списки не равны!")
#            break
#else:
#    print("Списки не равны!")

#print("Задание 5")
#maxSum = int(input("Введите максимальную границу суммы: "))
#exceptions = input("Введите список исключающих чисел (пр. 1, 5, 9):")
#ex = "["+exceptions+"]"
#nums=[i for i in range(maxSum+1)]
#print("Сумма вашего списка:", sum(nums)-sum(eval(ex)))

#print("Задание 6")
#try:
#    a = eval(input("Введите 1 сторону треугольника: "))
#    b = eval(input("Введите 2 сторону треугольника: "))
#    c = eval(input("Введите 3 сторону треугольника: "))
#    if(a+b>c and b+c>a and a+c>b):
#        print("Треугольник существует!")
#    else:
#        print("Треугольник не существует!")
#except:
#    print("Числовые значения введены неверно")
#    sys.exit(0)

#print("Задание 7")
#try:
#    i = eval(input("Введите фиксированное число для последовательности: "))
#    num1 = eval(input("Введите число 1: "))
#    num2 = eval(input("Введите число 2: "))
#    num3 = eval(input("Введите число 3: "))
#    if (num1+i == num2) and (num2+i == num3):
#        print("Числа являются тремя последовательными элементами!")
#    else:
#       print("Числа не являются тремя последовательными элементами!")
#except:
#    print("Числовые значения введены неверно!")
#    sys.exit(0)

#print("Задание 8")
#try:
#    num = int(input("Введите число от 1 до 7: "))
#    match num:
#        case 1: print("День недели - понедельник")
#        case 2: print("День недели - вторник")
#        case 3: print("День недели - среда")
#        case 4: print("День недели - четверг")
#        case 5: print("День недели - пятница")
#        case 6: print("День недели - суббота")
#        case 7: print("День недели - воскресенье")
#
#        case _: print("Вы ввели неверное число!")
#except:
#    print("Числовое значение введено неверно!")
#    sys.exit(0)

#print("Задание 9")
#try:
#    num1 = eval(input("Введите 1 число: "))
#    num2 = eval(input("Введите 2 число: "))
#    print(num1) if num1>num2 else print(num2)

#except SyntaxError:
#    print("Невозможно вычислить значение!")
#except NameError:
#    print("Введено не число!")
#except ZeroDivisionError:
#    print("Невозможно разделить число на 0!")
#except:
#    print("Что-то пошло не так!")
#    sys.exit(0)

print("Задание 10")
print("Уравнение Ax = B - A - 1")
try:
    a = eval(input("Введите число A: "))
    b = eval(input("Введите число B: "))
    if (a!=0):
        x = (b - a - 1)/a
        print("X = "+str(x))
    elif (a==0 and b==1):
        print("Решение - любое число!")
    else:
        print("Уравнение не имеет решения.")

except SyntaxError:
    print("Невозможно вычислить значение!")
except NameError:
    print("Введено не число!")
except ZeroDivisionError:
    print("Невозможно разделить число на 0!")
except:
    print("Что-то пошло не так!")
    sys.exit(0)