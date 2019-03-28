N, Y = map(int, input().split())

ans = (-1, -1, -1)
for x in range(N + 1):
    for y in range(N - x + 1):
        z = N - x - y
        if z < 0:
            continue
        if 10000 * x + 5000 * y + 1000 * z == Y:
            ans = (x, y, z)
print(ans[0], ans[1], ans[2])
