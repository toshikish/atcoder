N = int(input())
A = list(map(int, input().split()))
MOD = 1_000_000_007

st = [[0] * (i + 1) for i in range(N)]
st[0][0] = 1
S = 0
for i in range(N):
    S += A[i]
    dp = [st[j][S % (j + 1)] for j in range(i + 1)]
    if i == N - 1:
        break
    for j in range(1, i + 2):
        st[j][S % (j + 1)] += dp[j - 1]
        st[j][S % (j + 1)] %= MOD

print(sum(dp) % MOD)
