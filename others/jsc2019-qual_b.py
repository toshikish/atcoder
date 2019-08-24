N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

ans = 0
for i in range(N):
    l = len([a for a in A[0:i] if a < A[i]])
    r = len([a for a in A[i + 1:N] if a < A[i]])
    ans += (K - 1) * K * (l + r) // 2 + K * r
    ans %= MOD
print(ans)
