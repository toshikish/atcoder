from itertools import product
from collections import deque

A = [list(input()) for i in range(10)]
G = [Ai[:] for Ai in A]

n = 0
for i, j in product(range(10), repeat=2):
    if G[i][j] != 'o':
        continue
    n += 1
    q = deque([(i, j)])
    while len(q) > 0:
        ii, jj = q.popleft()
        G[ii][jj] = n
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = ii + di, jj + dj
            if 0 <= ni < 10 and 0 <= nj < 10 and G[ni][nj] == 'o':
                q.append((ni, nj))

ans = False
if n <= 4:
    target_f = (1 << n + 1) - 2
    for i, j in product(range(10), repeat=2):
        if A[i][j] == 'o':
            continue
        f = 0
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 10 and 0 <= nj < 10 and G[ni][nj] != 'x':
                f |= 1 << G[ni][nj]
        if f == target_f:
            ans = True
            break

print('YES' if ans else 'NO')
