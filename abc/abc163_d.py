N, K = map(int, input().split())
MOD = 1_000_000_007

ans = 0
for k in range(K, N + 2):
    ans += k * (N - k + 1) + 1
    ans %= MOD
print(ans)
