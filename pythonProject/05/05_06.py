A = "Муха - это маленькая птичка"
print(A)
print(A.find("а"))
print(A.index("а"))
print(A.rfind("а"))
print(A.rindex("а"))
print(A.count("а"))
print(A.endswith("птичка"))
print(A.endswith("гусеница"))
print(A.startswith("Муха"))
print(A.strip("Мука")) #удалить в начале и конце
print(A.rstrip("Мука")) #удалить только в конце строки
print(A.lstrip("Мука")) #удалить только в начале строки
print(A.replace("Муха", "Пингвин"))

symb = input("Введите букву: ")
num = A.find(symb)
L = []
while num !=-1:
    L.append(num)
    num = A.find(symb, num+1)
if len(L) == 0:
    print("Такой буквы в тексте нет!")
else:
    print(f"Позиции буквы {symb} в тексте {L}")