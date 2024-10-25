#A=[1,3,5]
#B=A
#B[1] = "Python"
#A[2] = (10,20)
#print(A)
#print(B)

#Поверхностные копии
A = [1,3,[10,20], "Python", [1,2], (3,4)]
B = A[:]
C = A.copy()
D=A
print("Исходные значения")
print("A: "+str(A))
print("B: "+str(B))
print("C: "+str(C))
print("D: "+str(D))

A[0] = [100,200]
A[2][1] = 300
A[3] = "Java"
A[4] = 90
C[4][1] = "C++"
print("После изменений") #— при создании копии не принимается в расчет, что 
                     #некоторые элементы могут быть списками
print("A: "+str(A))
print("B: "+str(B))
print("C: "+str(C))
print("D: "+str(D))