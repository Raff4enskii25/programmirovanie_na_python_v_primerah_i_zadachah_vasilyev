class MyClass:
    def __init__(self, n="Белый"):
        self.name=n
        print("Создан объект", self.name)
    def __del__(self):
        print("Удален объект:", self.name)

def create(n):
    obj = MyClass(n)

A = MyClass()
B = MyClass("Красный")
C = MyClass("Синий")
create("Желтый")
C.name="Зеленый"

del A; del B; del C