import heapq

N, K = map(int, input().split())
S = []
for i in range(N):
    t, d = map(int, input().split())
    heapq.heappush(S, (-d, t))

sum_d = 0
types = set()
surplus = []
for i in range(K):
    _d, t = heapq.heappop(S)
    sum_d += -_d
    if t in types:
        heapq.heappush(surplus, -_d)
    else:
        types.add(t)
len_types = len(types)
ans = sum_d + len_types * len_types

while S and surplus:
    _d, t = heapq.heappop(S)
    if t in types:
        continue
    types.add(t)
    removed_d = heapq.heappop(surplus)
    sum_d += -_d - removed_d
    len_types += 1
    ans = max(ans, sum_d + len_types * len_types)
print(ans)
