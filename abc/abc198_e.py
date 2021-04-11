from collections import deque

N = int(input())
C = list(map(lambda s: int(s) - 1, input().split()))
neighbors = [[] for _ in range(N)]
for _ in range(N - 1):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    neighbors[Ai].append(Bi)
    neighbors[Bi].append(Ai)

q = deque()
q.append((0, 0, 0))
ans = []
while q:
    v, pv, used = q.popleft()
    if used >> C[v] & 1 == 0:
        ans.append(v + 1)
    used |= 1 << C[v]
    for nv in neighbors[v]:
        if nv == pv:
            continue
        q.append((nv, v, used))

ans.sort()
for v in ans:
    print(v)
