#6. Напишите программу с функцией, которая аргументами получает ссылку на функцию (например, f()) и целое число (например, n). 
#Результатом является функция, которая вычисляет результат путем n-кратного применения функции f().

print("Задание 6")
def myFunc(f, n):
    def newFunc():
        for k in range(n):
            f(k)
    return newFunc()
    
def func(n):
    print(f"Это текст повторяется {n+1} раз")

myFunc(func, 5)