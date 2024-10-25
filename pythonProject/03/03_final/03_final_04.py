#. Напишите программу, в которой есть функция для заполнения вложенного списка. 
# Список заполняется натуральными числами «змейкой»: сначала заполняется первая строка, 
# затем последний столбец (сверху вниз), последняя строка (справа налево), первый столбец (снизу вверх),
#  вторая строка (слева направо), и так далее.
print("Задание 4")
row = 3
columns = 3

def showList(r,c):
    newList=[[0*i for i in range(r)] for j in range(c)]
    for i in range(r):
        newList[0][i] = i
    
    for i in range(c):
        for j in range(r):
            newList[i][r-1] = newList[0][r-1]+i
    
    for i in range(r):
        newList[c-1][-i-1] = newList[c-1][r-1]+i
    
    for i in range(c-1):
        for j in range(r):
            newList[-i-1][0] = newList[r-1][0] + i
    
    for i in range(r-1):
        newList[1][i] = newList[1][0]+i

    
    for i in range(c):
        print(newList[i])
            
showList(row, columns)