from collections import deque

N, M = map(int, input().split())
nx = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    nx[Ai].append(Bi)

ans = 0
for i in range(N):
    visited = [False] * N
    q = deque([i])
    while q:
        j = q.popleft()
        if visited[j]:
            continue
        visited[j] = True
        ans += 1
        for nj in nx[j]:
            if not visited[nj]:
                q.append(nj)
print(ans)
