A=[10,20,30,40]
for k in [0,1,2,'три',4,3]:
    #внешний блок:
    try:
        print(f"* Значение элемента А[{str(k)}]: ")
        #внутр.блок
        try:
            A[k]/=(k-1)
            print(A[k])
        except ZeroDivisionError:
            print("Попытка деления на ноль")
            A[k]=0.0
            print("Новое значение",A[k])
        else:
            print("Ошибки деления на ноль нет")
        finally:
            print("Завершение внутр.блока")
    except Exception as error:
        print("что-то пошло не так")
        print(f"Ошибка: {error.__class__.__name__}")
print("Программа завершила выполнение")