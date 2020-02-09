N, K = map(int, input().split())
p = list(map(int, input().split()))

S = sum(p[0:K])
max_S = S
for i in range(N - K):
    S += p[i + K] - p[i]
    max_S = max(S, max_S)
print((max_S + K) / 2)
