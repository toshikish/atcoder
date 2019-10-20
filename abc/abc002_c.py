xa, ya, xb, yb, xc, yc = map(int, input().split())
a, b = xb - xa, yb - ya
c, d = xc - xa, yc - ya
print(abs(a * d - b * c) / 2)
