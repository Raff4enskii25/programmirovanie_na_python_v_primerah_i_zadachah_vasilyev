A={"Начальный":1,"Средний":2,"Последний":3}
B = dict(A)
C = A.copy()
D ={k: v*10 for k, v in A.items()}

print("Созданы множества:")
print("A =", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)

for k in A:
    A[k]*=100
print()
print("После изменения оригинала:")
print("A =", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
#items() возвращает кортеж из ключа и значения, 
# а keys() и values() либо ключи, либо значения

