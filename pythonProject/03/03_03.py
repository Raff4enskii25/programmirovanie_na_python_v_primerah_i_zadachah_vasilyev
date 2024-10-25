A=(10,20,30)
print("A:"+str(A))
B=("Python", (2,3))
print("B:"+str(B))

C=A+B
print("C:"+str(C))
C+=(200,)
print("C:"+str(C))
C= C[:2] + (8,9) + C[2:] #Вставка элементов в кортеж
print("C:"+str(C))
C = C[:2] + (7,) + C[3:] #"присваивание" значения элементу
print("C:"+str(C))
C = C[:1] + C[2:] #Удаление элемента из кортежа 
print("C:" +str(C))
C = C[1:]
print("C:"+str(C))
C = (200,) + C
print("C:"+str(C))
C=("A", "B") + C[2:]
print("C:"+str(C))