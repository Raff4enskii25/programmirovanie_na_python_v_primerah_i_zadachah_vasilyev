import random
random.seed(666)
nums=[[random.randint(0, 15) for i in range(2)] for i in range(5)]
order = dict(nums)

for i in order.keys():
    print("Ключ:",i,"Значение", order[i], sep=" ")

for k in order.values():
    print(k, end=" ")

print()
print("Значение", order[14])
print("Значение", order.get(0, "Нет такого ключа!")) #словарь.get(ключ, значение) возвращает значение ключа, если такой ключ есть
print("Значение", order.get(15, "Нет такого ключа!")) #а если такого ключа нет, то возвращается значение, введенное через запятую
print("Значение", order.get(15))