A = {1,2,3,4}
B = {1,2,3,4,5,6,7,8}
C = {'a','b','c', 'd', 'f'}
D = {2,3,4,5}

print(A.issubset(B)) #является ли А подмножеством ВC
print(B.issuperset(A)) #является ли А подмножеством В
print(B.issubset(A))
print(A.issuperset(B))

print(A.isdisjoint(B)) #есть ли общие элементы

print(A<B) #является ли А подмножеством В
print(A>B) #является ли В подмножеством А

print(A<=B) #А является подмножеством В или равно В
print(B>=A)

print(B<=A)
print(C>=A)

if A==D:
    print("True")
else:
    print("False")
