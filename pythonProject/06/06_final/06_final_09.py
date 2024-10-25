#9. Напишите программу, в которой используется функция-генератор, 
#создающая итерируемый объект с названиями месяцев.
print("Задание 9")
def months():
    L=["January", "February", "March", "April", "May", "June", "Jule", "August", "September", "October", "November", "December"]
    for m in L:
        yield m
M = months()
for m in M:
    print(m, end=" ")