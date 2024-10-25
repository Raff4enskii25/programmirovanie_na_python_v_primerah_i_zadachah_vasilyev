mf =  open("D:\Documents\PythonTest\pythonProject\\resources\poetry.txt", encoding='UTF8')
k=1
print("Построчное считывание файла:")
for L in mf:
    print('['+str(k)+']', L, end="")
    k+=1
mf.close()
print("\nФайл закрыт")

k=1
with open("D:\Documents\PythonTest\pythonProject\\resources\poetry.txt", encoding='UTF8') as fm:
    for L in fm:
        print('['+str(k)+']', L, end="")
        k+=1
print("\nФайл закрыт")

mf1=  open("D:\Documents\PythonTest\pythonProject\\resources\poetry.txt", encoding='UTF8')
k=1
L = mf1.readline()
while L!="":
    print('['+str(k)+']', end="")
    for s in L:
        if s==" ":
            s='_'
        print(s, end="")
    k+=1
    L = mf1.readline()
mf1.close()
print("\nФайл закрыт")

mf2 =  open("D:\Documents\PythonTest\pythonProject\\resources\poetry.txt", encoding='UTF8')
L1 =mf2.readline(); print(L1)
L1 =mf2.readline(); print(L1)


