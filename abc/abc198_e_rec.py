import sys

sys.setrecursionlimit(100000)

N = int(input())
C = list(map(lambda s: int(s) - 1, input().split()))
neighbors = [[] for _ in range(N)]
for _ in range(N - 1):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    neighbors[Ai].append(Bi)
    neighbors[Bi].append(Ai)

ans = []
used = [0] * (max(C) + 1)


def dfs(v, p):
    if used[C[v]] == 0:
        ans.append(v + 1)
    used[C[v]] += 1
    for nv in neighbors[v]:
        if nv == p:
            continue
        dfs(nv, v)
    used[C[v]] -= 1
    return


dfs(0, -1)
ans.sort()
for v in ans:
    print(v)
