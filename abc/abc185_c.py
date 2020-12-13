from functools import reduce
from operator import mul

L = int(input())
numer = reduce(mul, range(L - 1, L - 12, -1), 1)
denom = reduce(mul, range(1, 12), 1)
print(numer // denom)
