nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Элементы списка с индексом от 0 до 3:", nums[0: 3])
print("Длина списка:", len(nums))
print("Последний элемент списка:", nums[-1])
print("Наибольшее значение:", max(nums), "Наименьшее значение:", min(nums))
print("Сумма:", sum(nums))
nums[1:-1]=[22,23]
print("Список после замены элементов", nums)
del nums[0: -1]
print("Список после удаления элементов:", nums)
nums = list(range(5,10))
print("Список символов от 5 до 10:", nums)
print("По возрастанию:", list(sorted(nums)))
print("По убыванию:", list(sorted(nums, reverse=True)))
nums=[2*k+1 for k in range(5)]
print("Нечетные числа:", nums)


symbs = list("Python")
print("Список из символов:", symbs)
print("Два первых символа:", symbs[:2])
print("Прочие символы:", symbs[2:])
del symbs[2:4]
print("Список с символами после удаления:", symbs)
print("Два последних символа:", symbs[-2:])
