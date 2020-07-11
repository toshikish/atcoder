from collections import defaultdict
from itertools import product

N = int(input())

f = defaultdict(int)
for x, y, z in product(range(1, 100), repeat=3):
    n = x * x + y * y + z * z + x * y + y * z + z * x
    f[n] += 1

for i in range(1, N + 1):
    print(f[i])
