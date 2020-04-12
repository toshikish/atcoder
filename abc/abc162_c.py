from math import gcd

K = int(input())

ans = 0
ans += sum(range(1, K + 1))
for i in range(1, K):
    for j in range(i + 1, K + 1):
        ans += gcd(i, j) * 6
for i in range(1, K - 1):
    for j in range(i + 1, K):
        for k in range(j + 1, K + 1):
            ans += gcd(gcd(i, j), k) * 6
print(ans)
