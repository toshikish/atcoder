from math import sin, cos, pi

N = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())

xm = (x0 + xh) / 2
ym = (y0 + yh) / 2
xr = (x0 - xh) / 2
yr = (y0 - yh) / 2
theta = 2 * pi / N
x1 = xm + cos(theta) * xr - sin(theta) * yr
y1 = ym + sin(theta) * xr + cos(theta) * yr
print(x1, y1)
