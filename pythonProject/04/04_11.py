days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weeks = dict([(days[i], i+1) for i in range(len(days))])
print(weeks)
dayOfWeek = input("Введите день недели: ")
print(dayOfWeek,"это", weeks[dayOfWeek],"день недели по счету")

order={k: 2**k for k in range(1, 10)}
degree = int(input("Введите число для возведения двойки в степень: "))
print("2 в степени", degree, "равно", order[degree])
print(order)