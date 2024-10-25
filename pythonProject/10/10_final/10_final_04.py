#4. Напишите программу, в которой решается уравнение вида A(A – 1) x =sin(A), 
# причем при значении A = 0 должно вычисляться решение x = –1.
import math
print("Задание 4")
def calculate(a):
    print(f"Уравнение: {a}({a} - 1)x = sin({a})")
    try:
        if a!=0:
            x = math.sin(a) / (a*(a-1))
        else:
            x=-1
    except TypeError as er:
        print('Аргумент - не число!')
    except ZeroDivisionError as er:
        print('Нет решений! На ноль делить нельзя!')
    except Exception as er:
        print('Произошла ошибка: '+str(er.__class__.__name__))
    else:
        print('х = '+str(x))
calculate(1)
calculate('hi')
calculate(0)
calculate(5)
calculate(3)