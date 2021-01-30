N, M = map(int, input().split())
AB = [tuple(map(lambda s: int(s) - 1, input().split())) for i in range(M)]
K = int(input())
CD = [tuple(map(lambda s: int(s) - 1, input().split())) for i in range(K)]

ans = 0
for p in range(1 << K):
    dishes = [False] * N
    for i in range(K):
        dishes[CD[i][p >> i & 1]] = True
    a = [dishes[Ai] and dishes[Bi] for Ai, Bi in AB].count(True)
    ans = max(ans, a)
print(ans)
