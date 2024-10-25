#1. Напишите программу, в которой создается функция с двумя аргументами, являющимися числовыми списками. Результатом является число, 
#равное сумме попарных произведений элементов списков. Если в одном 
#из списков элементов меньше, чем в другом, то недостающие элементы 
#получают путем циклического повторения содержимого списка.
print("Задание 1")
def listsSum(l, j):
    newL = []
    numL = 0
    numJ = 0
    if len(l)>len(j):
        while numL<len(l):
            newL.append(l[numL] + j[numJ])
            numL +=1
            numJ+=1
            if numJ==len(j):
                numJ=0
    elif len(j)>len(l):
        while numJ<len(j):
            newL.append(j[numJ] + l[numL])
            numL +=1
            numJ+=1
            if numL==len(l):
                numL=0
    else:
        for i in range(len(l)):
            newL.append(l[i] + j[i])
    return newL

print("l>j:", listsSum([1,2,3,4,5], [1,2,3]))
print("j>l:", listsSum([1,2,3], [1,2,3,4,5]))
print("l=j:", listsSum([1,2,3],[1,2,3]))