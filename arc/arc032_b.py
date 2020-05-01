from collections import defaultdict, deque

N, M = map(int, input().split())
X = defaultdict(list)
for i in range(M):
    ai, bi = map(lambda s: int(s) - 1, input().split())
    X[ai].append(bi)
    X[bi].append(ai)

G = [-1] * N
c = -1
for i in range(N):
    if G[i] != -1:
        continue
    Q = deque([i])
    c += 1
    while len(Q) > 0:
        p = Q.popleft()
        G[p] = c
        for x in X[p]:
            if G[x] != -1:
                continue
            Q.append(x)
print(c)
