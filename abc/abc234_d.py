from heapq import heapify, heappushpop

N, K = map(int, input().split())
P = list(map(int, input().split()))

hq = sorted(P[:K])
heapify(hq)
print(hq[0])
for i in range(K, N):
    heappushpop(hq, P[i])
    print(hq[0])
