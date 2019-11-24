from collections import defaultdict, deque


def pair(a, b):
    return (a, b) if a < b else (b, a)


N = int(input())
E = []
V = defaultdict(list)
C = {}
for i in range(N - 1):
    a, b = map(lambda s: int(s) - 1, input().split())
    E.append((a, b))
    V[a].append(b)
    V[b].append(a)
    C[(a, b)] = 0

K = 1
Q = deque([1])
visited = [False] * N
while Q:
    v = Q.popleft()
    visited[v] = True
    used = []
    to_paint = []
    for nb in V[v]:
        if visited[nb]:
            used.append(C[pair(v, nb)])
        else:
            Q.append(nb)
            to_paint.append(nb)
    i = 0
    for tp in to_paint:
        i += 1
        while i in used:
            i += 1
        C[pair(v, tp)] = i
    K = max(i, K)

print(K)
for e in E:
    print(C[e])
