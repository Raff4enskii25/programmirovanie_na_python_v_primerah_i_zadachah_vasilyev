#1
colors = ["Зеленый", "Красный", "Чёрный"]
for i in colors:
    print(len(i))

#2
n = 15
a,b=1,1
print(a,b, end=" ")
for i in range(n-2):
    a,b = b, a+b
    print(b, end=" ")

#3
text = input("\nВведите текст:" )
symbs = ["а", "я", "п"]
print("Ищем буквы:", symbs)
for i in symbs:
    if i in text:
        print("Такая буква есть в тексте:", i)
        break
    else:
        print("Такой буквы нет в тексте:", i)
else:
    print("Заданных букв в тексте нет:")
#test