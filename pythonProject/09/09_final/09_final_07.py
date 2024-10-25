#7. Напишите программу с классом, объекты которого можно индексировать.
#  В частности, у объекта должно быть два поля-списка с числами. 
#При индексировании объекта возвращается сумма элементов из списков 
#с соответствующим индексом. Если в каком-то списке нет такого элемента, он заменяется нулевым значением.
print("Задание 7")
class Main:
    def __init__(self, lis1, lis2):
        if (type(lis1) and type(lis2))==list:
            self.first_list = lis1
            self.second_list = lis2
            self.position=-1
            self.maxList = len(self.first_list) if len(self.first_list)>=len(self.second_list) else len(self.second_list)
        else: print("Какой-то из аргументов не является списком!")
    def __iter__(self):
        return self
    def __next__(self):
        self.position+=1
        if self.position < self.maxList:
            fi = self.first_list[self.position] if len(self.first_list)>self.position else 0
            si = self.second_list[self.position] if len(self.second_list)>self.position else 0
            return fi+si
        else: self.position=-1; raise StopIteration
        
A=Main([1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10])
for i in A:
    print(i, end=" ")
print()