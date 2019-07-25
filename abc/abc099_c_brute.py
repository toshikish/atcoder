N = int(input())

ans = N
for i in range(N + 1):
    c = 0
    res = i
    while res > 0:
        c += res % 6
        res //= 6
    res = N - i
    while res > 0:
        c += res % 9
        res //= 9
    ans = min(ans, c)
print(ans)
