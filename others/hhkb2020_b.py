H, W = map(int, input().split())
S = [input() for i in range(H)]

ans = 0
for i in range(H):
    for j in range(W - 1):
        if S[i][j] == '.' and S[i][j + 1] == '.':
            ans += 1
for i in range(H - 1):
    for j in range(W):
        if S[i][j] == '.' and S[i + 1][j] == '.':
            ans += 1

print(ans)
