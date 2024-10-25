class Alpha:
    pass
class Bravo:
    name="Bravo"
    def display():
        print("Поле name:", Bravo.name)
    def show(self):
        print("Поле value:", self.value)
    def __init__(self):
        self.value = 123
A = Alpha()
B = Bravo()
print("Класс Alpha")
n=1
for s in Alpha.__dict__:
    print(f"[{n}] {s}: {Alpha.__dict__[s]}")
    n+=1
n=1
print("Класс Bravo")
for s in Bravo.__dict__:
    print(f"[{n}] {s}: {Bravo.__dict__[s]}")
    n+=1
print("Объект А:", A.__dict__)
print("Объект В", B.__dict__)
Bravo.display()
Alpha.display = Bravo.display
del Bravo.display
B.show()
A.color = "Красный"
B.show=lambda: print("Объект В", B.value)
print("Класс Alpha")
n=1
for s in Alpha.__dict__:
    print(f"[{n}] {s}: {Alpha.__dict__[s]}")
    n+=1
print("Класс Bravo")
n=1
for s in Bravo.__dict__:
    print(f"[{n}] {s}: {Bravo.__dict__[s]}")
    n+=1
print("Объект А:", A.__dict__)
print("Объект В", B.__dict__)
Alpha.display()
Bravo.show(B)
B.show()