N, M = map(int, input().split())
INF = 1000000007
D = [[INF] * N for i in range(N)]
for i in range(N):
    D[i][i] = 0
for i in range(M):
    ai, bi, ti = map(int, input().split())
    ai -= 1
    bi -= 1
    D[ai][bi] = D[bi][ai] = ti

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
print(min(max(D[i][:i] + D[i][i + 1:]) for i in range(N)))
