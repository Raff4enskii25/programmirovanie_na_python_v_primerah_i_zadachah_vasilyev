txt = input("Введите текст: ")
txt = txt.lower()
sp = txt.split()
print("Слова:", sp)
symb_sum = 0
for i in range(len(sp)):
    w=sp[i].strip(".,:;-!?'")
    if w!=0:
        symb_sum += len(w)
print("Кол-во слов:", len(sp))
print("Кол-во символов:", symb_sum)
print("Средняя длина слова:", symb_sum/len(sp)) 