from math import pi, sin

A, B, C = map(int, input().split())

t_low = 0
t_high = (B + 100 + A - 1) // A
while True:
    t_mid = (t_low + t_high) / 2
    f = A * t_mid + B * sin(C * t_mid * pi)
    diff = f - 100
    if abs(diff) < 0.000001:
        break
    if diff >= 0:
        t_high = t_mid
    else:
        t_low = t_mid
print(t_mid)
