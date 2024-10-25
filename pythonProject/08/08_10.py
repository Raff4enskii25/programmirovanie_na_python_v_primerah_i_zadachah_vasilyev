class Alpha:
    "Это класс Alpha"
    pass
class Bravo:
    "Это класс Bravo"
print(Alpha.__doc__)
print(Bravo.__doc__)
A=Alpha()
B=Bravo()
Alpha.__doc__ ="Первый класс"
B.__class__.__doc__ ="Второй класс"
print(A.__class__.__doc__)
print(Alpha.__doc__)
print(B.__doc__)
print(Bravo.__doc__)
