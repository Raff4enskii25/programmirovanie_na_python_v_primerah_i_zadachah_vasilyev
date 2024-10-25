def count_sum(*n):
    s = 0
    for i in n:
        s+= i
    return s

def count_sum2(*n):
    return sum(n)

def sqr_sum(*n):
    s = 0
    for i in n:
        s+= i*i
    return s

def get_text(*t):
    return " ".join(t)

sum1 = count_sum(1,2,3,4,5,6,7,8,9)
sum2 = sqr_sum(1,2,3,4,5,6,7,8,9)
sum3 = count_sum2(1,2,3,4,5,6,7,8,9)
text = get_text("привет","я","андрей")

print(f"Сумма: {sum1}")
print(f"Сумма2: {sum3}")
print(f"Сумма квадратов: {sum2}")
print(f"Текст: {text}")

def show(*val):
 print("Тип:", type(val))
 print("Аргумент:", val)

show(1,2,3,4,5,6)