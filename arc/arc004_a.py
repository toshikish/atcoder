from itertools import combinations
from math import sqrt

N = int(input())
P = [tuple(map(int, input().split())) for i in range(N)]

ans = 0
for p1, p2 in combinations(P, 2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    ans = max(ans, dx * dx + dy * dy)
print(sqrt(ans))
