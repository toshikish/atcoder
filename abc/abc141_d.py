import heapq

N, M = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))

heapq.heapify(A)
for i in range(M):
    a = -heapq.heappop(A)
    heapq.heappush(A, -(a // 2))
print(-sum(A))
