N, K = map(int, input().split())
x = list(map(int, input().split()))

ans = 10 ** 10
for i in range(N - K + 1):
    j = i + K - 1
    if x[i] <= 0 <= x[j]:
        t = x[j] - x[i] + min(x[j], -x[i])
    else:
        t = max(abs(x[i]), abs(x[j]))
    ans = min(ans, t)
print(ans)
