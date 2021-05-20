H, W = map(int, input().split())
A = [input() for _ in range(H)]

S = [[0] * W for _ in range(H)]
for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        if i == H - 1 and j == W - 1:
            continue

        candidates = []
        if i + 1 < H:
            candidates.append((i + 1, j))
        if j + 1 < W:
            candidates.append((i, j + 1))
        if (i + j) % 2 == 0:
            S[i][j] = max([S[ni][nj] + (1 if A[ni][nj] == '+' else -1)
                           for ni, nj in candidates])
        else:
            S[i][j] = min([S[ni][nj] - (1 if A[ni][nj] == '+' else -1)
                           for ni, nj in candidates])

score = S[0][0]
print('Takahashi' if score > 0 else 'Draw' if score == 0 else 'Aoki')
