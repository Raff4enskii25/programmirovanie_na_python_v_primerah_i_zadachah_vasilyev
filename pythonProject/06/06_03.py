def shift(val):
    print("Функция shift()")
    print(f"Исходное значение: {val}")
    val = ["A","B","C"]
    print(f"После обработки: {val}")

def change(val):
    print("Функция change()")
    print(f"Исходное значение: {val}")
    if type(val) == list:
        for i in range(len(val)):
            val[i] *=2
    else:
        val *= 2
    print(f"После обработки: {val}")

a = 10
l = [10,20,30]

shift(a)
print(f"a после функции = {a}")
change(a)
print(f"a после функции = {a}")

print()
shift(l)
print(f"l после функции = {l}")
change(l)
print(f"l после функции = {l}")
#Для переменной L создается копия, и эта копия ссылается на тот же список,
#  на который ссылается переменная L. Поэтому когда в теле функции мы пытаемся изменить значения элементов списка,
#  на которые ссылается аргумент, мы на самом деле вносим изменения в тот же список, на который ссылается переменная L.