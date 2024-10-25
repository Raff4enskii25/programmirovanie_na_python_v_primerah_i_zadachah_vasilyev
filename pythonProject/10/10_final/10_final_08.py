#8. Напишите программу, в которой создается объект с двумя списками. 
#Списки заполняются значениями с помощью двух дочерних потоков: 
#один список заполняется символами, а второй список заполняется числами.
print("Задание 8")
from threading import Thread
class Main:
    def __init__(self):
        self.values=[]
        self.symbols=[]
A=Main()
def assign(obj, *n):
    for i in n:
        if type(i)==int or type(i)==float:
            obj.values.append(i)
        elif type(i)==str:
            obj.symbols.append(i)
N=Thread(target=assign, args=[A, 1, 2.0, 3, 4.0, 5, 6.0])
F=Thread(target=assign, args=[A, 'один', 'два','три','четыре','пять'])
N.start()
F.start()
N.join()
F.join()
print("Список с числами:", A.values)
print("Список с символами:", A.symbols)