from itertools import combinations
from math import sqrt

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

print(sqrt(max((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2
               for P1, P2 in combinations(P, 2))))
