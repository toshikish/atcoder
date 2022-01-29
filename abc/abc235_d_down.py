from collections import deque

a, N = map(int, input().split())

M = 1
n = N
while n > 0:
    M *= 10
    n //= 10
d = [-1] * M
d[N] = 0
q = deque([N])
while q:
    x = q.popleft()
    candidates = []
    if x % a == 0:
        candidates.append(x // a)
    s = str(x)
    if x >= 10 and s[1] != '0':
        candidates.append(int(s[1:] + s[0]))
    for nx in candidates:
        if nx < M and d[nx] == -1:
            d[nx] = d[x] + 1
            q.append(nx)

print(d[1])
