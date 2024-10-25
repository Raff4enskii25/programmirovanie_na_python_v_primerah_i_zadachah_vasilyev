#1
num = int(input("Введите число: "))
res = "четное" if num%2==0 else "нечетное"
print("Это "+res+" число")

#2
val = eval(input("Введите число: "))
a,b = (val[0], val[-1]) if type(val)==str else (val,type(val))
print(a)
print(b)