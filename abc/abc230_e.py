N = int(input())

ans = 0
for i in range(1, N + 1):
    d = N // i
    c = (N // d) - (N // (d + 1))
    ans += d * c
    if c > 1:
        break

d0 = d - 1
for d in range(d0, 0, -1):
    c = (N // d) - (N // (d + 1))
    ans += d * c

print(ans)
