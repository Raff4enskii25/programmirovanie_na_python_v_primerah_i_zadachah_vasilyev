print("Операции со списками")
A=[10, 20, 30]
print("A:"+str(A))
B =["Python", [2,3]]
print("B:"+str(B))
C=A+B
print("C:"+str(C))

C[2:3] = []
print(C)
C[2:2] = [1,2]
print(C)
C[:3] = ["A", "B"]
print(C)
C[2] = [7]
print(C)
C+=[200] #добавление в конец списка
print(C)
C = [200]+C #добавление в начало списка
print(C)