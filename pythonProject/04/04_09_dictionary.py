dictionary = {100:"Сто", 10:"Десять", 1:"Один"}
print(dictionary)
print(dictionary[100])
print(dictionary[10])
print(dictionary[1])
dictionary[3] = "Три"
dictionary[20] = "Двадцать"
dictionary.pop(1)
print(dictionary[3])
print(dictionary[20])
print(dictionary)

print("Второй словарь")
dictionary1=dict(Первый=1, Второй=2, Третий=3)
print(dictionary1)
print(dictionary1["Первый"])
print(dictionary1["Второй"])
print(dictionary1["Третий"])
dictionary1["Четвертый"] = 4
del dictionary1["Первый"]
dictionary1.pop("Второй")
print(dictionary1)