A = {2*k+1 for k in range(5)}
B = {2*k for k in range(5)}
C = {2*k for k in range(8)}
print("A:", A)
print("B", B)
print("C", C)

print("Объединения")
print("A|B=", A | B)
print("B|C=", B|C)
print("A|C=ы", A|C)

print("Пересечения")
print("A&B=", A&B)
print("B&C=", B&C)
print("A&C=", A&C)

print("Разность")
print("A-B=", A-B)
print("B-A=", B-A)
print("A-C=", A-C)
print("B-C=", B-C)

print("Симметрическая разность")
print("A^B=", A^B)
print("B^C=", B^C)
print("A^C=", A^C)
