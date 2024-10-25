#8. Напишите программу, в которой шифруется и дешифруется введенный пользователем текст.
#  При шифровании каждая буква заменяется на следующую (а последняя — на первую), но только эта операция 
#отдельно выполняется для гласных букв и для согласных. Для этого 
#нужно сформировать список гласных и согласных букв и шифрование 
#и дешифрование выполнять на основе этих списков.
vowelLetters = "аеёиоуыэюя"
letters = "бвгджзйклмнпрстфхцчшщ"
L = dict()
for i in vowelLetters:
    L[i] = vowelLetters[vowelLetters.index(i)+1] if vowelLetters.index(i) != len(vowelLetters)-1 else vowelLetters[0]
    L[i.upper()] = vowelLetters[vowelLetters.index(i)+1].upper() if vowelLetters.index(i) != len(vowelLetters)-1 else vowelLetters[0].upper()
for i in letters:
    L[i] = letters[letters.index(i)+1] if letters.index(i) != len(letters)-1 else letters[0]
    L[i.upper() ]= letters[letters.index(i)+1].upper() if letters.index(i) != len(letters)-1 else letters[0].upper() 

txt = input("Введите текст: ")
new_txt=""
for i in txt:
    if i in L.keys():
        new_txt += L[i]
print("Зашифрованный текст:", new_txt)

yN = input("Вы хотите дешифровать текст? (д/н) ")
match(yN):
    case "д":
        new_txt1 = ""
        L_res= {v: k for k, v in L.items()}
        for i in new_txt:
            if i in L_res.keys():
                new_txt1 += L_res[i]
        print("Дешифрованный текст:", new_txt1)
    case "н":
        pass

