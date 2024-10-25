#5. Напишите программу, в которой пользователь вводит два текстовых 
#значения, и на их основе создается новый текст. В этот новый текст поочередно
#включаются буквы из текстов, введенных пользователем. 
#Когда один из текстов заканчивается, в качестве символов из этого текста 
#используется «звездочка» *.
txt1 = input('Введите текст 1: ')
txt2 = input('Введите текст 2: ')
new_txt = ""
num = 0
while (num < len(txt1)) and (num<len(txt2)):
    new_txt += txt1[num]
    new_txt += txt2[num]
    num +=1
if num==len(txt1):
   for i in range(num, len(txt2)):
        new_txt+= "*"
        new_txt += txt2[i]
if num==len(txt2):
    for i in range(num, len(txt1)):
        new_txt += txt1[i]
        new_txt+= "*"
print("Новый текст:", new_txt)