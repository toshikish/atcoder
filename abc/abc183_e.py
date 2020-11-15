H, W = map(int, input().split())
S = [input() for i in range(H)]
MOD = 1_000_000_007

X = [[0] * W for i in range(H)]
v = [[0] * W for i in range(H)]
h = [[0] * W for i in range(H)]
d = [[0] * W for i in range(H)]
X[0][0] = v[0][0] = h[0][0] = d[0][0] = 1

for i in range(H):
    for j in range(W):
        if i == j == 0 or S[i][j] == '#':
            continue
        if 0 <= i - 1:
            X[i][j] += v[i - 1][j]
        if 0 <= j - 1:
            X[i][j] += h[i][j - 1]
        if 0 <= i - 1 and 0 <= j - 1:
            X[i][j] += d[i - 1][j - 1]
        X[i][j] %= MOD
        v[i][j] = h[i][j] = d[i][j] = X[i][j]
        if 0 <= i - 1:
            v[i][j] += v[i - 1][j]
            v[i][j] %= MOD
        if 0 <= j - 1:
            h[i][j] += h[i][j - 1]
            h[i][j] %= MOD
        if 0 <= i - 1 and 0 <= j - 1:
            d[i][j] += d[i - 1][j - 1]
            d[i][j] %= MOD
print(X[H - 1][W - 1])
