text = "Python"
num = 20
A = text.ljust(num, "_")
B = text.center(num, "_")
C = text.rjust (num, "_")
print('|', A, '|')
print('|', B, '|')
print('|', C, '|')