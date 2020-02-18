from collections import defaultdict

N, M = map(int, input().split())
neighbors = defaultdict(list)
for i in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    neighbors[Ai].append(Bi)
    neighbors[Bi].append(Ai)

for i in range(N):
    d = [M + 1] * N
    d[i] = 0
    for n in neighbors[i]:
        d[n] = 1
    ans = 0
    for n in neighbors[i]:
        for nn in neighbors[n]:
            if d[nn] == M + 1:
                d[nn] = 2
                ans += 1
    print(ans)
