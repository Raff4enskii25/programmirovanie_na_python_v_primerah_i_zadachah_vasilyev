#Напишите программу, в которой для объектов класса предусмотрен 
#специальный режим доступа к полям. В частности, у объекта должно 
#быть поле-список, значением которому можно присваивать только 
#список. Из присваиваемого списка в поле-список копируются только 
#текстовые значения. При считывании значения этого поля возвращается 
# текстовая строка, содержащая только начальные буквы текстовых 
#значений, которые входят в список
print("Задание 6")
class Main:
    def __init__(self, val):
        if type(val)==list:
            print("Начальный список:", val) 
            self.position=-1
            self.value = []
            for i in val:
                if type(i)==str: self.value.append(i)
            print("Итоговый список:", self.value)
        else: print("Аргумент не является списком!")
    def __iter__(self):
        try:
            return self
        except:
            print("Аргумент не является списком!")

    def __next__(self):
        self.position +=1
        self.new_text=""
        if self.position<len(self.value):
            txt = self.value[self.position]
            self.new_text += txt[0]
            return txt[0]
        else:
            print("Новый текст:", self.new_text)
            raise StopIteration
A=Main(["Aurora", "Evgeniy",123, "Albert", "Erik"])
for k in range(len(A.value)):
    print(next(A), end="")
