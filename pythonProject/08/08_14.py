def create(fields, vals, name=None):
    if type(name)!=str:
        name="MisterX"
    if type(fields)!=list or type(vals)!= list:
        class MyClass:
            def show(self):
                print("Объект без полей")
                print("Класс", self.__class__.__name__)
    else:
        class MyClass:
            def __init__(self):
                k=0
                for f in fields:
                    self.__dict__[f]=vals[k]
                    k+=1
            def show(self):
                print("Объект с полями:")
                for s in dir(self):
                    if not s.startswith("_") and s!="show":
                        print(s,"=", self.__dict__[s])
                print("Класс", self.__class__.__name__)
    MyClass.__name__ =name
    return MyClass()
A=create(["red","green","blue"],[1,2,3],"MyColors")
A.show()
B=create(["alpha","bravo"], ["Alpha","Bravo"])
B.show()
A.red=100
A.green=200
A.blue=300
A.show()
D=A.__class__()
D.show()
C=create(1,2,3)
C.show()
