class MyClass:
    def set(self,n):
        self.number = n
    def show(self):
        print("Поле number у self:", self.number)

A = MyClass()
B = MyClass()
A.set(100)
B.set(200)
A.show()
B.show()
A.number=123
B.number=321
A.show()
B.show()
A.newNumber= 666
print(A.newNumber)