L, R = map(int, input().split())

if L // 2019 < R // 2019 or L % 2019 == 0:
    ans = 0
else:
    l = L % 2019
    r = R % 2019
    ans = 2019
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            ans = min(ans, (i * j) % 2019)
print(ans)
