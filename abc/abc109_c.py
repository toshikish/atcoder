from fractions import gcd
from functools import reduce

N, X = map(int, input().split())
x = list(map(int, input().split()))

x.append(X)
x.sort()
diffs = set()
for i in range(N):
    diffs.add(x[i + 1] - x[i])
if len(diffs) == 1:
    ans = diffs.pop()
else:
    ans = reduce(gcd, diffs)
print(ans)
