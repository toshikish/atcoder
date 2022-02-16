from heapq import heappush, heappop

T = int(input())
INF = 1_000_000_007

for _ in range(T):
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)] + [(INF, INF)]
    P.sort()
    hq = []
    x = 1
    ans = True
    for l, r in P:
        while x < l and hq:
            if hq[0] < x:
                ans = False
                break
            heappop(hq)
            x += 1
        else:
            heappush(hq, r)
            x = l
            continue
        break
    print('Yes' if ans else 'No')
