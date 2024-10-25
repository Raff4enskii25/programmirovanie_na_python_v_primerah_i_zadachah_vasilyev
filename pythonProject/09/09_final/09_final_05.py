#5. Напишите программу, в которой для объектов класса предусмотрены 
#операции сравнения. У каждого объекта есть поле-список с числовыми 
#значениями. Операции сравнения выполняются так: объекты на предмет 
# равенства проверяются по первому элементу в списках, на предмет 
#«не равно» — по второму элементу в списках, «меньше» — по третьему 
# элементу в списках, и так далее. Если соответствующего элемента 
#в списке нет, используется нулевое значение.
print("Задание 5")
class Main:
    def __init__(self, val):
        if type(val)==list: self.value=val
        else: print("Значение не является списком!")
    def __eq__(self, obj, n=1-1):
        s = self.value[n] if len(self.value)>n else 0
        o = obj.value[n] if len(obj.value)>n else 0
        return s==o
    def __ne__(self,obj,n=2-1):
        s = self.value[n] if len(self.value)>n else 0
        o = obj.value[n] if len(obj.value)>n else 0
        return s!=o
    def __lt__(self,obj,n=3-1):
        s = self.value[n] if len(self.value)>n else 0
        o = obj.value[n] if len(obj.value)>n else 0
        return s<o
    def __le__(self,obj,n=4-1):
        s = self.value[n] if len(self.value)>n else 0
        o = obj.value[n] if len(obj.value)>n else 0
        return s<=o
    def __gt__(self,obj,n=5-1):
        s = self.value[n] if len(self.value)>n else 0
        o = obj.value[n] if len(obj.value)>n else 0
        return s>o
    def __ge__(self,obj,n=6-1):
        s = self.value[n] if len(self.value)>n else 0
        o = obj.value[n] if len(obj.value)>n else 0
        return s>=o
A=Main([1,2,3,4,5,6,7,8])
B=Main([1,3,5,7,9,11,13,15,17])
C=Main([-1,-2,-3])
D=Main("Hi!")
print("A:", A.value)
print("B:", B.value)
print("C:", C.value)
print("A==B", A==B)
print("A!=B", A!=B)
print("A<B", A<B)
print("A<=B", A<=B)
print("A>B", A>B)
print("A>=B", A>=B)
print("C>=A", C>=A)
print("A>C", A>C)