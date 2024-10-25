class Alpha:
    def __init__(self):
        self.set(100)
        print("Объект класса Alpha:", self.number)
    def set(self,n):
        self.number=n
    def show(self):
        print(self.__class__.__name__, self.number)
class Bravo(Alpha):
    def __init__(self):
        self.set(200)
        print("Объект класса Bravo:", self.number)
A=Alpha()
A.set(123)
A.show()
B=Bravo()
B.set(321)
B.show()