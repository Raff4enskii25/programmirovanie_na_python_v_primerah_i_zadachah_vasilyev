from fractions import Fraction
from decimal import Decimal

A = Fraction(1,3)
print("A=",A)
B = Fraction(2,5)
print("B=", B)
Alpha = 1/3
print("Alpha=",Alpha)
Beta = 2/5
print("Beta=",Beta)
print("A+B=", A+B)
print("Alpha+Beta=", Alpha + Beta)

print("Числа заданной точности (Decimal)")
A=Decimal('1.01')
print("A=", A)
B=Decimal('2.02')
print("B=", B)
print("A+B=", A+B)
Alpha, Beta = 1.01, 2.02
print("Alpha+Beta=", Alpha+Beta)