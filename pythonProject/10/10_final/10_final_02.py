#2. Напишите программу, в которой пользователю предлагается ввести 
#два целочисленных значения. Эти значения определяют границы диапазона,
# в котором отображаются целые числа. Использовать обработку исключений.
print("Задание 2")
def display():
    num1 = input("Введите целое число 1: ")
    num2 = input("Введите целое число 2: ")
    try:
        for i in range(eval(num1), eval(num2)+1):
           print(i, end=" ")
    except TypeError:
        print("Вы ввели не целое число!")
    except Exception as er:
        print(f"Произошла ошибка!", {er})
display()