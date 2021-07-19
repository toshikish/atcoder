H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
INF = 1e14

ans = INF

for _ in range(2):
    D = [[INF] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            s = INF
            if i - 1 >= 0:
                s = min(s, D[i - 1][j])
            if j - 1 >= 0:
                s = min(s, D[i][j - 1])
            ans = min(ans, s + A[i][j] + C * (i + j))
            D[i][j] = min(s, A[i][j] - C * (i + j))
    A = A[::-1]

print(ans)
