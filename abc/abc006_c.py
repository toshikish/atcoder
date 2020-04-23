N, M = map(int, input().split())

x = y = z = 0
a = M - 2 * N
if a < 0 or a > 2 * N:
    x = y = z = -1
else:
    if 0 <= a <= N:
        x = N - a
        y = a
        z = 0
    else:
        x = 0
        y = 2 * N - a
        z = a - N
print(x, y, z)
