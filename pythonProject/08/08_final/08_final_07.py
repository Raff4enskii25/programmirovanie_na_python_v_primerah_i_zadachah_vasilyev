#7. Напишите программу, в которой описана функция. 
# В качестве аргументов функции передаются два объекта одного и того же класса. 
#У каждого объекта есть поле, представляющее собой список из целых 
#чисел. В результате функция возвращает объект того же класса. 
# Полесписок этого объекта получается суммированием соответствующих элементов из полей-списков объектов,
# переданных аргументами функции. Если в этих объектах списки разной длины, то недостающие элементы 
#в списке заменяются нулями.
print("Задание 7")
class MyClass:
    def newList(self, l):
        self.list = l

def func(o1, o2):
    if o1.__class__.__name__ == o2.__class__.__name__:
        newList = o1.__class__()
        newList.list = []
        if(len(o1.list)>len(o2.list)):
            for i in range(len(o1.list)):
                newList.list.append(o1.list[i]+o2.list[i]) if i<len(o2.list) else newList.list.append(0)
        elif len(o1.list)<len(o2.list):
            for i in range(len(o2.list)):
                newList.list.append(o1.list[i]+o2.list[i]) if i<len(o1.list) else newList.list.append(0)
        else:
            for i in range(len(o1.list)):
                newList.list.append(o1.list[i]+o2.list[i])
        print("Созданный список:", newList.list)
        return newList
    else:
        print("Объекты разных классов!")
print("len A>len B")
A, B, =MyClass(), MyClass()
A.newList([1,2,3,4,5,6])
B.newList([1,2,3,4])
C=func(A,B)
print("len A < len B")
A.newList([1,2,3])
B.newList([1,2,3,4,5,6,7,8])
D=func(A,B)
print("len A = len B")
A.newList([1,2,3])
B.newList([1,2,3])
E=func(A,B)
    