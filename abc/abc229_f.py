from itertools import product

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 1e16

ans = INF
for s in range(2):
    dp = [INF] * 2
    dp[s] = 0
    for i in range(N):
        ndp = [INF] * 2
        for pj, j in product(range(2), repeat=2):
            t = dp[pj]
            if j == 0:
                t += A[i]
            if j == pj:
                t += B[(i - 1) % N]
            ndp[j] = min(ndp[j], t)
        dp = ndp
    ans = min(ans, dp[s])

print(ans)
