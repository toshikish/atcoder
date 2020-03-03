N, K = map(int, input().split())

ans = 0
for bi in range(K + 1, N + 1):
    q = N // bi
    r = N % bi
    ans += (bi - K) * q + max(0, r - K + 1)
if K == 0:
    ans -= N
print(ans)
