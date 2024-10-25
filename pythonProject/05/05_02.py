name = "Python"
num = 12.34567
A ="'Python'\n'Java'n\'C#'"
print(A)
print("Кол-во символов", len(A))
a = r"'Python'\n'Java'\n'C#'"
print(a)
print("Кол-во символов", len(a))

print(f"Язык {name} - крутой!")
print(f"Число {num:9.3f}")
print(f"Число {num:09.3f}")
print(f"Число {num}")
num = 12
print(f"Число {num:#9b}")