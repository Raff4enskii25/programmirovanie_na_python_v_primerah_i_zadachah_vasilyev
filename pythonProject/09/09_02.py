class Alpha:
    code=123
    def alpha(self):
        print("Alpha:",self.code)
class Bravo(Alpha):
    def bravo(self):
        print("Bravo:",self.code)
class Charlie(Bravo):
    def charlie(self):
        print("Charlie:",self.code)
def show(MyClass):
    print("\nКласс", MyClass.__name__, end=":\n")
    for s in MyClass.__mro__:
        print(f"<{s.__name__}>,", end="",sep="")
show(Alpha)
show(Bravo)
show(Charlie)
A=Alpha()
B=Bravo()
C=Charlie()
print("Объект А:")
A.alpha()
print("Объект В:")
B.bravo()
print("Объект C:")
C.alpha()
C.bravo()
C.charlie()
Bravo.code=321
print("Выполнена команда Bravo.code=321")
print("Объект C:")
C.alpha()
C.bravo()
C.charlie()
print("Объект А:")
A.alpha()