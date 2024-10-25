class Alpha:
    def alpha(self):
        print("Class Alpha")
class Bravo:
    def bravo(self):
        print("Class Bravo")
class Charlie:
    def charlie(self):
        print("Class Charlie")
class Delta(Alpha,Bravo,Charlie):
    pass
print("Наследование:")
k=1
for s in Delta.__mro__:
    print(f"[{k}] {s.__name__}")
    k+=1
obj=Delta()
obj.alpha()
obj.bravo()
obj.charlie()