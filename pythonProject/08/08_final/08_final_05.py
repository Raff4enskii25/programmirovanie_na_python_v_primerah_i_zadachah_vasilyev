#5. Напишите программу, в которой описывается функция, предназначенная для создания объекта.
#  Объект создается на основе уже существующего объекта, который передается функции в качестве аргумента. 
#В создаваемый объект добавляются только те неслужебные поля из исходного объекта, которые имеют целочисленное значение.
print("Задание 5")
class MyClass:
    def __init__(self):
        self.value = 123
        self.num = 5
        self.text = "txt"
def func(obj):
    newObj = obj.__class__()
    for i in dir(newObj):
        if not i.startswith("_"):
            value = getattr(newObj, i)
            if isinstance(value, str):
                delattr(newObj, i)
    return newObj
A=MyClass()
B=func(A)
print("B:", B.__dict__)