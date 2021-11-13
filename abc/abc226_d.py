from itertools import permutations
from math import gcd

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

S = set()
for i, j in permutations(range(N), 2):
    dx, dy = P[j][0] - P[i][0], P[j][1] - P[i][1]
    g = gcd(dx, dy)
    S.add((dx // g, dy // g))
print(len(S))
