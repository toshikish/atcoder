from bisect import bisect_right
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
X = int(input())

tA = list(accumulate(A))
ans = N * (X // tA[-1]) + bisect_right(tA, X % tA[-1]) + 1
print(ans)
