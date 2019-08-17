import heapq

N, H = map(int, input().split())
b = []
max_a = 0
for i in range(N):
    ai, bi = map(int, input().split())
    heapq.heappush(b, -bi)
    max_a = max(ai, max_a)

ans = 0
while b != [] and H > 0:
    bi = -heapq.heappop(b)
    if bi < max_a:
        break
    H -= bi
    ans += 1
if H > 0:
    ans += (H + max_a - 1) // max_a
print(ans)
