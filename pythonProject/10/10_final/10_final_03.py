#3. Напишите программу для решения квадратного уравнения вида (A**2–1)x = B.
# В процессе поиска решения использовать обработку исключительных ситуаций
print("Задание 3")
def calculate(a,b):
    try:
        print(f"Уравнение: ({a}^2 - 1)*x = {b}")
        x = b / ((a**2)-1)
    except TypeError as er:
        er="Аргумент - не число"
        return er
    except ZeroDivisionError as er:
        er = "Решений нет! На ноль делить нельзя!"
        return er
    except Exception as er:
        er="Произошла ошибка: "+str(er.__class__.__name__)
    else: 
        txt="x = "+str(x)
        return txt
print(calculate(1,2))
print(calculate(5,2))
print(calculate(0,1))
print(calculate(10,3))
print(calculate('str', 5))
    