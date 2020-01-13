from collections import deque
from itertools import product

INF = 1001001001
dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

ans = 0
for i, j in product(range(H), range(W)):
    if S[i][j] == '#':
        continue
    d = [[INF] * W for i in range(H)]
    d[i][j] = 0
    q = deque([(i, j)])
    while len(q) > 0:
        x, y = q.popleft()
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] != '#' and d[nx][ny] == INF:
                d[nx][ny] = d[x][y] + 1
                ans = max(d[nx][ny], ans)
                q.append((nx, ny))
print(ans)
