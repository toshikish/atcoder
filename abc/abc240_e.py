import sys
sys.setrecursionlimit(1000000)

N = int(input())
G = [[] for _ in range(N)]
len_G = [0] * N
for _ in range(N - 1):
    ui, vi = map(lambda s: int(s) - 1, input().split())
    G[ui].append(vi)
    len_G[ui] += 1
    G[vi].append(ui)
    len_G[vi] += 1

t = 0
L = [N] * N
R = [0] * N


def dfs(v, p):
    if p != -1 and len_G[v] == 1:
        global t
        t += 1
        L[v], R[v] = t, t
        return L[v], R[v]
    for nv in G[v]:
        if nv == p:
            continue
        Li, Ri = dfs(nv, v)
        L[v] = min(Li, L[v])
        R[v] = max(Ri, R[v])
    return L[v], R[v]


dfs(0, -1)

for i in range(N):
    print(L[i], R[i])
