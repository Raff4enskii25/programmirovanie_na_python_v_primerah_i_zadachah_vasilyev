A=[10,20,30,40]
for k in [0,1,2,"три",4,3]:
    try:
        print(f"* Значение элемента A[{str(k)}]: ", end="")
        A[k]/=(k-1)
        print(A[k])
    except (TypeError,IndexError) as error:
        print()
        print("Исключение класса:", error.__class__.__name__)
        print(error.__doc__)
        print("Базовый класс:", error.__class__.__bases__[0].__name__)
    except ZeroDivisionError as error:
        print()
        print("Произошла ошибка деления на ноль")
        print("Цепочка наследования")
        for s in error.__class__.__mro__:
            print(s.__name__)
        A[k]=0.0
        print("Элементу присвоено значение", A[k])