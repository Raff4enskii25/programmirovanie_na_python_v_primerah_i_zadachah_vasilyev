class MyClass:
    pass
A = MyClass()
B = MyClass()

print("Объект А:", A)
print("Объект В:", B)

print("Класс объекта А:", type(A).__name__)
print("Класс объекта B:", type(B).__name__)
print("Класс объекта А:", type(A))
print("Сравнение объектов:", A==B, B==A)