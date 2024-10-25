A = ["Python", "Java", "C#"]
print("Cписок A:", A)
B =", ".join(A)
print("Строка B:", B)
B = B.partition(",")
print("Разделитель - ',' :", B)

print()
C = "Python, Java, C#"
print(C)
print(C.split())
print("До разбики на подстроки:",C.splitlines())
C = """Python
Java
C#"""
print("После:", C.splitlines())