import pprint
from collections import defaultdict
import sys
n = int(input())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
if sum(a) < sum(b):
    print(-1)
    sys.exit()
min_i = 0
residue = 0
repos = defaultdict(int)
for i in range(n):
    tmp = a[i] - b[i]
    if tmp < 0:
        min_i += 1
        residue = -tmp
    elif tmp > 0:
        repos[tmp] += 1
repo_keys = sorted(repos.keys(), reverse=True)
#pprint.pprint(repo_keys)
print(min_i)
while residue > 0:
    k = repo_keys.pop(0)
    v = repos[k]
    if k * v >= residue:
        min_i += int(residue / k) + (residue % k > 0)
        break
    else:
        residue -= k * v
        min_i += v
print(min_i)
