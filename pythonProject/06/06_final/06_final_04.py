#4. Напишите программу, в которой создается функция с одним текстовым аргументом
#  и произвольным количеством целочисленных аргументов. Результатом является текст, сформированный из букв первого 
#текстового аргумента. Целочисленные аргументы определяют индексы букв, которые нужно включить в текст-результат.

print("Задание 4")
def myNewText(t, *n):
    newT = ""
    for i in n:
        if i<len(t):
            newT += t[i].strip(" .,''")
        else:
            print(f"Элемента с индексом {i} нет в тексте!")
    return newT

print("Результат:", myNewText("Привет, я Андрей!", 0,1,5,6,7,8,9,15,25))