while True:
    res=input("Введите натуральное число: ")
    try:
        num=int(res)
        if num<1:
            msg="Число должно быть натуральным"
            raise ArithmeticError(msg)
    except ArithmeticError as er:
        print(er)
    except:
        print("Ошибка ввода")
    #если ошибок не было
    else:
        break
print("Сумма от 1 до", num,"=",sum(range(num+1)))