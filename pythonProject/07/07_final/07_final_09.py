#9. Напишите программу, в которой пользователь вводит имя текстового 
#файла, а программа отображает содержимое этого файла, а также создает 
#копию этого файла с пронумерованными строками.
print("Задание 9")
fileName = input("Введите название текстового файла: ")
file = open(f"D:\Documents\PythonTest\pythonProject\\resources\\{fileName}.txt", encoding="UTF8")
filecopy = open(f"D:\Documents\PythonTest\pythonProject\\resources\\{fileName}_copy.txt", 'w+t', encoding="UTF8")
line_number = 1
lines = file.readlines()
for line in lines:
    filecopy.write(f"[{line_number}] {line}")
    line_number += 1
filecopy.close()
file.close()
print("Копия файла создана")