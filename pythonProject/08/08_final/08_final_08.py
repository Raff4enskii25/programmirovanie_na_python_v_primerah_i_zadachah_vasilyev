#8. Напишите программу, в которой создается цепочка объектов. 
# Для создания цепочки объектов предложите функцию, при вызове которой 
#в качестве аргумента передается целое число, определяющее количество 
#объектов в цепочке. Результатом функция должна возвращать ссылку 
#на первый объект в цепочке.

print("Задание 8")
class MyClass():
    def __init__(self, n=1, v=1):
        self.value = v
        if n==1:
            self.next=None
        else:
            self.next = MyClass(n-1, v+1)
        print(f"[{n}] Создается объект в цепочке")
    def show(self):
        print(self.value, end=" ")
        if self.next !=None:
            self.next.show()

def func(n):
    obj = MyClass(n)
    return obj
B=func(5)
B.show()

