vals=iter([100,"A",[1,2]])
try:
    print("Первое:",next(vals))
    print("Второе:",next(vals))
    print("Третье:",next(vals))
    print("Четвертое:",next(vals))
except StopIteration:
    print("Значений больше нет!")