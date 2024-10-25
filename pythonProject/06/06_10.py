num = 10
L = lambda n: 2*n+1
print("Нечетные числа:")
for k in range(num):
    print(L(k), end=" ")

print("\n Степени двойки")
L = lambda n: 2**n
for k in range(num):
    print(L(k), end=" ")

print("\n Квадраты чисел")
for k in range(num):
    print((lambda x: x*x)(k+1), end =" ")

def calc(x, y):
 return x+y
F=lambda x, y: calc(x, y)
f=calc
calc=lambda x, y: x*y
print("\nF(3,5)", F(3,5))
print("\nf(3,5)", f(3,5))
print("\ncalc(3,5)", calc(3,5))
