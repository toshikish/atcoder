from collections import defaultdict, deque

N, Q = map(int, input().split())
adjacent = defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adjacent[a].append(b)
    adjacent[b].append(a)
ans = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x

q = deque([(0, -1)])
while len(q) > 0:
    u, p = q.pop()
    for v in adjacent[u]:
        if v == p:
            continue
        ans[v] += ans[u]
        q.appendleft((v, u))
print(' '.join([str(ans[i]) for i in range(N)]))
