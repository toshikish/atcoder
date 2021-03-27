from math import sin, cos, pi

N = int(input())
x0, y0 = map(int, input().split())
p0 = complex(x0, y0)
xh, yh = map(int, input().split())
ph = complex(xh, yh)

pm = (p0 + ph) / 2
theta = 2 * pi / N
r = complex(cos(theta), sin(theta))
p1 = pm + (p0 - pm) * r
print(p1.real, p1.imag)
