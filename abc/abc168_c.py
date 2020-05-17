from math import cos, sqrt, radians
A, B, H, M = map(int, input().split())

d1 = 30 * (H + M / 60)
d2 = M * 6
print(sqrt(A * A + B * B - 2 * A * B * cos(radians(abs(d1 - d2)))))
