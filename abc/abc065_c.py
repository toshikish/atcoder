import math

N, M = map(int, input().split())
MOD = 10 ** 9 + 7

if N == M:
    ans = math.factorial(N) * math.factorial(M) * 2 % MOD
elif abs(N - M) == 1:
    ans = math.factorial(N) * math.factorial(M) % MOD
else:
    ans = 0
print(ans)
