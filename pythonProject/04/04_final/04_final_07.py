#7. Напишите программу, которая выполняется следующим образом. 
#Пользователь вводит текст. На основе этого текста создается словарь. 
#Ключами словаря служат символы из текста, а значениями элементов 
#словаря являются количества вхождений соответствующих символов 
#в текст. Например, если пользователь вводит текст "ABBCAB", то словарь
#  будет состоять из трех элементов с ключами "A", "B" и "C", а значения 
# элементов соответственно равны 2 (в тексте 2 буквы "A"), 3
#(в тексте 3 буквы "B") и 1 (в тексте 1 буква "C").

print("Задание 7")
text = input("Введите текст: ")
A = [i for i in text]
B = {}
for i in A:
    B[i] = A.count(i)
print("B:", B)
    