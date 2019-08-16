import queue

N, M = map(int, input().split())
adjacent = [[False] * N for i in range(N)]
bridges = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    bridges.append((a, b))
    adjacent[a][b] = adjacent[b][a] = True

ans = 0
for a, b in bridges:
    adjacent[a][b] = adjacent[b][a] = False
    visited = [0] * N

    visited[0] = 1
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in range(N):
            if not adjacent[u][v]:
                continue
            if visited[v] == 1:
                continue
            visited[v] = 1
            q.put(v)

    if sum(visited) < N:
        ans += 1
    adjacent[a][b] = adjacent[b][a] = True
print(ans)
