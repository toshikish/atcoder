from itertools import combinations
from math import gcd

N = int(input())
P = [tuple(map(int, input().split())) for i in range(N)]


def norm(x, y):
    if x == 0 and y == 0:
        return (0, 0)
    elif x == 0:
        return (0, 1)
    elif y == 0:
        return (1, 0)
    if x < 0:
        x *= -1
        y *= -1
    g = gcd(x, y)
    return (x // g, y // g)


ans = False
for p1, p2, p3 in combinations(P, 3):
    if norm(p2[0] - p1[0], p2[1] - p1[1]) == norm(p3[0] - p1[0], p3[1] - p1[1]):
        ans = True
        break
print('Yes' if ans else 'No')
