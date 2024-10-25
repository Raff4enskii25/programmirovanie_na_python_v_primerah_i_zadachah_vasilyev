class MyClass:
    def __init__(self,num):
        self.code=num
    def __str__(self):
        return str(self.code)
    def __add__(self,n):
        if type(n)==int:
            val=self.code+n
        else: val=0
        return MyClass(val)
A=MyClass(100)
print("Object A:", A)
B=A+25
print("Object B:", B)
C=A+"Hello"
print("Object C:", C)