from collections import defaultdict
import heapq

N, M = map(int, input().split())
works = defaultdict(list)
for i in range(N):
    A, B = map(int, input().split())
    works[A].append(B)

ans = 0
min_A = min(works.keys())
if min_A < M:
    a = min_A
    bag = []
    heapq.heapify(bag)
    while a <= M:
        d = M - a
        for w in works[a]:
            heapq.heappush(bag, -w)
        if len(bag) >= 1:
            ans -= heapq.heappop(bag)
        a += 1
print(ans)
