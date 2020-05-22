import math

l = list(map(int, input().split()))

l.sort()
R = sum(l)
r = max(l[2] - l[1] - l[0], 0)
print(math.pi * (R * R - r * r))
