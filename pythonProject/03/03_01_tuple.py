a=1, 2, "три", 4, "V"
print(a, type(a))
print(len(a))
print(a[3])
print(a[0:2+1])
print(a[:])
print(a[2], len(a[2]))

print("Новый кортеж")
b=tuple(i+1 for i in range(5))
print(b)
for i in range(len(b)):
    print(b[i])

print("Кортеж С")
c = tuple([k+1 for k in range(2)] for i in range(10))
print(c)
print(c[2][1])

print("Кортеж D - степень двойки")
d=tuple(2**k for k in range(1, 10+1))
print(d)

