def checkGlobals():
    global A, B
    A = "Alpha"
    B = "Beta"
    D = "Delta"
    print(f"A в функции: {A}")
    print(f"B в функции: {B}")
    print(f"C в функции: {C}")
    print(f"D в функции: {D}")

A = "А"
C = "C"
D = "D"

print(f"До вызова функции А={A}")
print(f"До вызова функции C={C}")
print(f"До вызова функции D={D}")

checkGlobals()

print(f"A после функции: {A}")
print(f"B после функции: {B}")
print(f"C после функции: {C}")
print(f"D после функции: {D}")