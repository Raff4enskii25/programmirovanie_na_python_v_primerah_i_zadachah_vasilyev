#3. Напишите программу, в которой пользователь вводит текстовое значение
#  и для этого текстового значения определяются гласные буквы, 
#представленные во введенном тексте.

print("Задание 3")

text = input("Введите текст: ")

vowelLetters = ['а', 'у', 'ы', 'я', 'и', 'е', 'ё', 'ю', 'о', 'э']
A = set()

for i in text:
    if i in vowelLetters:
        A.add(i)
print("Гласные буквы в введенном тексте: ", A)