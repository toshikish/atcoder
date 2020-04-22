from math import sqrt

x, y = map(int, input().split())
N = int(input())
V = [tuple(map(int, input().split())) for i in range(N)]

ans = 1000000007
for i in range(N):
    x1, y1 = V[i]
    x2, y2 = V[(i + 1) % N]
    a = y2 - y1
    b = -(x2 - x1)
    c = x2 * y1 - x1 * y2
    d = abs(a * x + b * y + c) / sqrt(a * a + b * b)
    ans = min(d, ans)

print(ans)
