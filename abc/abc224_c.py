from itertools import combinations

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i0, i1, i2 in combinations(range(N), 3):
    dx0 = P[i1][0] - P[i0][0]
    dy0 = P[i1][1] - P[i0][1]
    dx1 = P[i2][0] - P[i0][0]
    dy1 = P[i2][1] - P[i0][1]
    if dx0 * dy1 != dx1 * dy0:
        ans += 1
print(ans)
