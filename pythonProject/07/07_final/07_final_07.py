#7. Напишите программу, в которой пользователь вводит две даты,
#  а программа определяет количество полных дней между этими датами.
print("Задание 7")
from datetime import date
date1 = date.fromisoformat(input("Введите дату 1: (пр. 2024-10-11) "))
date2 = date.fromisoformat(input("Введите дату 2: (пр. 2025-10-11) "))

days = 0
if date1>date2:
    days = date1-date2
else:
    days = date2-date1
print("Кол-во полных дней между датами:", days.days)