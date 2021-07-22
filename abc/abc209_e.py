from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

edges = [(w[:3], w[-3:]) for w in words]
M = 0
num = {}
for e in edges:
    for p in e:
        if p in num:
            continue
        num[p] = M
        M += 1

origin = [[] for _ in range(M)]
deg = [0] * M
for pre, post in edges:
    pr = num[pre]
    po = num[post]
    origin[po].append(pr)
    deg[pr] += 1

ans = [0] * M
q = deque()
for i in range(M):
    if deg[i] == 0:
        ans[i] = -1
        q.append(i)
while q:
    v = q.popleft()
    if ans[v] == -1:
        for u in origin[v]:
            if ans[u] != 0:
                continue
            ans[u] = 1
            q.append(u)
    elif ans[v] == 1:
        for u in origin[v]:
            if ans[u] != 0:
                continue
            deg[u] -= 1
            if deg[u] == 0:
                ans[u] = -1
                q.append(u)

phrase = ['Takahashi', 'Draw', 'Aoki']
for _, post in edges:
    print(phrase[ans[num[post]] + 1])
