#10. Напишите программу, в которой используется функция-генератор,
# создающая итерируемый объект со степенями двойки. Количество 
#элементов определяется аргументом функции-генератора

def degrees(n):
    for k in range(n):
        yield 2**(k+1)

num = int(input("Введите число: "))

print("Степени двойки:", end=" ", sep=" ")
for i in degrees(num):
    print(i, end=" ")