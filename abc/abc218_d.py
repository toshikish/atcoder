from collections import defaultdict
from itertools import combinations

N = int(input())
P = defaultdict(set)
for _ in range(N):
    xi, yi = map(int, input().split())
    P[xi].add(yi)

ans = 0
for i, j in combinations(P.keys(), 2):
    n = len(P[i] & P[j])
    ans += n * (n - 1) // 2

print(ans)
