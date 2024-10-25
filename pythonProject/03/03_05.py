A=5*[0]
print(A)
B=(1,2,)*3
print(B)
C=B*2
print(C)
D = (B[1]*4,)*2
print(D)
E = ([1]*4,)*3
print(E)

Alpha = [[0]*3]*2
print(Alpha)
Alpha[0][2] = 1
print(Alpha)

Beta = [0]*3
print(Beta)
Beta[2] = 1
print(Beta)

A1, *B1, C1 = 1,2,3,4,5,6
print(A1)
print(B1)
print(C1)