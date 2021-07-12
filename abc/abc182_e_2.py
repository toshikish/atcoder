from sys import stdin
input = stdin.readline

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

L = [[False] * W for _ in range(H)]
memo = [[False] * W for _ in range(H)]
for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    visited = [[False] * W for _ in range(H)]

    def f(i, j):
        if not (0 <= i < H and 0 <= j < W):
            return False
        if S[i][j] == 'L':
            return True
        if S[i][j] == '#':
            return False
        if visited[i][j]:
            return memo[i][j]
        visited[i][j] = True
        memo[i][j] = f(i + di, j + dj)
        return memo[i][j]

    for i in range(H):
        for j in range(W):
            if f(i, j):
                L[i][j] = True

print([L[i][j] for i in range(H) for j in range(W)].count(True))
