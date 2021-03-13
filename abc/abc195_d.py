from heapq import heappop, heappush

N, M, Q = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))
queries = [tuple(map(lambda s: int(s) - 1, input().split())) for _ in range(Q)]

items.sort()
for Li, Ri in queries:
    boxes = X[:Li] + X[Ri + 1:]
    boxes.sort()
    hq = []
    i = 0
    ans = 0
    for Xi in boxes:
        while i < N and items[i][0] <= Xi:
            heappush(hq, -items[i][1])
            i += 1
        if len(hq) > 0:
            ans += -heappop(hq)
    print(ans)
