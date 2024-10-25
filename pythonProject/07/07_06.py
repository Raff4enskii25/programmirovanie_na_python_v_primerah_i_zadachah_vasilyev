from datetime import date
mydate = date(2024, 10,9)
print("Дата:", mydate)
print("День:", mydate.day)
print("Месяц", mydate.month)
print("Год:", mydate.year)
print("День недели:", mydate.weekday())
print("День недели:", mydate.isoweekday())
newdate = mydate.replace(2077, month = 3)
print("Новая дата:", newdate)
mydate = date.fromisoformat("2024-10-09")
print("Дата:", mydate)
todayDate = date.today()
print("Сегодняшняя дата:", todayDate)
print("До новой даты:", newdate-todayDate)