class Alpha:
    def __getattr__(self,name):
        return "такого атрибута нет!"
    def __delattr__(self, name):
        if name=="number":
            print("Удалять нельзя!")
        else:
            object.__delattr__(self,name)
A=Alpha()
A.value="объект А"
print('value:', A.value)
del A.value
print('value:', A.value)
A.number=123
print('number:',A.number)
del A.number
print("number:", A.number)
del A.__dict__["number"]
print("number:", A.number)