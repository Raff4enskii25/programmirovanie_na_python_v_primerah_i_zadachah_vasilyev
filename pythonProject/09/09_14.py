class Alpha:
    def __getattr__(self,name):
        return len(name)
class Bravo:
    def show(self,x):
        print("Метод show()",x)
    def __getattr__(self,name):
        if len(name)<5:
            return lambda x:print("Первый метод:",x)
        else: return lambda x:print("Второй метод", x*x)
print("Object A classname Alpha")
A=Alpha()
A.value="Alpha"
print("Value field:", A.value)
print("Color field:", A.color)
print("Myattribute field:", A.myattribute)
print("Object B classname Bravo")
B=Bravo()
B.show(10)
B.hi(10)
B.display(10)
B.format(20)