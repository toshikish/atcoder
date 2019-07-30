N = int(input())

res = N
base = 1
ans = 0
while res > 0:
    ans += (N // (base * 10)) * base
    r = N % (base * 10) + 1
    if r >= base:
        ans += min(r - base, base)
    base *= 10
    res //= 10
print(ans)
