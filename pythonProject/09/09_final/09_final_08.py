#8. Напишите программу с классом, объекты которого можно вызывать. 
#У объекта класса должно быть поле-список с числовыми значениями, 
#а результатом метод возвращает полиномиальную сумму. В частности, 
#если в списке содержатся числа a0, a1, …, an и в качестве аргумента 
# объекту при вызове передается значение x, то в качестве результата должно 
#возвращаться значение a0 + a1x + a2x^2 + … + anx^n.
print("Задание 8")
class Main:
    def __init__(self, lis, x=1):
        if type(lis)==list: self.value=lis; self.x=x; self.position=-1
        else: print("Значение не является списком!")
    def __iter__(self):
        return self
    def __next__(self):
        self.position+=1
        if self.position<len(self.value):
            res=self.value[self.position]*(self.x**self.position) if self.position>0 else self.value[self.position]
            return res
        else: raise StopIteration
A=Main([1,2,3,4,5],2)
for i in A:
    print(i, end=" ")