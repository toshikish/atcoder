from bisect import bisect
from itertools import accumulate

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

accumA = [0] + list(accumulate(A))
accumB = list(accumulate(B))
ans = 0
for i in range(N + 1):
    if accumA[i] > K:
        break
    n = i + bisect(accumB, K - accumA[i])
    ans = max(n, ans)
print(ans)
