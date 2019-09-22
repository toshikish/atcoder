N, K = map(int, input().split())
a = list(map(int, input().split()))

acum_a = [a[0]]
acum_b = [max(0, a[0])]
for i in range(1, N):
    acum_a.append(acum_a[-1] + a[i])
    acum_b.append(acum_b[-1] + max(0, a[i]))

ans = 0
for i in range(N - K + 1):
    score = 0
    if i == 0:
        score += max(0, acum_a[K - 1])
    else:
        score += acum_b[i - 1]
        score += max(0, acum_a[i + K - 1] - acum_a[i - 1])
    score += acum_b[N - 1] - acum_b[i + K - 1]
    ans = max(ans, score)
print(ans)
