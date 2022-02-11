N = int(input())
MOD = 998244353

ans = 0
b = 10
while N >= b - 1:
    m = b - b // 10
    ans += m * (m + 1) // 2
    ans %= MOD
    b *= 10
m = N - (b // 10 - 1)
ans += m * (m + 1) // 2
ans %= MOD
print(ans)
