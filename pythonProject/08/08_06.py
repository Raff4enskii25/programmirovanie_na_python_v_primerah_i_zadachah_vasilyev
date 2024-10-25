class MyClass():
    color = "Красный"
    def set(txt):
        MyClass.color=txt
    def show():
        print(MyClass.color)
MyClass.show()
MyClass.set("Зеленый")
MyClass.show()
MyClass.color="Синий"
MyClass.show()
A=MyClass()
B=MyClass()
print("Класс:", MyClass.color)
print("Объект A:", A.color)
print("Объект В", B.color)
A.color="Белый"
print("Класс:", MyClass.color)
print("Объект A:", A.color)
print("Объект В", B.color)
MyClass.color="Желтый"
print("Класс:", MyClass.color)
print("Объект A:", A.color)
print("Объект В", B.color)
del A.color
print("Класс:", MyClass.color)
print("Объект A:", A.color)
print("Объект В", B.color)