from fractions import gcd
from functools import reduce

MOD = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))

L = reduce(lambda x, y: x * y // gcd(x, y), A)

ans = 0
for i in range(N):
    ans += L // A[i]
print(ans % MOD)
