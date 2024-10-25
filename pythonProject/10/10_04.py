print("Начинаем генерировать ошибки:")
error=Exception("Первая ошибка")
try:
    try:
        try:
            raise error
        except:
            print(error)
            raise
    except Exception as e:
        print("Повторная обработка:")
        print(e)
        try:
            raise ArithmeticError("Вторая ошибка")
        except ArithmeticError as e:
            print(e)
        raise Warning
except Warning:
    print("Еще одна ошибка")
print("Ошибок больше нет")