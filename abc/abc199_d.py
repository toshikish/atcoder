from collections import defaultdict, deque

N, M = map(int, input().split())
neighbors = defaultdict(list)
for _ in range(M):
    A, B = map(lambda s: int(s) - 1, input().split())
    neighbors[A].append(B)
    neighbors[B].append(A)

ans = 1
visited = [False] * N
for i in range(N):
    if visited[i]:
        continue
    order = []
    q = deque([i])
    visited[i] = True
    while q:
        v = q.pop()
        order.append(v)
        for nv in neighbors[v]:
            if visited[nv]:
                continue
            q.append(nv)
            visited[nv] = True

    L = len(order)
    color = [-1] * N

    def dfs(j):
        if j == L - 1:
            return 1
        t = 0
        v = order[j + 1]
        for c in range(3):
            if any([color[nv] == c for nv in neighbors[v]]):
                continue
            color[v] = c
            t += dfs(j + 1)
            color[v] = -1
        return t

    color[i] = 0
    ans *= dfs(0) * 3
    if ans == 0:
        break
print(ans)
