N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
s = 0
r = 0
for l in range(N):
    while s < K and r < N:
        s += a[r]
        r += 1
    if s < K:
        break
    ans += N - r + 1
    s -= a[l]
print(ans)
