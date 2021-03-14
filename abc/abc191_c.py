H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(H - 1):
    for j in range(W - 1):
        if [S[i + di][j + dj] for di in [0, 1] for dj in [0, 1]].count('#') % 2 == 1:
            ans += 1
print(ans)
