A=[0,1,2, [3,4], (5,6), 7, "Java"]
print(A)
A.append("Python")
print(A)
for i in range(5):
    A.append(i)
print(A)
A.append([6,5,4,3])
print(A)
A.extend([12, 14, 16])
print(A)
A.pop(1)
print(A)
A.remove(2)
print(A)
A.insert(5, "Hello!")
print(A)
for k in range(len(A)-1):
    A.append(A.pop(-k-2))
print(A)

B=[]
for k in range(len(A)//2):
    B.append(A[k])
print("B:",B)

C=[9,10]
for i in range(10-len(C)):
    C.insert(0,C[0]-1)
print("C:",C)

F =[1,1]
for i in range(10):
    F.append(F[-1]+F[-2])
print(F)
F.reverse()
print(F)
