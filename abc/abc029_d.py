N = int(input())

res = N
base = 1
ans = 0
while res > 0:
    ans += (N // (base * 10)) * base
    r = N % (base * 10) + 1
    if base <= r < 2 * base:
        ans += r - base
    elif r >= 2 * base:
        ans += base
    base *= 10
    res //= 10
print(ans)
