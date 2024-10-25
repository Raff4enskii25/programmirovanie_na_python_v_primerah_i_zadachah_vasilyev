A=[i for i in range(10)]
print(A)
print(A[::2])
print(A[::-2])

B=tuple(i for i in range(21) if i%3!=0)
print(B)

C=[i for i in range(15) if i%5==0]
print(C)

D = [0 if i==0 or i==1 else i**2 for i in range(13) if not i in(2,3,4,5,6)]
print(D)

E = [2*i if i in(1,2,3,4) else i**3 for i in range(10)]
print(E)

F = tuple(2**(i//2) if i%2==0 else 3**(i//2) for i in range(2, 14))
print(F)

Alpha = A[::-1]
print(Alpha)

Bravo = B[::2]
print(Bravo)

G =tuple(i for i in range(25) if i%2==0)
print(G)

Charlie = 5*[A]
print(Charlie)