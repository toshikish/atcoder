from collections import deque

N, M = map(int, input().split())
g = [[[] for _ in range(26)] for _ in range(N)]
h = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi, Ci = input().split()
    Ai = int(Ai) - 1
    Bi = int(Bi) - 1
    Ci = ord(Ci) - ord('a')
    g[Ai][Ci].append(Bi)
    h[Ai].append((Bi, Ci))
    g[Bi][Ci].append(Ai)
    h[Bi].append((Ai, Ci))

INF = 1000000007
dp = [[[INF] * 27 for _ in range(N)] for _ in range(N)]
q = deque()


def push(a, b, c, x):
    if dp[a][b][c] != INF:
        return
    dp[a][b][c] = x
    q.append((a, b, c, x))


push(0, N - 1, 26, 0)
while q:
    a, b, c, x = q.popleft()
    if c == 26:
        for ea, ca in h[a]:
            push(b, ea, ca, x + 1)
    else:
        for ea in g[a][c]:
            push(b, ea, 26, x + 1)

ans = min([INF] + [min(dp[i][i] + [INF]) for i in range(N)])
print(-1 if ans == INF else ans)
