import sys

#1
print("Уравнение ax=b")
a,b = eval(input("Введите через запятую два числа (пр. 2,4): "))

if(type(a)!=int and type(a)!=float) or (type(b)!=int and type(b)!=float):
    print("Числа введены!")
    sys.exit(0)
elif(a!=0):
        print("Решение: x =",str(b/a))
elif(b!=0):
    print("Решений нет!")
else:
    print("Решение - любое число!")
print("Поиск значения завершен.")

#2
res = "Число "
text = input("Введите число: ")
text = text.lower() #перевод в нижний регистр
#для верхнего региста text.upper()
if(text == "один" or text=="единица"):
    res +="1"
    print(res)
else:
     print("Не входит в диапазон")