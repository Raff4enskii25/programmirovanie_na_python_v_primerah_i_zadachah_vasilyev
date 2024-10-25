class MyClass:
    def __init__(self, val):
        self.value=val
    def __str__(self):
        return "Поле "+str(self.value)
    def __bool__(self):
        if type(self.value)==int:
            return True
        else:
            return False
    def __int__(self):
        if self:
            return self.value
        else:
            return 0
print("Object A")
A=MyClass(100)
print(A)
print("Число", int(A))
print("A - 1 =", int(A)-1)
print("Object B")
B=MyClass("B")
print(B)
print("Число", int(B))
print("B + 1=",int(B)+1)
print("Bool A:", bool(A))
print("Bool B:", bool(B))