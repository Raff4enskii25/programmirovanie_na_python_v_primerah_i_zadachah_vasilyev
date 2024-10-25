#10. Напишите программу, в которой создается итератор, генерирующий 
#числа Фибоначчи (первые два числа равны единице, а каждое следующее есть сумма двух предыдущих).
#Количество генерируемых чисел передается в качестве аргумента конструктору при создании итератора.
print("Задание 10")
class Main:
    def __init__(self, n):
        self.number = n
        self.count = 0
        self.a = 1
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count != self.number:
            if self.count <2:
                self.count +=1
                return 1
            else:
                self.count +=1
                self.n = self.a + self.b
                self.a, self.b=self.b, self.b+self.a
                return self.n
        else: raise StopIteration
A=Main(15)
for i in A:
    print(i, end=" ")