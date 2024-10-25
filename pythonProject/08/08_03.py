class MyClass:
    def set(self,n):
        self.number = n
    def show(self):
        print("Number =", self.number)

obj = MyClass()
print("Наличие поля number:", hasattr(obj, "number"))
try:
    obj.show()
except AttributeError:
    print("Нет такого поля!")
obj.number = 123
print("Наличие поля number:", hasattr(obj, "number"))
obj.show()
obj.set(321)
obj.show()