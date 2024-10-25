class Alpha:
    def __getattribute__(self, name):
        print("Alpha: запрос поля",name)
        return object.__getattribute__(self,name)
    #если атрибута нет
    def __getattr__(self,name):
        print("Нет такого поля!")
        return "Alpha "+name
class Bravo:
    def __getattribute__(self,name):
        print("Bravo: запрос поля",name)
        try:
            res=object.__getattribute__(self,name)
        except AttributeError:
            res="Bravo: нет поля",name
        return res
print("Объект А класса Alpha")
A=Alpha()
A.value=123
print("Поле value:", A.value)
print("Еще раз:", object.__getattribute__(A,"value"))
A.value=321
print("Поле value:", A.value)
print(A.color)
print("Объект В класса Bravo")
B=Bravo()
B.mylist=[1,2,3]
print("Поле mylist:", B.mylist)
print("Еще раз:", object.__getattribute__(B,"mylist"))
B.mylist=["A","B",'C']
print("Поле mylist:", B.mylist)
print(B.myset)
