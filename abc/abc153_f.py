from collections import deque

N, D, A = map(int, input().split())
M = [tuple(map(int, input().split())) for i in range(N)]

M.sort()
ans = 0
diff = 0
q = deque()
for i in range(N):
    Xi, Hi = M[i]
    while len(q) > 0 and q[0][0] < Xi:
        diff += q.popleft()[1]
    Hi += diff
    if Hi <= 0:
        continue
    c = (Hi + A - 1) // A
    ans += c
    diff -= A * c
    q.append((Xi + 2 * D, A * c))
print(ans)
