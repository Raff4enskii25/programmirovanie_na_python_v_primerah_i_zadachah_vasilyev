#8. Напишите программу, в которой пользователь вводит момент времени,
#а программа определяет интервал между текущим моментом и моментом времени, который указал пользователь.
print("Задание 8")
from datetime import datetime
userDt = datetime.fromisoformat(input("Введите дату: (пр. '2024-10-11 01:39:52')" ))
curDt = datetime.today()
inter = curDt - userDt
print("Интервал между текущим моментом и вашей датой:", inter)
