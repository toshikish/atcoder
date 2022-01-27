from collections import defaultdict
from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = list(accumulate(A))
C = defaultdict(int)
ans = 0
for i in range(N - 1, -1, -1):
    C[B[i]] += 1
    ans += C[(0 if i == 0 else B[i - 1]) + K]
print(ans)
