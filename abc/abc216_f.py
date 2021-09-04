N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

AB = list(zip(A, B))
AB.sort()
maxA = AB[-1][0]

dp = [0] * (maxA + 1)
dp[0] = 1
ans = 0
for i in range(N):
    Ai = AB[i][0]
    Bi = AB[i][1]
    if Ai >= Bi:
        ans += sum(dp[0:Ai - Bi + 1])
        ans %= MOD
    if i == N - 1:
        break
    if maxA >= Bi:
        for j in range(maxA - Bi, -1, -1):
            dp[j + Bi] += dp[j]
            dp[j + Bi] %= MOD

print(ans)
