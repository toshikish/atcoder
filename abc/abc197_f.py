from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N)]
adj = [[False] * N for _ in range(N)]
for _ in range(M):
    Ai, Bi, Ci = input().split()
    Ai = int(Ai) - 1
    Bi = int(Bi) - 1
    Ci = ord(Ci) - ord('a')
    g[Ai].append((Bi, Ci))
    g[Bi].append((Ai, Ci))
    adj[Ai][Bi] = adj[Bi][Ai] = True

INF = 1000000007
dp = [[INF] * N for _ in range(N)]
q = deque()
ans = INF


def push(a, b, c):
    if dp[a][b] != INF:
        return
    dp[a][b] = c
    q.append((a, b, c))


push(0, N - 1, 0)
while q:
    a, b, c = q.popleft()
    if c >= ans:
        break
    if a == b:
        ans = c
        break
    if adj[a][b]:
        ans = c + 1
        continue
    for ea, ca in g[a]:
        for eb, cb in g[b]:
            if ca != cb:
                continue
            push(ea, eb, dp[a][b] + 2)

print(-1 if ans == INF else ans)
