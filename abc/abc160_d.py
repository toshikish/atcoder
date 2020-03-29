N, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1

ans = [0] * (N - 1)
for i in range(N - 1):
    for j in range(i + 1, N):
        d = min(j - i, abs(X - i) + 1 + abs(Y - j),
                abs(Y - i) + 1 + abs(X - j))
        ans[d - 1] += 1

for k in range(N - 1):
    print(ans[k])
