A=[10,20,30,40]
for k in [0,1,2,"три",4,3]:
    try:
        print(f"A[{str(k)}]=", end="")
        A[k]/=(k-1)
        print(A[k])
    except IndexError:
        print("нет такого элемента!")
    except ZeroDivisionError:
        A[k]=0.0
        print(A[k], "- деление на ноль")
    except TypeError:
        print("неверный тип индекса!")