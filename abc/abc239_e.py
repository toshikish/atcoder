import sys

sys.setrecursionlimit(1000000)

N, Q = map(int, input().split())
X = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    G[Ai].append(Bi)
    G[Bi].append(Ai)
queries = [tuple(map(lambda s: int(s) - 1, input().split())) for _ in range(Q)]

K = max(queries[i][1] for i in range(Q)) + 1
P = [[] for _ in range(N)]


def dfs(v, p):
    Pv = [X[v]]
    for nv in G[v]:
        if nv == p:
            continue
        Pv.extend(dfs(nv, v))
    Pv.sort(reverse=True)
    P[v] = Pv if len(Pv) <= K else Pv[:K]
    return P[v]


dfs(0, -1)
for Vi, Ki in queries:
    print(P[Vi][Ki])
