N = int(input())

ans = 0
d = 2
while N >= 10 ** d - 1:
    hd = d // 2
    ans += 9 * (10 ** (hd - 1))
    d += 2

hd = d // 2
base = 10 ** hd
i = 10 ** (hd - 1)
while i * base + i <= N:
    ans += 1
    i += 1

print(ans)
