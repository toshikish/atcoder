from collections import deque

R, C = map(int, input().split())
sy, sx = map(lambda s: int(s) - 1, input().split())
gy, gx = map(lambda s: int(s) - 1, input().split())
c = [input() for i in range(R)]

visited = [[False] * C for i in range(R)]
d = [[0] * C for i in range(R)]
q = deque()
q.append((sx, sy))
while len(q) > 0:
    x, y = q.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < C and 0 <= ny < R and c[ny][nx] != '#' and not visited[ny][nx]:
            visited[ny][nx] = True
            d[ny][nx] = d[y][x] + 1
            q.append((nx, ny))
print(d[gy][gx])
