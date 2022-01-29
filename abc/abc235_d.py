from collections import deque

a, N = map(int, input().split())

M = 1
n = N
while n > 0:
    M *= 10
    n //= 10
d = [-1] * M
d[1] = 0
q = deque([1])
while q:
    x = q.popleft()
    candidates = [a * x]
    if x >= 10 and x % 10 != 0:
        s = str(x)
        candidates.append(int(s[-1] + s[:-1]))
    for nx in candidates:
        if nx < M and d[nx] == -1:
            d[nx] = d[x] + 1
            q.append(nx)

print(d[N])
