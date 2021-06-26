from collections import deque

N = int(input())
A = list(map(lambda s: int(s) - 1, input().split()))
M = 200000

neighbors = [set() for _ in range(M)]

for i in range(N // 2):
    if A[i] == A[N - i - 1]:
        continue
    neighbors[A[i]].add(A[N - i - 1])
    neighbors[A[N - i - 1]].add(A[i])

visited = [False] * M
ans = 0
for i in range(M):
    if visited[i] or neighbors[i] == set():
        continue
    q = deque([i])
    c = 0
    while q:
        v = q.popleft()
        if visited[v]:
            continue
        visited[v] = True
        c += 1
        for nv in neighbors[v]:
            if visited[nv]:
                continue
            q.append(nv)
    ans += c - 1

print(ans)
