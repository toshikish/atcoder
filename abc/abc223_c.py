from bisect import bisect_right
from itertools import accumulate

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

D = [Pi[0] for Pi in P]
aD = list(accumulate(D))
T = [Pi[0] / Pi[1] for Pi in P]
aT = list(accumulate(T))
hT = aT[-1] / 2
i = bisect_right(aT, hT)
rT = hT - aT[i - 1]
print(aD[i - 1] + D[i] * rT / T[i])
