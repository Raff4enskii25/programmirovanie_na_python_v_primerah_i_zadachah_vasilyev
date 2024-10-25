number = int(input("Введите число: "))
while number>0:
    digit = number%10
    print("|" + str(digit), end="")
    number//=10
print("|")

number2 = int(input("Введите число: "))
num = number2//2
k = 2
while k<=num:
    if number2 % k==0:
        print("Число не является простым!")
        break
    k+=1
else:
    print("Это простое число")
print("Проверка завершена")

number3 = int(input("Введите число: "))
i = 1
while i<= number3//2:
    if number3%i==0:
        print("Делится на", i)
    i+=1
print("Делится на", number3)
