from itertools import accumulate
from bisect import bisect_left

N, K = map(int, input().split())
a = [int(input()) for i in range(N)]

A = list(accumulate(a))
print(bisect_left(A, K) + 1)
