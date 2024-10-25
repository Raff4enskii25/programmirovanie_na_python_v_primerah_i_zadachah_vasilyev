#9. Напишите программу, в которой создается итератор, генерирующий 
#нечетные натуральные числа. Количество генерируемых чисел определяется аргументом конструктора.
print("Задание 9")
class Main:
    def __init__(self,n):
        if type(n)==int: self.number = n; self.count=0; self.round=1; self.n=0
        else: print("Значение - не число!")
    def __iter__(self):
        return self
    def __next__(self):
        if self.count != self.number:
            if self.round%2!=0:
                self.n = self.round
                self.round +=1
                self.count +=1
                return self.n
            else: 
                self.round+=1
                return self.__next__()
        else: raise StopIteration
A=Main(10)
for i in A:
    print(i, end=" ")