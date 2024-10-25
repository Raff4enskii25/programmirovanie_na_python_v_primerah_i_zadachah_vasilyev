import random
random.seed(2024)
A=[1,2,3,4,5,6,7,8,9]
B={'A','B','C','D'}
C="Python"
D={1:"Один", 2:'Два', 3:'Три', 4:'Четыре'}

def show(L, symb):
    if(type(L) != dict):
        for i in L:
            print(symb, i, sep="", end="")
        print(symb)
    else:
        for i in L.values():
            print(symb, i, sep="", end="")
        print(symb)

show(A, "|")
show(B, "/")
show(C, "*")
show(D, '#')

def get_nums(n, state):
    if type(n)!=int:
        return []
    if state:
        L=list(2*(k+1) for k in range(n))
    else:
        L=list(2*k+1 for k in range(n))
    return L

print(get_nums(10, True))
print(get_nums(8, False))
print(get_nums(12.5, True))

def get_symbs(n):
    if n>10 or n<1:
        num=10
    else:
        num=n
    S=set()
    Nmin=ord("A")
    Nmax=ord("Z")
    while len(S)<num:
        S.add(chr(random.randint(Nmin, Nmax)))
    return S

print(get_symbs(7))
print(get_symbs(-5))
print(get_symbs(15))