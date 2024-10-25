#10. Напишите программу, в которой создается бинарное дерево объектов: в вершине структуры находится объект, который содержит ссылки 
#на два объекта того же класса. Каждый из этих объектов содержит ссылки на два объекта, и так далее.
print("Задание 10")
class Tree:
    def __init__(self, n=1):
        if n==0:
            self.first = None
            self.second = None
        else:
            self.first = Tree(n-1)
            self.second =Tree(n-1)
    def show(self, lvl=1):
        if self.first != None:
            print(f"Level {lvl}:", "First:", hasattr(self, 'first'), "|", "Second:", hasattr(self, 'second',))
            self.first.show(lvl+1)
A=Tree(5)
A.show()
