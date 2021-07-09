H, W, N, M = map(int, input().split())
S = [['.'] * W for _ in range(H)]
L = []
for _ in range(N):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    S[Ai][Bi] = 'L'
    L.append((Ai, Bi))
for _ in range(M):
    Ci, Di = map(lambda s: int(s) - 1, input().split())
    S[Ci][Di] = '#'

Hr = [[False] * W for _ in range(H)]
Vt = [[False] * W for _ in range(H)]
for Ai, Bi in L:
    for di in [1, -1]:
        i = Ai
        j = Bi
        condition = True
        while condition:
            Vt[i][j] = True
            i += di
            condition = 0 <= i < H and S[i][j] != '#' and not Vt[i][j]
    for dj in [1, -1]:
        i = Ai
        j = Bi
        condition = True
        while condition:
            Hr[i][j] = True
            j += dj
            condition = 0 <= j < W and S[i][j] != '#' and not Hr[i][j]

print([Hr[i][j] or Vt[i][j] for i in range(H) for j in range(W)].count(True))
