#1
#print("Обработка исключений")
#try:
#    num = int(input("Введите целое число: "))
#    print("Вы ввели целое число!")
#except:
#    print("Нужно было ввести целое число!")

#2
print("Операции со списком чисел")
try:
    nums = eval(input("Введите числовой список (пр 1,2,3,4):"))
    a = int(nums[0])
    b = int(nums[-1])
    print(a, b)
except ValueError:
    print("Ошибка при преобразовании!")    
except TypeError:
    print("TypeError: Недопустимая операция")
except IndexError:
    print("IndexError: неверный индекс!")
except ZeroDivisionError:
    print("ZeroDivisionError: попытка деления на ноль!")
except NameError:
    print("NameError: неверный идентификатор!")
except SyntaxError:
    print("SyntaxError: невозможно вычислить значение!")
except:
    print("Что-то пошло не так!")
print("Завершение программы!")