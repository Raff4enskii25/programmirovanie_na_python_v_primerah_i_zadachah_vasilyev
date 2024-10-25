class Alpha:
    code=123
    def __init__(self,num):
        print("Constructor #1")
        self.number=num
        print("Object is created")
        self.show()
    def show(self):
        print("Method #1")
        print("Class:", self.__class__.__name__)
        print("Class code:", self.__class__.code)
        print("Number field:", self.number)
        print("-"*20)

class Bravo(Alpha):
    code = 456
class Charlie(Bravo):
    def __init__(self, num,txt):
        print("Constructor #2")
        self.number=num
        self.name=txt
        print("New object")
        self.show()
    def show(self):
        print("Method #2")
        print("Class:", self.__class__.__name__)
        print("Class code:", self.__class__.code)
        print("Number field:", self.number)
        print("Name field:", self.name)
        print("-"*20)
class Delta(Charlie):
    code=789

A=Alpha(100)
A.code=321
print("After comand A.code=321")
A.show()
B=Bravo(200)
C=Charlie(300, "C")
D=Delta(400,"D")
A.show()
print("A.code =", A.code)