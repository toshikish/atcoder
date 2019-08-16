from collections import defaultdict
import queue

N = int(input())
to = defaultdict(list)
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    to[u].append((v, w))
    to[v].append((u, w))

ans = [-1] * N
ans[0] = 0
q = queue.Queue()
q.put(0)
while not q.empty():
    u = q.get()
    for v, w in to[u]:
        if ans[v] != -1:
            continue
        ans[v] = (ans[u] + w) % 2
        q.put(v)

for i in range(N):
    print(ans[i])
