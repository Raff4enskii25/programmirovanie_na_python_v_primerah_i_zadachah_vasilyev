#4. Напишите программу, в которой пользователь вводит целое число, 
#а программа переводит его в восьмеричную систему, меняет порядок 
#следования цифр в представлении числа и результат отображает в области вывода.

print("Задание 4")
num = int(input("Введите целое число: "))
octNum = oct(num); octNum = octNum[2:]
print(f"Число {num} в восьмеричной системе: {octNum}")
octNum = octNum[::-1]
print(f"Новое число: {octNum}")
