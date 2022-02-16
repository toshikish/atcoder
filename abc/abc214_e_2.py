from collections import defaultdict
from heapq import heapify, heappush, heappop

T = int(input())
INF = 1_000_000_007

for _ in range(T):
    N = int(input())
    D = defaultdict(list)
    for _ in range(N):
        Li, Ri = map(int, input().split())
        D[Li].append(Ri)
    D[INF].append(INF)
    hq = []
    ans = True
    L = list(D.keys())
    heapify(L)
    x = L[0]
    while x <= 1_000_000_000:
        if x == L[0]:
            heappop(L)
            for Ri in D[x]:
                heappush(hq, Ri)
        heappop(hq)
        if hq:
            if hq[0] <= x:
                ans = False
                break
            x += 1
        else:
            x = L[0]
    if hq:
        ans = False
    print('Yes' if ans else 'No')
