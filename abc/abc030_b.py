n, m = map(int, input().split())
d = abs(30 * (n % 12) + 0.5 * m - 6 * m)
print(min(d, 360 - d))
