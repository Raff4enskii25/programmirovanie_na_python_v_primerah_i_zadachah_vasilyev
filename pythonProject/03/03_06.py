import random

def show(A):
    for a in A:
        for s in a:
            print(s, end=" ")
        print()

def rands(m,n):
    res=[[random.randint(0,9) for i in range(n)] for j in range(m)]
    return res

def symbs(m,n):
    val='A'
    res=[['' for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = val
            val = chr(ord(val)+1)
    return res

A=[[(j+1)*10+i+1 for i in range(5)] for j in range(3)]
print("Список А:")
show(A)

random.seed(2019)
B=rands(3,4)
print("Список B:")
show(B)

C = symbs(3,5)
print("Список C:")
show(C)

size=[3,5,4,6]
D=[['*' for k in range(s)] for s in size]
print("Список D:")
show(D)