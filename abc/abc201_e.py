from collections import deque

N = int(input())
neighbors = [[] for _ in range(N)]
for _ in range(N - 1):
    ui, vi, wi = map(int, input().split())
    ui -= 1
    vi -= 1
    neighbors[ui].append((vi, wi))
    neighbors[vi].append((ui, wi))

d = [-1] * N
q = deque()
d[0] = 0
for nv, nw in neighbors[0]:
    q.append((0, nv, nw))
while q:
    u, v, w = q.popleft()
    d[v] = d[u] ^ w
    for nv, nw in neighbors[v]:
        if d[nv] != -1:
            continue
        q.append((v, nv, nw))

MOD = 1_000_000_007
ans = 0
for b in range(60):
    c = [0] * 2
    for i in range(N):
        c[d[i] >> b & 1] += 1
    ans += c[0] * c[1] * 1 << b
    ans %= MOD
print(ans)
