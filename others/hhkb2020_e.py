H, W = map(int, input().split())
S = [input() for i in range(H)]
MOD = 1_000_000_007

v = [[0] * W for i in range(H)]
h = [[0] * W for i in range(H)]
for i in range(H):
    c = 0
    start = -1
    for j in range(W):
        if S[i][j] == '.':
            if c == 0:
                start = j
            c += 1
            if j < W - 1:
                continue
        if start >= 0:
            for jj in range(start, j + 1):
                h[i][jj] = c
        c = 0
        start = -1
for i in range(W):
    c = 0
    start = -1
    for j in range(H):
        if S[j][i] == '.':
            if c == 0:
                start = j
            c += 1
            if j < H - 1:
                continue
        if start >= 0:
            for jj in range(start, j + 1):
                v[jj][i] = c
        c = 0
        start = -1

K = sum([Si.count('.') for Si in S])
P = [1] * (K + 1)
for i in range(1, K + 1):
    P[i] = P[i - 1] * 2
    P[i] %= MOD

ans = K * P[K]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        ans -= P[K - v[i][j] - h[i][j] + 1]
        ans %= MOD

print(ans)
