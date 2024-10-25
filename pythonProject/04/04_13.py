from copy import deepcopy
A={"один":1,"два":"двойка","три":[3,4]}

B = dict(A)
C= A.copy()
D=deepcopy(A)
F={"четыре":"four", "пять":"V"}

print("A =", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)

A["два"]=2
A["три"][1]=5

print("A =", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
A.update(F)
print("A после добавления другого словаря =", A)