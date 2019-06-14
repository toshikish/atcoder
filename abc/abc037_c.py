N, K = map(int, input().split())
a = list(map(int, input().split()))

n = {}
ans = 0
for i in range(N):
    if i not in n:
        n[i] = n[N - 1 - i] = min(i + 1, K, N - K + 1)
    ans += a[i] * n[i]
print(ans)
