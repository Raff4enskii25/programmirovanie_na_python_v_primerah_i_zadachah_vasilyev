#7. Напишите программу для шифрования и дешифрования текста. Текст 
#шифруется так: каждая буква заменяется на ту, что размещена от нее 
#на две позиции влево. Вторая буква в алфавите заменяется на последнюю. 
#Первая буква в алфавите заменяется на предпоследнюю
txt = input("Введите текст: ")
new_txt = ""
letters_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
letters = dict()
for obj in enumerate(letters_rus):
    letters[obj[1]] = letters_rus[obj[0] - 2]
    letters[obj[1].upper()] = letters[obj[1]].upper()
new_txt = ''.join(letters[letter] if letter in letters else letter for letter in txt)
print("Зашифрованный текст:",new_txt)