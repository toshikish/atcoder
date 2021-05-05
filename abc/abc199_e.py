from collections import defaultdict

N, M = map(int, input().split())
conditions = defaultdict(list)
for _ in range(M):
    Xi, Yi, Zi = map(int, input().split())
    conditions[Xi].append((Yi, Zi))


def popcount(n):
    return bin(n).count('1')


mask = [(1 << i) - 1 for i in range(N)]
dp = [0] * (1 << N)
dp[0] = 1
for s in range(1 << N):
    c = popcount(s)
    for Yi, Zi in conditions[c]:
        if popcount(s & mask[Yi]) > Zi:
            dp[s] = 0
            break
    for i in range(N):
        if (s >> i) & 1:
            continue
        dp[s | (1 << i)] += dp[s]
print(dp[(1 << N) - 1])
