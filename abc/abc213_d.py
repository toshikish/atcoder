N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    G[Ai].append(Bi)
    G[Bi].append(Ai)

for i in range(N):
    G[i].sort()

source = [-1] * N
visited = [False] * N
idx = [0] * N
v = 0
ans = [v + 1]
visited[v] = True
while True:
    while idx[v] < len(G[v]):
        nv = G[v][idx[v]]
        if visited[nv]:
            idx[v] += 1
            continue
        if source[nv] == -1:
            source[nv] = v
        ans.append(nv + 1)
        visited[nv] = True
        v = nv
        break
    else:
        if v == 0:
            break
        else:
            nv = source[v]
            ans.append(nv + 1)
            v = nv

print(' '.join(list(map(str, ans))))
