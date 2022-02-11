from collections import defaultdict, deque

N, Q = map(int, input().split())
G = defaultdict(list)
for _ in range(Q):
    li, ri = map(int, input().split())
    li -= 1
    G[li].append(ri)
    G[ri].append(li)

visited = [False] * (N + 1)
q = deque([0])
visited[0] = True
while q:
    v = q.popleft()
    for nv in G[v]:
        if visited[nv]:
            continue
        q.append(nv)
        visited[nv] = True

print('Yes' if visited[N] else 'No')
