class MyClass:
    def __del__(self):
        print("Удален объект")
A = MyClass()
B=A
del A