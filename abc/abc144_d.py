import math

a, b, x = map(int, input().split())

h = x / a / a
r = b - h
t = 2 * r / a if h >= b / 2 else a * b * b / 2 / x
print(math.degrees(math.atan(t)))
