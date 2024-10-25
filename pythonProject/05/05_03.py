A="число {}, текст {}, и снова число {}"
txt = A.format(123, 'Python', 321)
print(txt)
txt = "Число {0}, это {0:b} или {0:X}".format(42)
print(txt)
txt="Число: {:_>+20.3E}".format(123.468)
print(txt)
txt="Код: {0:05d}, Символ: {0:*^5c}".format(65)
print(txt)
print()
B="{0:_{2}{1}s}"
num = 6
for k in range(1, num+1):
    print(B.format("V", k,">"), end="")
    print(" "*(2*(num-k)), end="")
    print(B.format("V", k,"<"))