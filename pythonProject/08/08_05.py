class Alpha:
    pass
class Bravo:
    pass
MyClass = Alpha
A = MyClass()
MyClass = Bravo
B=MyClass()
Alpha=Bravo
C=Alpha()
MyClass=A.__class__
D=MyClass()
print("Объект А:", type(A).__name__)
print("Объект B:", type(B).__name__)
print("Объект C:", type(C).__name__)
print("Объект D:", type(D).__name__)
MyClass.__name__ ="First"
Bravo.__name__ = "Second"
print("Объект А:", type(A).__name__)
print("Объект B:", type(B).__name__)
print("Объект C:", type(C).__name__)
print("Объект D:", type(D).__name__)