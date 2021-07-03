N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 1e24
for k in range(1, N + 1):
    dp = [[-1] * k for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(N):
        jmax = min(i + 1, k)
        for j in range(jmax - 1, -1, -1):
            for r in range(k):
                if dp[j][r] == -1:
                    continue
                nr = (r + A[i]) % k
                dp[j + 1][nr] = max(dp[j + 1][nr], dp[j][r] + A[i])
    if dp[k][X % k] != -1:
        ans = min(ans, (X - dp[k][X % k]) // k)

print(ans)
