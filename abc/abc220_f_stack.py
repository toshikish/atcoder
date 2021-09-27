from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    ui, vi = map(int, input().split())
    ui -= 1
    vi -= 1
    G[ui].append(vi)
    G[vi].append(ui)

order = []
S = deque()
S.append((0, -1))
while S:
    v, p = S.pop()
    order.append((v, p))
    for nv in G[v]:
        if nv == p:
            continue
        S.append((nv, v))

size = [1] * N
ans = [0] * N

for v, p in order[:0:-1]:
    size[p] += size[v]
    ans[0] += size[v]

for v, p in order[1:]:
    ans[v] = ans[p] + N - size[v] * 2

for i in range(N):
    print(ans[i])
