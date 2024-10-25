name = "D:\Documents\PythonTest\pythonProject\\resources\\newtxt.txt"
txt="Python"
mf = open(name, 'w+t', encoding="UTF8")
print("Текст для записи в файл:", txt)
mf.write(txt)
#переходим в начало файла
mf.seek(0)
#первый символ в файле
print(mf.tell(), "=>", mf.read(1))
#переходим в конец файлы
mf.seek(0,2)
#позиция с последним символом в файле
num = mf.tell()-1
#переходим на позицию с последним символом
mf.seek(num)
#последний символ в файле
print(mf.tell(), "=>", mf.read(1))
#обратно в начало файла
mf.seek(0)
#3 первых символа
print("3 первых символа:",mf.read(3))
mf.close()
print("Программа завершила выполнение")