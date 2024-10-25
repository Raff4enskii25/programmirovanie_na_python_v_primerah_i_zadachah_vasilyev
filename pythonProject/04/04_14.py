A = dict(zip([1,2,3],['K','L','M'])) #создается словарь на основе двух списков
B = dict.fromkeys([10,20,30], 'Z') #в данном словаре все элементы будут иметь одно значение

print("A =", A)
print("B =", B)

print("Сравнение словарей:" )
print("A==B", A==B)
print("A!=B", A!=B)

A.update(B)
print("Объединение словарей")
print("A = ", A)

print((20, 'Z') in A.items())
print(20 in A)
print('Z' in A)
print(5 not in A)

A.clear()
print("Словарь после очистки:")
print("A = ", A)