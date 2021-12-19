from bisect import bisect_left

N, X = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    ans = X
elif X == 1:
    ans = 1
else:
    D = bisect_left(A, X)
    if D == N:
        ni = X // A[-1]
        dp = [ni, ni + 1]
        x = X % A[-1]
        S = D - 2
    else:
        dp = [0, 1]
        x = X
        S = D - 1
    for i in range(S, -1, -1):
        ndp = [0] * 2
        ni = x // A[i]
        bi = A[i + 1] // A[i]
        ndp[0] = min(dp[0] + ni, dp[1] + bi - ni)
        ndp[1] = min(dp[0] + ni + 1, dp[1] + bi - ni - 1)
        dp = ndp
        x %= A[i]
    ans = dp[0]
print(ans)
