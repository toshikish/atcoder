from collections import defaultdict, deque

N, M = map(int, input().split())
neighbors = defaultdict(list)
for i in range(M):
    ui, vi = map(lambda s: int(s) - 1, input().split())
    neighbors[ui].append(vi)
    neighbors[vi].append(ui)

G = [0] * N
ans = 0
n = 1
for i in range(N):
    if G[i] != 0:
        continue
    is_tree = True
    G[i] = n
    S = deque([(i, -1)])
    while len(S) > 0:
        v, p = S.pop()
        for c in neighbors[v]:
            if c == p:
                continue
            if G[c] == n:
                is_tree = False
            else:
                G[c] = n
                S.append((c, v))
    if is_tree:
        ans += 1
    n += 1
print(ans)
