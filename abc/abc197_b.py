H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
S = [input() for _ in range(H)]

ans = -3
for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    i, j = X, Y
    while 0 <= i < H and 0 <= j < W:
        if S[i][j] == '#':
            break
        ans += 1
        i += di
        j += dj
print(ans)
