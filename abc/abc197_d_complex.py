from math import sin, cos, pi

N = int(input())
p0 = complex(*list(map(int, input().split())))
ph = complex(*list(map(int, input().split())))

pm = (p0 + ph) / 2
theta = 2 * pi / N
r = complex(cos(theta), sin(theta))
p1 = pm + (p0 - pm) * r
print(p1.real, p1.imag)
