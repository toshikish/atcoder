from collections import defaultdict
import heapq

N = int(input())
X = defaultdict(list)
for i in range(N - 1):
    ai, bi = map(int, input().split())
    X[ai].append(bi)
    X[bi].append(ai)

ans = []
q = [1]
visited = [False] * N
while len(q) > 0:
    v = heapq.heappop(q)
    ans.append(v)
    visited[v - 1] = True
    for nv in X[v]:
        if visited[nv - 1]:
            continue
        heapq.heappush(q, nv)

print(' '.join(list(map(str, ans))))
