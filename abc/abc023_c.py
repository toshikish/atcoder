from collections import defaultdict
from itertools import product

R, C, K = map(int, input().split())
N = int(input())
r2n = defaultdict(int)
c2n = defaultdict(int)
candies = set()
for i in range(N):
    r, c = map(int, input().split())
    r2n[r] += 1
    c2n[c] += 1
    candies.add((r, c))

n2lr = defaultdict(int)
n2lc = defaultdict(int)
for i in range(1, R + 1):
    n2lr[r2n[i]] += 1
for i in range(1, C + 1):
    n2lc[c2n[i]] += 1

ans = 0
for nr in range(K + 1):
    ans += n2lr[nr] * n2lc[K - nr]

for r, c in candies:
    s = r2n[r] + c2n[c]
    if s == K:
        ans -= 1
    elif s == K + 1:
        ans += 1
print(ans)
