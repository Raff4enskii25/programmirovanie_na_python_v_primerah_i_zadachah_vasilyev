#Задание № 3. Программа в которой пользователю предлагается ввести текст, а затем в этом тексте. 
#без применения специальных методов (а именно, не используя метод swapcase()), все большие буквы 
#меняются на маленькие, а маленькие - на большие
txt = "adgkrFGgkFEOWKV"
new_txt = ""
m = ord("a")
n = ord("z")
M = ord("A")
N = ord("Z")

print("a =", m, "z =", n, "A =", M, "Z =", N)
print("Исходная строка: ", txt)

for k in txt:
    if ord(k) >= m and ord(k) <= n:
        k = chr(ord(k) - (n - N))   
    elif ord(k) >= M and ord(k) <= N:
        k = chr(ord(k) + (n - N))
    
    new_txt += k
print("Строка после редактирования: ", new_txt)