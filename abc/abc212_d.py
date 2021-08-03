from heapq import heappush, heappop

Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

a = 0
h = []
for query in queries:
    t = query[0]
    if t == 3:
        print(heappop(h) + a)
        continue
    Xi = query[1]
    if t == 1:
        heappush(h, Xi - a)
    elif t == 2:
        a += Xi
