from collections import deque

H, W = map(int, input().split())
s = [input() for i in range(H)]

p = [[0 for j in range(W)] for i in range(H)]
p[0][0] = 1
visited = [[False for j in range(W)] for i in range(H)]
Q = deque()
Q.append((0, 0))
while len(Q) > 0:
    i, j = Q.popleft()
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for ni, nj in neighbors:
        if 0 <= ni < H and 0 <= nj < W and s[ni][nj] != '#' and p[ni][nj] == 0 and not visited[ni][nj]:
            p[ni][nj] = p[i][j] + 1
            Q.append((ni, nj))
    visited[i][j] = True

n_black = sum([row.count('#') for row in s])
print(H * W - n_black - p[H - 1][W - 1] if p[H - 1][W - 1] != 0 else - 1)
