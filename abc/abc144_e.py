import numpy as np

N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))
F = np.array(list(map(int, input().split())))

A.sort()
F[::-1].sort()

sum_A = A.sum()
if sum_A <= K:
    ans = 0
else:
    high = (A * F).max()
    low = 0
    mid = (high + low) // 2
    while low < mid < high:
        if sum_A - np.minimum(A, mid // F).sum() <= K:
            high = mid
        else:
            low = mid
        mid = (high + low) // 2
    ans = high

print(ans)
