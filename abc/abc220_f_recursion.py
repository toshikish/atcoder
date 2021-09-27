import sys
sys.setrecursionlimit(300000)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    ui, vi = map(int, input().split())
    ui -= 1
    vi -= 1
    G[ui].append(vi)
    G[vi].append(ui)

size = [1] * N
ans = [0] * N


def dfs1(v, p=-1):
    for nv in G[v]:
        if nv == p:
            continue
        dfs1(nv, v)
        size[v] += size[nv]
        ans[0] += size[nv]


def dfs2(v, p=-1):
    for nv in G[v]:
        if nv == p:
            continue
        ans[nv] = ans[v] + N - size[nv] * 2
        dfs2(nv, v)


dfs1(0)
dfs2(0)
for i in range(N):
    print(ans[i])
