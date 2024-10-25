from copy import *
class MyClass:
    pass
A=MyClass()
A.value=100
A.nums=[1,2,3]
B=A
C=copy(A)
D=deepcopy(A)
print("A:", A.value, "и", A.nums)
print("B:", B.value, "и", B.nums)
print("C:", C.value, "и", C.nums)
print("D:", D.value, "и", D.nums)
print("A.value=200 и A.nums[1=0]")
A.value=200
A.nums[1]=0
print("A:", A.value, "и", A.nums)
print("B:", B.value, "и", B.nums)
print("C:", C.value, "и", C.nums)
print("D:", D.value, "и", D.nums)
print("Удаляется А")
del A
print("B.value=300 и B.nums[2]=4")
B.value=300
B.nums[2]=4
print("B:", B.value, "и", B.nums)
print("C:", C.value, "и", C.nums)
print("D:", D.value, "и", D.nums)