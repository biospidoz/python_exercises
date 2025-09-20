import math
print("Введите координаты точки A: ")
a1, a2, *_ = input().split(" ")
print("Введите координаты точки B: ")
b1, b2, *_ = input().split(" ")
a1 = float(a1)
a2 = float(a2)
b1 = float(b1)
b2 = float(b2)

coordinateA =((b1 - a1) ** 2)
coordinateB = ((b2 - a2) ** 2)
action = coordinateB + coordinateA
lengthAB = math.sqrt(float(action))
print("Длина отрезка AB =", f"{lengthAB:.3f}")
