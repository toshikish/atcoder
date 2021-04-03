from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi, Ci = input().split()
    Ai, Bi = map(lambda s: int(s) - 1, [Ai, Bi])
    Ci = ord(Ci) - ord('a')
    g[Ai].append((Bi, Ci))
    g[Bi].append((Ai, Ci))

INF = 1000000007
dp = [[INF] * N for _ in range(N)]
q = deque()


def push(a, b, c):
    if dp[a][b] != INF:
        return
    dp[a][b] = c
    q.append((a, b, c))


push(0, N - 1, 0)
while q:
    a, b, c = q.popleft()
    for ea, ca in g[a]:
        for eb, cb in g[b]:
            if ca != cb:
                continue
            push(ea, eb, dp[a][b] + 1)

ans = min([INF] + [dp[i][i] * 2 for i in range(N)]
          + [dp[i][ei] * 2 + 1 for i in range(N) for ei, _ in g[i]])
print(-1 if ans == INF else ans)
