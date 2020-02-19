from collections import defaultdict, deque

N = int(input())
neighbors = defaultdict(list)
for i in range(N - 1):
    ai, bi, ci = map(int, input().split())
    ai -= 1
    bi -= 1
    neighbors[ai].append((bi, ci))
    neighbors[bi].append((ai, ci))
Q, K = map(int, input().split())
K -= 1
queries = [tuple(map(lambda s: int(s) - 1, input().split())) for i in range(Q)]

queue = deque([K])
d = [0] * N
while len(queue) > 0:
    v = queue.pop()
    for child, ci in neighbors[v]:
        if child == K or d[child] != 0:
            continue
        d[child] = d[v] + ci
        queue.append(child)

for xi, yi in queries:
    print(d[xi] + d[yi])
