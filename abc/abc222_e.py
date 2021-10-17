from collections import defaultdict
import sys
sys.setrecursionlimit(2000)

N, M, K = map(int, input().split())
A = list(map(lambda s: int(s) - 1, input().split()))
G = [[] for _ in range(N)]
for i in range(N - 1):
    Ui, Vi = map(lambda s: int(s) - 1, input().split())
    G[Ui].append((Vi, i))
    G[Vi].append((Ui, i))

C = [0] * (N - 1)


def dfs(v, pv, g):
    if v == g:
        return True
    for nv, i in G[v]:
        if nv == pv:
            continue
        if dfs(nv, v, g):
            C[i] += 1
            return True
    return False


for i in range(M - 1):
    dfs(A[i], -1, A[i + 1])

S = sum(C)
if (S + K) % 2 == 1 or K < -S:
    ans = 0
else:
    MOD = 998244353
    dp = defaultdict(int)
    dp[0] = 1
    for i in range(N - 1):
        ndp = defaultdict(int)
        for d, v in dp.items():
            ndp[d + C[i]] += v
            ndp[d - C[i]] += v
        for d in ndp.keys():
            ndp[d] %= MOD
        dp = ndp
    ans = dp[K]
print(ans)
