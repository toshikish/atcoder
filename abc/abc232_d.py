from collections import deque

H, W = map(int, input().split())
C = [input() for _ in range(H)]

visited = [[False] * W for _ in range(H)]
ans = 1
q = deque([(0, 0)])
while q:
    i, j = q.popleft()
    ans = max(ans, i + j + 1)
    for nx in [(i + 1, j), (i, j + 1)]:
        if nx[0] >= H or nx[1] >= W or visited[nx[0]][nx[1]] or C[nx[0]][nx[1]] == '#':
            continue
        visited[nx[0]][nx[1]] = True
        q.append(nx)
print(ans)
