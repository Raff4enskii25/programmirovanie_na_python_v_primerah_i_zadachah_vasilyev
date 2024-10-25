A={1,2,3,4,5, "Hello!"}
B={1,2,3,4,5,6,7,8,9}
C={1,2,3,4,5,6,7,8,9, "This is from C!"}
print("A:",A)
print("B:",B)
print("C:", C)
print("Объединение A с B:", A.union(B))
print("Пересечение А с В:", A.intersection(B))
print("Разность В с А:", B.difference(A))
print("Симметрическая разность A с B:", A.symmetric_difference(B))
A.update(B)
print("Множество А после добавления в него элементов В (A.update(B)):", A)
print("B:", B)
A.intersection_update(B)
print("После A.intersection_update(B):", B)
print("Остались только те элементы А, которые входят в В")

A.symmetric_difference_update(C)
print("После A.symmetric_difference_update(C):", A)
print("Остались только те элементы, которые встречаются в данных множествах только 1 раз!")