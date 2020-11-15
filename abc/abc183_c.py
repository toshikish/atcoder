from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]

ans = 0
for p in permutations(range(1, N)):
    c = [0] + list(p) + [0]
    t = sum([T[c[i]][c[i + 1]] for i in range(N)])
    if t == K:
        ans += 1
print(ans)
